import streamlit as st

st.title("🔍 Find Workers")

service_type = st.selectbox(
    "Select Service",
    [
        "Wardrobe Repair",
        "Welding",
        "Gate Repair",
        "Fabrication"
    ]
)

location = st.text_input("Enter Location")

preferred_date = st.date_input(
    "Preferred Service Date"
)

urgency = st.selectbox(
    "Urgency",
    [
        "Normal",
        "Urgent (Within 24 Hours)",
        "Emergency"
    ]
)

damage_image = st.file_uploader(
    "Upload Damage Image"
)

description = st.text_area(
    "Describe the Problem"
)

if st.button("Submit Request"):

    if "requests" not in st.session_state:
        st.session_state.requests = []

    request = {
        "service": service_type,
        "location": location,
        "date": str(preferred_date),
        "urgency": urgency,
        "description": description,
        "status": "Pending"
    }

    st.session_state.requests.append(request)

    st.success("Request Submitted Successfully!")