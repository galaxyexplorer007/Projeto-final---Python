from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacao = request.form["operacao"]

            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                resultado = "Erro: divisão por zero" if num2 == 0 else num1 / num2
        except Exception as e:
            resultado = f"Erro: {e}"
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")