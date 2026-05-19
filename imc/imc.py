import streamlit as st

with st.sidebar:
    st.title("Calculadora IMC")

    st.header("Definição de IMC")

    st.write("Índice de Massa Corporal (IMC)")
    st.write("É uma medida utilizada para avaliar se uma pessoa está com peso adequado em relação à sua altura.")
    st.write("O IMC é calculado dividindo o peso da pessoa (em kg) pela altura (em metros) ao quadrado.")

st.title("Calculadora")

peso = st.number_input(label= "Digite seu peso (kg):", min_value= 0.0, step = 0.1)
altura = st.number_input(label = "Informe sua altura (m):", min_value = 0.0, step = 0.1)

if st.button("Calcular IMC"):
    if altura > 0:

        imc = peso / (altura ** 2)
        imc_ideal = 22.5
        delta = imc - imc_ideal

        if imc < 18.5:
            resultado = {
                "Classe": 'Abaixo do peso',
                "delta": delta
            }
        elif 18.5 <= imc < 25:
            resultado = {
                "Classe": 'Peso normal',
                "delta": delta
            }
        elif 25 <= imc < 30:
            resultado = {
                "Classe": 'Sobrepeso',
                "delta": delta
            }
        else:
            resultado = {
                "Classe": 'Obesidade',
                "delta": delta
            }

        st.write(f"Resultado: {resultado}")

    else:
        st.error("A altura deve ser maior que zero.")

    col1, col2 = st.columns(2)

    col1.metric("IMC classificado", resultado["Classe"], resultado["delta"], delta_color= "inverse")
    col2.metric("IMC calculado", round(imc, 2), resultado["delta"], delta_color= "inverse")

    st.divider()

st.text("Fonte")
st.image("C:\\Users\\Igor Cruz\\OneDrive\\Área de Trabalho\\STREAMLIT\\imc\\175-x-175-3.webp")

    