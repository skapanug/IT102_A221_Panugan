import streamlit as st


def loginScreen():

    leftCol, rightCol = st.columns([3, 2])

    with leftCol:

        st.markdown(
            """
            <div style="
                background-color:white;
                height:100vh;
                border-radius:0px;
            ">
            </div>
            """,
            unsafe_allow_html=True
        )

    with rightCol:

        st.markdown(
            """
            <div style="
                background-color:#8d1021;
                padding:30px;
                border-radius:10px;
            ">
            """,
            unsafe_allow_html=True
        )

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

        st.markdown("</div>", unsafe_allow_html=True)

    return (
        username,
        password,
        loginButton
    )


def signupScreen():

    leftCol, rightCol = st.columns([3, 2])

    import os

    with leftCol:

        st.write(
            os.path.exists("assets/logo.png")
        )

        st.image(
            "assets/logo.png",
            width=600
        )

    with rightCol:

        st.markdown(
            """
            <div style="
                background-color:#8d1021;
                padding:30px;
                border-radius:10px;
            ">
            """,
            unsafe_allow_html=True
        )

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

        st.markdown("</div>", unsafe_allow_html=True)

    return (
        username,
        password,
        confirmPassword,
        signupButton
    )