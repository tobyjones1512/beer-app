import streamlit as st

st.title("🍺 Beer App")

st.header(
    "Add Pub"
)

pubName = st.text_input("Pub Name")

pubStreet = st.text_input("Pub Address Line 1 (Street)")

pubPostcode = st.text_input("Pub Postcode")