import streamlit as st
import rdkit
from rdkit import Chem
from rdkit.Chem import Draw, rdDepictor
# 環状化合物をきれいに描画 https://future-chem.com/rdkit-coordgen/
# rdDepictor.SetPreferCoordGen(True)



# Header
st.title("Retro-inversian")
st.write("rdkit version", rdkit.__version__)
