import streamlit as st


st.set_page_config(
    page_title="Worker Registration",
    layout="wide"
)

if "worker_step" not in st.session_state:
    st.session_state.worker_step = 1
st.title("🧑‍🏭 Become a Worker")
st.markdown("""
### Complete your worker profile

Provide your information to get verified and start receiving customer requests.
""")




# col1, col2, col3, col4 = st.columns(4)

# steps = [
#     "Basic",
#     "Professional",
#     "Verification",
#     "Portfolio"
# ]

# for i, col in enumerate([col1, col2, col3, col4], start=1):
#     with col:
#         if i < st.session_state.worker_step:
#             st.success(f"✅  {steps[i-1]}")
#         elif i == st.session_state.worker_step:
#             st.warning(f"❌ {steps[i-1]}")
#         else:
#             st.info(f"🟡 {steps[i-1]}")


if st.session_state.worker_step == 1:

      st.subheader("📋 Basic Information")

      full_name = st.text_input("Full Name")

      phone = st.text_input("Phone Number")

      email = st.text_input("Email Address")

      dob = st.date_input("Date of Birth")

      if st.button("Next ➡️"):
        st.session_state.worker_step = 2
        st.rerun()
elif st.session_state.worker_step == 2:

       st.subheader("🛠 Professional Information")

       primary_skill = st.selectbox(
        "Primary Skill",
        [
            "Welding",
            "Wardrobe Repair",
            "Gate Repair",
            "Fabrication",
            "Grill Work"
        ]
    )

       experience = st.number_input(
        "Years of Experience",
        min_value=0,
        max_value=50
    )

       service_radius = st.selectbox(
        "Service Radius",
        [
            "5 KM",
            "10 KM",
            "20 KM",
            "50 KM"
        ]
    )

       available_days = st.multiselect(
        "Available Days",
        [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]
    )

       col1, col2 = st.columns(2)

       with col1:
         if st.button("⬅️ Previous"):
            st.session_state.worker_step = 1
            st.rerun()

       with col2:
         if st.button("Next ➡️"):
            st.session_state.worker_step = 3
            st.rerun()
#  Verification
elif st.session_state.worker_step == 3:

    st.subheader("📄 Verification")

    st.info(
        "Verification helps customers trust your profile and increases your chances of getting hired."
    )

    aadhaar = st.file_uploader(
        "Upload Aadhaar Card",
        type=["pdf", "jpg", "jpeg", "png"]
    )

    selfie = st.file_uploader(
        "Upload Selfie Photo",
        type=["jpg", "jpeg", "png"]
    )

    certificate = st.file_uploader(
        "Trade Certificate (Optional)",
        type=["pdf", "jpg", "jpeg", "png"]
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅️ Previous"):
            st.session_state.worker_step = 2
            st.rerun()

    with col2:
        if st.button("Next ➡️"):
            st.session_state.worker_step = 4
            st.rerun()


# protfolio
elif st.session_state.worker_step == 4:

    st.subheader("📸 Portfolio Setup")

    st.write(
        "Show customers your previous work and tell them about your expertise."
    )

    about_me = st.text_area(
        "About Me",
        placeholder="Describe your experience, specialties, and services..."
    )

    work_photos = st.file_uploader(
        "Upload Work Photos",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )

    work_videos = st.file_uploader(
        "Upload Work Videos",
        type=["mp4", "mov", "avi"],
        accept_multiple_files=True
    )

    availability = st.selectbox(
        "Availability",
        [
            "Full Time",
            "Part Time",
            "Weekends Only",
            "On Call"
        ]
    )

    emergency_service = st.checkbox(
        "Available for Emergency Service"
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅️ Previous"):
            st.session_state.worker_step = 3
            st.rerun()

    with col2:
          if st.button("🚀 Complete Registration"):
            st.balloons()

            @st.dialog("Welcome to FIX AT HOME 🧑‍🏭")
            def welcome_popup():

              st.success("Registration Completed")

              st.markdown("""
        ### Your profile is now under review

        ✅ Basic Information Submitted

        ✅ Professional Information Submitted

        ✅ Verification Documents Uploaded

        ✅ Portfolio Added

        Estimated approval time: 24-48 hours
        """)

              if st.button("Go to Dashboard"):

                st.switch_page("pages/Worker_Dashboard.py")

            welcome_popup()
st.markdown("""
<style>
.step-box{
    text-align:center;
    padding:10px;
}

.step-circle-complete{
    width:45px;
    height:45px;
    border-radius:50%;
    background:#2563eb;
    color:white;
    font-size:20px;
    font-weight:bold;
    display:flex;
    align-items:center;
    justify-content:center;
    margin:auto;
}

.step-circle-active{
    width:45px;
    height:45px;
    border-radius:50%;
    border:4px solid #2563eb;
    color:#2563eb;
    font-size:20px;
    font-weight:bold;
    display:flex;
    align-items:center;
    justify-content:center;
    margin:auto;
}

.step-circle-pending{
    width:45px;
    height:45px;
    border-radius:50%;
    background:#d1d5db;
    color:white;
    font-size:20px;
    font-weight:bold;
    display:flex;
    align-items:center;
    justify-content:center;
    margin:auto;
}

.step-title{
    margin-top:8px;
    font-size:14px;
    font-weight:600;
}
</style>
""", unsafe_allow_html=True)





col1,col2,col3,col4 = st.columns(4)

current_step = st.session_state.worker_step

titles = [
    "Basic Info",
    "Professional",
    "Verification",
    "Portfolio"
]

icons = ["👤","🛠","📄","📸"]

cols = [col1,col2,col3,col4]

for i,col in enumerate(cols,start=1):

    if i < current_step:
        circle = "step-circle-complete"
        symbol = "✓"

    elif i == current_step:
        circle = "step-circle-active"
        symbol = icons[i-1]

    else:
        circle = "step-circle-pending"
        symbol = icons[i-1]

    with col:
        st.markdown(f"""
        <div class="step-box">
            <div class="{circle}">
                {symbol}
            </div>
            <div class="step-title">
                {titles[i-1]}
            </div>
        </div>
        """, unsafe_allow_html=True)
st.progress(current_step / 4)
