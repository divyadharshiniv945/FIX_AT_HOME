import streamlit as st

st.title("🧑‍🏭 Become a Worker")

name = st.text_input("Full Name")

phone = st.text_input("Phone Number")

location = st.text_input("Location")

skill = st.selectbox(
    "Skill",
    [
        "Welding",
        "Wardrobe Repair",
        "Gate Repair",
        "Fabrication"
    ]
)

experience = st.number_input(
    "Years of Experience",
    min_value=0,
    max_value=50
)

about = st.text_area(
    "About Yourself"
)

portfolio_image = st.file_uploader(
    "Upload Previous Work Photo",
    type=["jpg", "jpeg", "png"]
)

if st.button("Register"):
    st.success("Worker Profile Created!")