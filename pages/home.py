import streamlit as st



st.set_page_config(page_title='FIX AT HOME', page_icon=':hammer_and_wrench:', layout='wide')
st.set_page_config(
    page_title="FIX AT HOME",
    layout="wide"
)


# Navbar

col1, col2, col3, col4, col5, col6,col7 = st.columns(
    [5,1,1,1,1,1,1]
)

with col1:
    st.markdown("## 🔨 FIX AT HOME")

with col2:
    st.text("Home")

with col3:
    st.text("Services")
    

with col4:
    st.text("Community")

with col5:
    st.text("Contact")



with col6:
        st.text("About Us")

with col7:
        st.text("Sign Up")

st.divider()

st.markdown("""
<h1 style='text-align:center;'>
Heavy Items? We Fix Them At Home.
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align:center;font-size:20px;'>
Find trusted welders, fabricators and repair experts
near your location.
</p>
""", unsafe_allow_html=True)
col1,col2,col3 = st.columns([2,2,2])

with col2:
    if st.button(
        "🔍 Find Worker",
        use_container_width=True
    ):
         st.switch_page("pages/find_worker.py")

with col2:
    if st.button(
        "🧑‍🏭 Become Worker",
        use_container_width=True
    ):
        st.switch_page("pages/worker_onboarding.py")
st.divider()

st.subheader("Our Services")

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.info("🚪 Wardrobe Repair")

with col2:
    st.info("🔥 Welding")

with col3:
    st.info("🚧 Gate Repair")

with col4:
    st.info("🏠 Fabrication")

st.divider()

st.subheader("Why Choose Us")

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.success("✅ Verified Workers")

with col2:
    st.success("🏠 Doorstep Service")

with col3:
    st.success("⚡ Emergency Support")

with col4:
    st.success("🤖 AI Cost Estimation")


st.divider()


st.subheader("How It Works")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("1️⃣ Upload Problem")

with col2:
    st.info("2️⃣ Get Quotes")

with col3:
    st.info("3️⃣ Worker Visits")

with col4:
    st.info("4️⃣ Repair Completed")


st.divider()

st.subheader("For Workers")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("📸 Showcase Portfolio")

with col2:
    st.success("👥 Join Community")

with col3:
    st.success("💰 Earn More Income")

col1,col2,col3 = st.columns(3)

with col1:
    st.metric(
        "Workers",
        "500+"
    )

with col2:
    st.metric(
        "Jobs Completed",
        "1200+"
    )

with col3:
    st.metric(
        "Rating",
        "4.8 ⭐"
    )
st.divider()

st.subheader("Customer Reviews")

st.info(
    "⭐⭐⭐⭐⭐ Wardrobe repair completed at my home. Very professional service."
)

st.info(
    "⭐⭐⭐⭐⭐ Found a welder within 30 minutes."
)

st.divider()

st.markdown(
    """
    <center>
    🔨 FIX AT HOME <br>
    Connecting Skilled Workers with Customers <br><br>

    Contact Us | Privacy Policy | Terms & Conditions
    </center>
    """,
    unsafe_allow_html=True
)