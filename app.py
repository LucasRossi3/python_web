from flask import Flask, render_template

app = Flask(__name__)

# POSTS MOCK
posts = [
    {
        "titulo": "Post 1",
        "texto": "Meu primeiro post"
    }, 
    {   
        "titulo": "Post 2",
        "texto": "Meu segundo post"
    },
    {   
        "titulo": "Post 3",
        "texto": "Meu terceiro post"
    }
]

@app.route("/")
def exibir_entradas():
    return render_template('exibir_entradas.html', legal=posts)

@app.route("/legal")
def legal():
    return "<h1>Voce é muito legal</h1>"