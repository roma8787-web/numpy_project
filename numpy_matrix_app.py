
import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="🔢 NumPy Matrix App", layout="centered")

st.title("🔢 NumPy Matrix Operations")
st.markdown("Carica due matrici (in formato CSV) ed esegui operazioni matematiche di base.")

# Caricamento matrici
file1 = st.file_uploader("📂 Carica la prima matrice (CSV)", type="csv")
file2 = st.file_uploader("📂 Carica la seconda matrice (CSV)", type="csv")

if file1 and file2:
    try:
        mat1 = pd.read_csv(file1, header=None).to_numpy()
        mat2 = pd.read_csv(file2, header=None).to_numpy()

        st.subheader("🧮 Matrice A")
        st.dataframe(mat1)

        st.subheader("🧮 Matrice B")
        st.dataframe(mat2)

        if mat1.shape == mat2.shape:
            st.success("✅ Le matrici hanno la stessa forma, si possono sommare e sottrarre.")
            
            st.subheader("➕ Somma (A + B)")
            st.write(mat1 + mat2)

            st.subheader("➖ Differenza (A - B)")
            st.write(mat1 - mat2)
        else:
            st.warning("⚠️ Le matrici non hanno la stessa forma: somma e differenza non possibili.")

        # Prodotto
        if mat1.shape[1] == mat2.shape[0]:
            st.subheader("✖️ Prodotto Matriciale (A × B)")
            st.write(np.dot(mat1, mat2))
        else:
            st.warning("⚠️ Numero di colonne di A diverso dal numero di righe di B: prodotto non possibile.")

        # Trasposizione
        st.subheader("🔁 Trasposte")
        st.write("📌 Aᵀ:")
        st.write(mat1.T)
        st.write("📌 Bᵀ:")
        st.write(mat2.T)

    except Exception as e:
        st.error("❌ Errore nel caricamento delle matrici. Verifica il formato dei file.")
        st.exception(e)
else:
    st.info("🔽 Carica due file CSV per iniziare. Ogni cella deve contenere un numero.")
