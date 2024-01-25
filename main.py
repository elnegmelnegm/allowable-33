import streamlit as st
st.set_page_config(
    page_title="ُEDA AI Chat",
    page_icon="https://www.edaegypt.gov.eg/media/wc3lsydo/group-287.png",
    layout="wide",
)

st.markdown('''
<img src="https://www.edaegypt.gov.eg/media/wc3lsydo/group-287.png" width="250" height="100">''', unsafe_allow_html=True)
st.title("Allowable Adjustments for Chromatography Parameters")
st.header("For isocratic HPLC methods")

st.link_button("Ratio of components in mobile phase ", "https://allowable-p9chesfzkpzz6kpiqucrfx.streamlit.app/", use_container_width= True, help="This application enables the user to adjust the ratio of components in mobile phase of isocratic HPLC methods")
st.link_button("Other Adjustments for Chromatography Parameters ", "https://allowable2-estsgodghdq9sebadmkmzq.streamlit.app/", use_container_width= True, help="This application enables the user to adjust the other parameters of isocratic HPLC methods")
