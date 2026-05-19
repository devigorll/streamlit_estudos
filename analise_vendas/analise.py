import streamlit as st
import pandas as pd

st.set_page_config(layout = "wide")

with st.sidebar:
    st.title("Análise de lucro")

    uploades_file = st.file_uploader("Faça upload do arquivo de vendas", type = "csv")
     
if uploades_file is not None:
    df = pd.read_csv(uploades_file)
    
    with st.sidebar:

        distinct_regions = df["Region"].unique().tolist()
        selected_region = st.selectbox("Região específica", options = distinct_regions)

        selected_seller = st.radio("Vendedor específico", options = ["H", "C", "M", "L"], index = None)

        if selected_region:
            df = df[df["Region"] == selected_region]

        if selected_seller:
            df = df[df["Order Priority"] == selected_seller]

    st.title("Lucro por tipo de item")

    st.bar_chart(df, x = "Item Type", y= "Total Profit")
    st.dataframe(df, use_container_width= True)