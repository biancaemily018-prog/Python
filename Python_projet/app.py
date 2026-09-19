from flask import flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    #dados que serão calculados pelo python
    titulo_pagina = "Dashboard de Demonstração"
    aluno = {"nome": "Lucas", "Curso": "Engenharia de Software", "nota": 9.5}
    status = "Aprovado" if aluno ["nota"] >= 5.0 else "Reprovado"

    return render_template(
        "index.html",
        usuario=aluno,
        resultado=status,
    )

if __name__ == "__main__":
    app.run(debug=True)