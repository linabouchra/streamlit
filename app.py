import streamlit as st
import pandas as pd
g
# Titre principal
st.title("Devoir Streamlit : Tableau de Bord")

# Sidebar avec les infos des étudiants
st.sidebar.title("Informations Étudiants")
st.sidebar.markdown("**Noms :** Zerouga Bouchra Lina et Bouras Sadek Rayan")
st.sidebar.markdown("**IDs :** 222231413801 et 22223141")
st.sidebar.markdown("**Groupe :** 1")

# Exemple de graphique
st.header("Exemple de Visualisation")

chart_data = pd.DataFrame({
    'Valeurs': [1, 2, 3, 4, 5, 4, 3, 2, 3, 4, 5, 6, 5]
})

st.line_chart(chart_data)
