import streamlit as st

import streamlit as st

st.set_page_config(
    page_title="Worker Dashboard",
    layout="wide"
)

st.title("🧑‍🏭 Worker Dashboard")

st.success("Welcome Back!")

# Metrics

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Jobs",
        "0"
    )

with col2:
    st.metric(
        "Rating",
        "0 ⭐"
    )

with col3:
    st.metric(
        "Portfolio Photos",
        "0"
    )

with col4:
    st.metric(
        "Profile Completion",
        "100%"
    )

st.divider()

# Verification Status

st.info("""
🟡 Verification Status

Your documents are currently under review.

Expected Approval Time:
24 - 48 Hours
""")

st.divider()

# Available Jobs

st.subheader("📋 Available Jobs")

if "requests" not in st.session_state:
    st.session_state.requests = []

for i, request in enumerate(st.session_state.requests):

    with st.container(border=True):

        st.subheader(request["service"])

        st.write(
            f"📍 Location: {request['location']}"
        )

        st.write(
            f"📝 {request['description']}"
        )

        col1, col2 = st.columns(2)

        with col1:
            if st.button(
                "Accept",
                key=f"accept_{i}"
            ):
                request["status"] = "Accepted"

        with col2:
            if st.button(
                "Reject",
                key=f"reject_{i}"
            ):
                request["status"] = "Rejected"

        st.write(
            f"Status: {request['status']}"
        )
st.divider()

# Portfolio

st.subheader("📸 Portfolio")

st.write("You haven't uploaded any portfolio items yet.")

if st.button("Upload Portfolio"):
    st.info("Portfolio page coming soon.")

st.divider()

# Reviews

st.subheader("⭐ Reviews")

st.write("No customer reviews yet.")

st.divider()

# Community

st.subheader("👥 Community")

st.write(
    "Connect with other workers, ask questions and share experiences."
)

if st.button("Open Community"):
    st.info("Community feature coming soon.")