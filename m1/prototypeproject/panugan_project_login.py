import streamlit as st


def loginScreen():

    st.markdown(
        """
        <style>

        .login-container {
            display: flex;
            height: 80vh;
        }

        .left-panel {
            background-color: white;
            flex: 1;
            border-radius: 15px 0px 0px 15px;
        }

        .right-panel {
            background-color: #440000;
            flex: 1;
            padding: 50px;
            border-radius: 0px 15px 15px 0px;
            color: white;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    leftCol, rightCol = st.columns(2)

    with leftCol:

        st.markdown(
            """
            <div style="
                background:white;
                height:600px;
                border-radius:15px;
            ">
            </div>
            """,
            unsafe_allow_html=True
        )

    with rightCol:

        st.header("Login")

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
            "Login"
        )

    return (
        username,
        password,
        loginButton
    )


def signupScreen():

    leftCol, rightCol = st.columns(2)

    with leftCol:

        st.markdown(
            """
            <div style="
                background:white;
                height:600px;
                border-radius:15px;
            ">
            </div>
            """,
            unsafe_allow_html=True
        )

    with rightCol:

        st.header("Sign Up")

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
            "Create Account"
        )

    return (
        username,
        password,
        confirmPassword,
        signupButton
    )