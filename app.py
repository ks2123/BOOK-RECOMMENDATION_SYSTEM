# pyrefly: ignore [missing-import]
import streamlit as st

st.set_page_config(page_title="Book Recommender System", layout="wide")

st.title(" Book Recommendation System")
st.write("Collaborative Filtering based Recommendation Engine")


selected_book = st.selectbox(
    "Type or select a book from the list:",
    ["1984", "The Two Towers", "Harry Potter and the Chamber of Secrets"]
)

if st.button("Recommend"):
    st.success(f"Fetching recommendations for: {selected_book}")