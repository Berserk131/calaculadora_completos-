from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculadora():
    resultados = None
    if request.method == 'POST':
        personas = int(request.form.get('personas', 0))
        por_persona = int(request.form.get('por_persona', 0))
        paltas_mulitas = request.form.get('paltas_mulitas') == 'on'

        total_completos = personas * por_persona
        
        # Lógica de ingredientes (estimaciones estándar)
        tomates_kg = total_completos * 0.06  # 60g por completo
        # Si las paltas están mulitas (malas), compramos un 20% más por si acaso
        paltas_kg = total_completos * 0.075 * (1.2 if paltas_mulitas else 1.0)
        
        resultados = {
            "panes": total_completos,
            "vienesas": total_completos,
            "tomates_kg": round(tomates_kg, 2),
            "tomates_un": round(tomates_kg / 0.2), # promedio 200g c/u
            "paltas_kg": round(paltas_kg, 2),
            "paltas_un": round(paltas_kg / 0.15)  # promedio 150g c/u
        }

    return render_template('index.html', resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)