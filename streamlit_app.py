import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Título do app
st.title("Análise de Desempenho de Ações")

# Entrada de dados pelo usuário
st.sidebar.header("Parâmetros de entrada")
acoes = st.sidebar.text_input("Digite os códigos das ações separados por vírgula (ex: AAPL, MSFT, TSLA)", "AAPL, MSFT")
inicio = st.sidebar.date_input("Data de início", pd.to_datetime("2023-01-01"))
fim = st.sidebar.date_input("Data de fim", pd.to_datetime("today"))

# Processar a entrada do usuário
symbols = [acao.strip() for acao in acoes.split(",")]

if st.sidebar.button("Gerar Gráficos"):
    if symbols:
        st.subheader(f"Gráficos de Desempenho ({inicio} a {fim})")
        for symbol in symbols:
            try:
                # Baixar dados da ação
                dados = yf.download(symbol, start=inicio, end=fim)
                if dados.empty:
                    st.warning(f"Sem dados para {symbol}. Verifique o código.")
                    continue
                
                # Gráfico de fechamento ajustado
                st.write(f"Desempenho de: {symbol}")
                plt.figure(figsize=(10, 5))
                plt.plot(dados['Adj Close'], label=symbol)
                plt.title(f"Fechamento Ajustado - {symbol}")
                plt.xlabel("Data")
                plt.ylabel("Preço ($)")
                plt.legend()
                st.pyplot(plt)
            except Exception as e:
                st.error(f"Erro ao processar {symbol}: {e}")
    else:
        st.error("Nenhuma ação foi informada!")
