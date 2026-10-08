import streamlit as st
import os



def loginScreen():

    leftCol, rightCol = st.columns([3, 2])

    with leftCol:



        logoPath = os.path.join(
            os.path.dirname(__file__),
            "assets",
            "logo.png"
        )

        st.markdown(
            "<div style='height:100px'></div>",
            unsafe_allow_html=True
        )

        st.image(
            logoPath,
            width=700
        )

    with rightCol:

        st.subheader("Login")

        username = st.text_input(
            "Username",
            key="login_username"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        loginButton = st.button(
            "Login",
            use_container_width=True
        )

        st.markdown("---")

        if st.button(
            "Create Account",
            use_container_width=True
        ):

            st.session_state.auth_page = "Sign Up"

            st.rerun()

    return (
        username,
        password,
        loginButton
    )


def signupScreen():

    leftCol, rightCol = st.columns([3, 2])

    with leftCol:


        logoPath = os.path.join(
            os.path.dirname(__file__),
            "assets",
            "logo.png"
        )

        st.markdown(
            "<div style='height:100px'></div>",
            unsafe_allow_html=True
        )

        st.image(
            logoPath,
            width=700
        )

    with rightCol:

        st.subheader("Create Account")

        username = st.text_input(
            "Username",
            key="signup_username"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="signup_password"
        )

        confirmPassword = st.text_input(
            "Confirm Password",
            type="password",
            key="signup_confirm"
        )

        signupButton = st.button(
            "Create Account",
            use_container_width=True
        )

        if st.button(
            "Back to Login",
            use_container_width=True
        ):

            st.session_state.auth_page = "Login"

            st.rerun()

    return (
        username,
        password,
        confirmPassword,
        signupButton
    )