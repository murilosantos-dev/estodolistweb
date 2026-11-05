from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "dssenai"

ADMIN_EMAIL = "ventilador0409@gmail.com"
ADMIN_SENHA = "vento0409"

@app.route("/") # HomePage - Página Inicial
def home():
    if "login" not in session:
        return redirect ("/login")

    # Usuário logado
    return render_template("index.html")

# -----------------------------------------------
# Rota de login
@app.route("/login", methods=["GET", "POST"])
def login():
    if "login" in session:
        return redirect("/")
    
    if request.method == "GET":
        return render_template("login.html")

    # POST
    email = request.form.get("email") # Pegando o email que estava no form HTML
    senha = request.form.get("senha") # Está informação está no atributo name

    if email == ADMIN_EMAIL and senha == ADMIN_SENHA:
        session["login"] = True 
        return redirect('/') # Redireciona para a rota
    else:
        return render_template ("login.html", msgerro = "E-mail ou senha estão incorretos!")

# ------------------------------------------------
#Rota Logout
@app.route("/logout")
def logout():
    session.clear() #Apaga a lista sessão
    return redirect("/login")

# ------------------------------------------------
# Tratamento do erro - Código 404
@app.errorhandler(404)
def not_found(erro):
    return render_template("erro404.html")




if __name__ == "__main__":
    app.run(debug=True, port=5000)
    # host="0,0,0,0" Habilita o IP Público