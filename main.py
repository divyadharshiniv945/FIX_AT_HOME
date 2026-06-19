import streamlit as st
# from PIL import Image

# image = Image.open("logo.png")
# st.image(image, caption="My Image")
# # download_button

# # title 
# st.title("FIX AT HOME")
# #  text
# st.write("welding")
# # header
# st.header("header: welding")
# st.subheader("subheader: welding")
# st.text("text: welding")
# st.markdown("markdown   : welding")
# st.caption("caption: welding")
# st.markdown('[Google](https://www.google.com)')
# # button
# car=st.text_input("Enter your car model")
# button=st.button('check availabilty')
# cartypes=["toyota","honda","ford","bmw","audi"]
# if car in cartypes:
#         st.write("Your car model is available")
#         st.write(f"Your car model is {car}")
# else:
#         st.write("Your car model is not available")


# def app():
#         st.title("Welcome to :violet[FIX AT HOME] 🧑‍🏭🔥")
#         st.subheader("LOGIN:")
#         email=st.text_input("EMAIL ADDRESS:")
#         password=st.text_input("PASSWORD:",type="password")
#         if st.button(":green[LOGIN]"):
#                 st.success("Login successful!")
                


# app()

st.set_page_config(page_title="FIX AT HOME") 
if "role" not in st.session_state:
    st.session_state.role = None

   
st.markdown(
    "<h1 style='text-align:center;'>🔨FIX AT HOME</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;'>Find verified welding fabricators near your location..</p>",
    unsafe_allow_html=True

)

st.markdown(
    "<p style='text-align:center;'>          </p>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;'>           </p>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <h1 style='text-align:front; font-size:26px;'>CHOOSE THE ROLE ?
    </h1>
    """,
    unsafe_allow_html=True
)
# two buttons
col1, col2,col3 = st.columns([2,2,2])
with col1:
    if st.button("Customer"):
        st.session_state.role = "customer"

with col2:
    if st.button("Worker"):
        st.session_state.role = "worker"

if st.session_state.role == "customer":
    # sign up page 

    st.subheader("👤 Customer Portal")

    customer_option = st.radio(
        "Choose an option",
        ["Sign Up", "Sign In"]
    )

    if customer_option == "Sign Up":

        st.subheader("New Customer?")

        customer_name = st.text_input(
            "Name",
            key="customer_name"
        )

        new_customer_email = st.text_input(
            "Email",
            key="new_customer_email"
        )

        new_customer_password = st.text_input(
            "Password",
            type="password",
            key="new_customer_password"
        )

        confirm_new_customer_password = st.text_input(
            "Confirm Password",
            type="password",
            key="confirm_new_customer_password"
        )

        if st.button("Sign Up"):

            if new_customer_password == confirm_new_customer_password:
                st.success("Customer Account Created")
            else:
                st.error("Passwords do not match")

    elif customer_option == "Sign In":

        st.subheader("Customer Login")

        customer_email = st.text_input(
            "Email",
            key="customer_email"
        )

        customer_password = st.text_input(
            "Password",
            type="password",
            key="customer_password"
        )

        if st.button("Login"):
            st.success("Customer Logged In")
        st.divider()

        st.markdown(
        "<p style='text-align:center;'>Or you can sign in with</p>",
        unsafe_allow_html=True
    )

        col1, col2, col3 = st.columns(3)

        with col1:
         st.button(" Sign In with Google  :red[𝙂]")
        with col2:
          st.button(" Sign In with Facebook :blue[ⓕ]")

        with col3:
          st.button(" Sign In with LinkedIn 💼")
    


   


elif  st.session_state.role =="worker":
    st.text("You are a worker. Please proceed to worker sign up/login page.")
    # Add code for worker login page here       

        

