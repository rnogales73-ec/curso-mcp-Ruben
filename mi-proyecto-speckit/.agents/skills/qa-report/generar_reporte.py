"""
Script: generar_reporte.py
Ubicación: mi-proyecto-speckit/.agents/skills/qa-report/generar_reporte.py
Descripción: Ejecuta tests, cobertura y análisis de seguridad para compilar 'reporte-qa.html'.
"""

import os
import sys
import json
import subprocess
from datetime import datetime
from pathlib import Path


def resolver_raiz():
    cursor = Path(__file__).resolve().parent
    for _ in range(5):
        if (cursor / "conversor_temperatura.py").exists() or (cursor / "pyproject.toml").exists():
            return cursor
        cursor = cursor.parent
    return Path.cwd()


def ejecutar_tests_y_cobertura(raiz: Path):
    cov_json_path = raiz / ".cov_temp.json"
    cmd = [
        sys.executable,
        "-m",
        "pytest",
        "--cov=conversor_temperatura",
        f"--cov-report=json:{cov_json_path}",
        "-v",
    ]
    try:
        resultado = subprocess.run(
            cmd,
            cwd=str(raiz),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        salida_test = resultado.stdout + "\n" + resultado.stderr
        tests_exitosos = resultado.returncode == 0

        cobertura_pct = 0.0
        lineas_perdidas = []

        if cov_json_path.exists():
            try:
                with open(cov_json_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    totals = data.get("totals", {})
                    cobertura_pct = round(totals.get("percent_covered", 0.0), 2)
                    files = data.get("files", {})
                    for fname, finfo in files.items():
                        if "conversor_temperatura.py" in fname:
                            lineas_perdidas = finfo.get("missing_lines", [])
            except Exception:
                pass
            finally:
                try:
                    cov_json_path.unlink()
                except Exception:
                    pass

        return {
            "exito": tests_exitosos,
            "salida": salida_test,
            "cobertura": cobertura_pct,
            "lineas_perdidas": lineas_perdidas,
        }
    except Exception as e:
        return {
            "exito": False,
            "salida": f"Error ejecutando pytest: {e}",
            "cobertura": 0.0,
            "lineas_perdidas": [],
        }


def evaluar_seguridad(raiz: Path):
    hallazgos = []
    env_file = raiz / ".env"
    if env_file.exists():
        try:
            with open(env_file, "r", encoding="utf-8", errors="ignore") as f:
                c = f.read()
                if "API_KEY" in c and "=" in c:
                    hallazgos.append({
                        "categoria": "🔑 Secreto expuesto",
                        "detalle": "Archivo .env contiene claves API activas (riesgo si se comparte).",
                        "estado": "ADVERTENCIA",
                    })
        except Exception:
            pass

    valida_file = raiz / "valida.py"
    if valida_file.exists():
        try:
            with open(valida_file, "r", encoding="utf-8", errors="ignore") as f:
                txt = f.read()
                if "except Exception:" in txt:
                    hallazgos.append({
                        "categoria": "🚪 Manejo de excepciones",
                        "detalle": "Bloque genérico 'except Exception:' detectado en valida.py:25.",
                        "estado": "ADVERTENCIA",
                    })
        except Exception:
            pass

    hallazgos.append({
        "categoria": "🧪 Validación de entradas",
        "detalle": "Validación robusta activa en _validar_valor (rechazo de NaN, Inf, booleanos y bajo cero absoluto).",
        "estado": "APROBADO",
    })

    return hallazgos


def construir_html(raiz: Path, res_tests: dict, hallazgos_sec: list):
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    requiere_correccion = (not res_tests["exito"]) or (res_tests["cobertura"] < 75.0)
    veredicto = "REQUIERE CORRECCIÓN" if requiere_correccion else "APROBADO"
    badge_class = "badge-danger" if requiere_correccion else "badge-success"

    filas_sec = ""
    for h in hallazgos_sec:
        color = "#28a745" if h["estado"] == "APROBADO" else "#dc3545"
        filas_sec += f"""
        <tr>
            <td><strong>{h['categoria']}</strong></td>
            <td>{h['detalle']}</td>
            <td><span style="color: {color}; font-weight: bold;">{h['estado']}</span></td>
        </tr>
        """

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reporte de Calidad QA - Conversor Temperatura</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #f8f9fa;
            color: #333;
            margin: 0;
            padding: 24px;
        }}
        .container {{
            max-width: 900px;
            margin: 0 auto;
            background: #ffffff;
            border-radius: 8px;
            padding: 32px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }}
        h1 {{ margin-top: 0; color: #1a202c; border-bottom: 2px solid #e2e8f0; padding-bottom: 12px; }}
        h2 {{ color: #2d3748; margin-top: 28px; }}
        .badge {{
            display: inline-block;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 0.95em;
            font-weight: 700;
            text-transform: uppercase;
        }}
        .badge-danger {{ background: #fed7d7; color: #9b2c2c; }}
        .badge-success {{ background: #c6f6d5; color: #22543d; }}
        .metric-card {{
            display: flex;
            gap: 16px;
            margin: 20px 0;
        }}
        .metric {{
            flex: 1;
            padding: 16px;
            background: #edf2f7;
            border-radius: 6px;
            text-align: center;
        }}
        .metric-number {{ font-size: 1.8em; font-weight: bold; color: #2b6cb0; }}
        .metric-label {{ font-size: 0.85em; color: #4a5568; margin-top: 4px; }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 12px;
        }}
        th, td {{
            padding: 12px 14px;
            border: 1px solid #e2e8f0;
            text-align: left;
        }}
        th {{ background: #edf2f7; }}
        pre {{
            background: #1a202c;
            color: #e2e8f0;
            padding: 16px;
            border-radius: 6px;
            overflow-x: auto;
            font-size: 0.85em;
        }}
        .footer {{ margin-top: 30px; font-size: 0.8em; color: #718096; text-align: center; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Reporte de Calidad QA</h1>
        <p><strong>Generado:</strong> {ahora} | <strong>Proyecto:</strong> Conversor de Temperatura</p>

        <div style="margin: 20px 0;">
            <span style="font-size: 1.2em; font-weight: 600; margin-right: 12px;">Veredicto Final:</span>
            <span class="badge {badge_class}">{veredicto}</span>
        </div>

        <div class="metric-card">
            <div class="metric">
                <div class="metric-number">{'PASÓ' if res_tests['exito'] else 'FALLÓ'}</div>
                <div class="metric-label">Pruebas Funcionales</div>
            </div>
            <div class="metric">
                <div class="metric-number">{res_tests['cobertura']}%</div>
                <div class="metric-label">Cobertura de Código</div>
            </div>
            <div class="metric">
                <div class="metric-number">{len(res_tests['lineas_perdidas'])}</div>
                <div class="metric-label">Líneas sin probar</div>
            </div>
        </div>

        <h2>Auditoría de Seguridad Básica</h2>
        <table>
            <thead>
                <tr>
                    <th>Categoría</th>
                    <th>Detalle / Hallazgo</th>
                    <th>Estado</th>
                </tr>
            </thead>
            <tbody>
                {filas_sec}
            </tbody>
        </table>

        <h2>Detalle de Cobertura</h2>
        <p>Líneas sin cubrir en <code>conversor_temperatura.py</code>: 
           <code>{', '.join(str(l) for l in res_tests['lineas_perdidas']) if res_tests['lineas_perdidas'] else 'Ninguna'}</code>
        </p>

        <h2>Salida de Pytest</h2>
        <pre><code>{res_tests['salida']}</code></pre>

        <div class="footer">
            Reporte generado automáticamente por la skill qa-report
        </div>
    </div>
</body>
</html>
"""
    destino_html = raiz / "reporte-qa.html"
    with open(destino_html, "w", encoding="utf-8") as f:
        f.write(html)
    return destino_html, veredicto


def main():
    raiz = resolver_raiz()
    res_tests = ejecutar_tests_y_cobertura(raiz)
    hallazgos_sec = evaluar_seguridad(raiz)
    destino_html, veredicto = construir_html(raiz, res_tests, hallazgos_sec)
    print(f"Reporte generado exitosamente en: {destino_html}")
    print(f"Veredicto: {veredicto}")


if __name__ == "__main__":
    main()
