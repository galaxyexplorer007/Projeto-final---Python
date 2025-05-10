import streamlit as st

st.set_page_config(page_title="Calculadora Web", page_icon="🧮")

st.title("🧮 Calculadora Web")

# Entrada de dados
num1 = st.number_input("Número 1")
operador = st.selectbox("Operação", ["+", "-", "*", "/"])
num2 = st.number_input("Número 2")

# Calcular
if st.button("Calcular"):
    try:
        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            if num2 == 0:
                resultado = "Erro: divisão por zero"
            else:
                resultado = num1 / num2
        st.success(f"Resultado: {resultado}")
    except Exception as e:
        st.error(f"Erro: {e}")
