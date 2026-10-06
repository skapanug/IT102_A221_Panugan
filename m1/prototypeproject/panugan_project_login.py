import streamlit as st


def loginScreen():

    leftCol, rightCol = st.columns([3, 2])

    with leftCol:

        st.markdown(
            """
            <div style="
                background-color:white;
                height:700px;
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

        st.caption(
            "Don't have an account? Use Sign Up."
        )

        st.markdown("</div>", unsafe_allow_html=True)

    return (
        username,
        password,
        loginButton
    )


def signupScreen():

    leftCol, rightCol = st.columns([3, 2])

    with leftCol:

        st.markdown(
            """
            <div style="
                background-color:white;
                height:700px;
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

        st.markdown("</div>", unsafe_allow_html=True)

    return (
        username,
        password,
        confirmPassword,
        signupButton
    )