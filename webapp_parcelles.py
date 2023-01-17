import streamlit as st
import pandas as pd

df_parcelles = pd.read_csv('parcelles.csv')

st.title('Chercher dans les parcelles')

nom_proprietaire = st.text_input('Nom du propriétaire')

siren = st.text_input('Siren')

if nom_proprietaire:
    df_parcelles = df_parcelles[df_parcelles['Dénomination (Propriétaire(s) parcelle)'].str.contains(nom_proprietaire, case=False, na=False)]
    st.write(df_parcelles)

if siren:
    df_parcelles = df_parcelles[df_parcelles['N° SIREN (Propriétaire(s) parcelle)'].str.contains(siren, case=False, na=False)]
    st.write(df_parcelles)
