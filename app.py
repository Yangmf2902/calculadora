from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calcular():
    resultado = None
    if request.method == 'POST':
        valor_inicial = float(request.form['valor_inicial'])
        taxa_juros = float(request.form['taxa_juros']) / 100
        tempo = int(request.form['tempo'])
        tipo_juros = request.form['tipo_juros']

        if tipo_juros == 'compostos':
            resultado = valor_inicial * (1 + taxa_juros) ** tempo
        elif tipo_juros == 'simples':
            resultado = valor_inicial + (valor_inicial * taxa_juros * tempo)

    return render_template('page.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True) 
