import streamlit as st


def loginScreen():

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