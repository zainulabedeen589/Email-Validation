# streamlit_app.py

import streamlit as st
from st_social_media_links import SocialMediaIcons
from Email_Validation import validate_email


# Streamlit frontend
st.set_page_config(page_title="Email Validator", page_icon="📧")

st.markdown(
    """
    <h2 style='text-align: center; color: #4A90E2;'>📧 Email Verification App </h2>
    <hr style="border:1px solid #4A90E2">
    """,
    unsafe_allow_html=True
)

st.title("Zainul Abedeen")



links = [

    "https://github.com/zainulabedeen589",
    "https://www.linkedin.com/in/zainulabedeen589"
]

icons = SocialMediaIcons(links)
icons.render()  # Renders on main page
icons.render(sidebar=True)  # Also renders in sidebar


email = st.text_input("Enter your email:", placeholder="example@domain.com")

if st.button("Verify"):
    if email:
        result = validate_email(email)
        if "Valid" in result:
            st.success(result)
        else:
            # st.error(result)
            st.error("❌ In-Valid.")
            st.warning("Please enter a valid email address.")
            
    else:
        st.warning("Please enter an email address.")
