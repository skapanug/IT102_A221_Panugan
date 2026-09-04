import streamlit as st

import panugan_bank_auth
import panugan_bank_storage
import panugan_bank_transactions
import panugan_bank_analysis
import panugan_bank_utils

st.markdown("""
<style>
.stButton button {
    background-color: #003366;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="panugan Bank",
    page_icon="🏦",
    layout="wide"
)
st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #0f2e1d;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #143d27;
}

/* Headers */
h1, h2, h3 {
    color: #d4f5dd;
}

/* Normal text */
p, label, div {
    color: #ffffff;
}

/* Buttons */
.stButton > button {
    background-color: #1f6b3b;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #2d8a50;
}

/* Metric cards */
[data-testid="stMetric"] {
    background-color: #1a4d31;
    padding: 15px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# SESSION STATE
# ==========================================

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False


if "account" not in st.session_state:

    st.session_state.account = None


# ==========================================
# BANK HEADER
# ==========================================

st.title("Panugan BANK")

st.caption(
    "Secure Digital Banking System"
)


# ==========================================
# LOGIN / REGISTRATION
# ==========================================

if not st.session_state.logged_in:

    login_tab, register_tab = st.tabs(
        [
            "Login",
            "Register"
        ]
    )


    # ======================================
    # LOGIN
    # ======================================

    with login_tab:

        st.subheader(
            "Welcome Back"
        )

        account_number = st.text_input(
            "Account Number",
            key="login_account"
        )

        pin = st.text_input(
            "PIN",
            type="password",
            key="login_pin"
        )

        if st.button(
            "Login",
            use_container_width=True
        ):

            account, message = (
                panugan_bank_auth
                .login_account(
                    account_number,
                    pin
                )
            )

            if account is not None:

                st.session_state.logged_in = True

                st.session_state.account = (
                    account
                )

                st.success(message)

                st.rerun()

            else:

                st.error(message)


    # ======================================
    # REGISTRATION
    # ======================================

    with register_tab:

        st.subheader(
            "Create Your Panugan Bank Account"
        )

        name = st.text_input(
            "Full Name",
            key="register_name"
        )

        account_number = st.text_input(
            "Account Number",
            key="register_account"
        )

        pin = st.text_input(
            "Create 4-Digit PIN",
            type="password",
            key="register_pin"
        )

        confirm_pin = st.text_input(
            "Confirm PIN",
            type="password",
            key="register_confirm_pin"
        )

        account_type = st.selectbox(
            "Account Type",
            [
                "Savings Account",
                "Student Account"
            ]
        )

        starting_balance = st.number_input(
            "Starting Balance",
            min_value=0.0,
            step=100.0,
            format="%.2f"
        )

        if st.button(
            "Create Account",
            use_container_width=True
        ):

            account, message = (
                panugan_bank_auth
                .register_account(
                    name,
                    account_number,
                    pin,
                    confirm_pin,
                    account_type,
                    starting_balance
                )
            )

            if account is not None:

                st.success(message)

                st.info(
                    "Your account has been created. "
                    "Please use the Login tab."
                )

            else:

                st.error(message)


# ==========================================
# LOGGED-IN BANKING APPLICATION
# ==========================================

else:

    account = (
        st.session_state.account
    )


    # ======================================
    # SIDEBAR
    # ======================================

    st.sidebar.title(
        "Services"
    )

    st.sidebar.write(
        f"**{account.account_name}**"
    )

    st.sidebar.caption(
        account.get_account_type()
    )

    st.sidebar.write(
        f"Account: "
        f"{account.account_number}"
    )

    st.sidebar.divider()


    menu = st.sidebar.radio(
        "BANKING MENU",
        [
            "🏠 Dashboard",
            "💰 Deposit",
            "💸 Withdraw",
            "📄 Transaction History",
            "📊 Transaction Analysis"
        ]
    )


    st.sidebar.divider()


    if st.sidebar.button(
        "Logout",
        use_container_width=True
    ):

        st.session_state.logged_in = False

        st.session_state.account = None

        st.rerun()


    # ======================================
    # DASHBOARD
    # ======================================

    if menu == "🏠 Dashboard":

        st.header(
            f"Welcome, {account.account_name}"
        )

        st.subheader(
            "Account Overview"
        )

        col1, col2, col3 = st.columns(3)


        col1.metric(
            "Current Balance",
            panugan_bank_utils
            .format_currency(
                account.check_balance()
            )
        )


        col2.metric(
            "Account Type",
            account.get_account_type()
        )


        col3.metric(
            "Account Number",
            account.account_number
        )
        st.divider()

        col4, col5 = st.columns(2)

        transactions = (
            panugan_bank_transactions
            .get_transactions()
        )

        user_transactions = [
            t for t in transactions
            if t.get("account_number")
            == account.account_number
        ]

        col4.metric(
            "Total Transactions",
            len(user_transactions)
        )

        col5.metric(
            "Status",
            "Active"
        )

        st.divider()


        st.info(
            "Select a banking service from "
            "the menu on the left."
        )


    # ======================================
    # DEPOSIT
    # ======================================

    elif menu == "💰 Deposit":

        st.header(
            "Deposit Money"
        )

        st.write(
            f"Current Balance: "
            f"**{panugan_bank_utils.format_currency(account.check_balance())}**"
        )

        amount = st.number_input(
            "Deposit Amount",
            min_value=0.0,
            step=100.0,
            format="%.2f"
        )


        if st.button(
            "Confirm Deposit",
            use_container_width=True
        ):

            if not panugan_bank_utils.is_valid_amount(
                amount
            ):

                st.error(
                    "Invalid deposit amount."
                )

            else:

                success = account.deposit(
                    amount
                )

                if success:

                    panugan_bank_storage.update_account(
                        account
                    )

                    panugan_bank_transactions.record_transaction(
                        account,
                        "Deposit",
                        amount
                    )

                    st.success(
                        "Deposit successful."
                    )

                    st.metric(
                        "New Balance",
                        panugan_bank_utils
                        .format_currency(
                            account.check_balance()
                        )
                    )


    # ======================================
    # WITHDRAW
    # ======================================

    elif menu == "💸 Withdraw":

        st.header(
            "Withdraw Money"
        )

        st.write(
            f"Available Balance: "
            f"**{panugan_bank_utils.format_currency(account.check_balance())}**"
        )

        amount = st.number_input(
            "Withdrawal Amount",
            min_value=0.0,
            step=100.0,
            format="%.2f"
        )


        if st.button(
            "Confirm Withdrawal",
            use_container_width=True
        ):

            if not panugan_bank_utils.is_valid_amount(
                amount
            ):

                st.error(
                    "Invalid withdrawal amount."
                )

            elif amount > account.check_balance():

                st.error(
                    "Insufficient balance."
                )

            else:

                success = account.withdraw(
                    amount
                )

                if success:

                    panugan_bank_storage.update_account(
                        account
                    )

                    panugan_bank_transactions.record_transaction(
                        account,
                        "Withdraw",
                        amount
                    )

                    st.success(
                        "Withdrawal successful."
                    )

                    st.metric(
                        "New Balance",
                        panugan_bank_utils
                        .format_currency(
                            account.check_balance()
                        )
                    )


    # ======================================
    # TRANSACTION HISTORY
    # ======================================

    elif menu == "📄 Transaction History":

        st.header(
            "Transaction History"
        )

        transactions = (
            panugan_bank_transactions
            .get_transactions()
        )


        # Show only transactions
        # belonging to the logged-in user.

        transactions = [
            transaction
            for transaction in transactions
            if transaction.get(
                "account_number"
            ) == account.account_number
        ]


        if transactions:

            display_data = []

            for transaction in transactions:

                display_data.append({

                    "Timestamp":
                        transaction.get(
                            "timestamp",
                            "N/A"
                        ),

                    "Transaction":
                        transaction.get(
                            "transaction",
                            "N/A"
                        ),

                    "Amount":
                        panugan_bank_utils
                        .format_currency(
                            transaction.get(
                                "amount",
                                0
                            )
                        ),

                    "Balance After":
                        panugan_bank_utils
                        .format_currency(
                            transaction.get(
                                "balance_after",
                                0
                            )
                        )
                })


            st.dataframe(
                display_data,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info(
                "No transaction history available."
            )


    # ======================================
    # TRANSACTION ANALYSIS
    # ======================================

    elif menu == "📊 Transaction Analysis":

        st.header(
            "Transaction Analysis"
        )

        result = (
            panugan_bank_analysis
            .analyze_transactions(
                account.account_number
            )
        )
        import pandas as pd

        chart_data = pd.DataFrame(
            {
                "Count": [
                    result["deposits"],
                    result["withdrawals"]
                ]
            },
            index=[
                "Deposits",
                "Withdrawals"
            ]
        )

        st.subheader(
            "Transaction Overview"
        )

        st.bar_chart(chart_data)

        # ==================================
        # ANALYSIS 1
        # TRANSACTION SUMMARY
        # ==================================

        st.subheader(
            "1. Transaction Summary"
        )

        col1, col2, col3 = st.columns(3)


        col1.metric(
            "Total Transactions",
            result[
                "total_transactions"
            ]
        )


        col2.metric(
            "Deposits",
            result[
                "deposits"
            ]
        )


        col3.metric(
            "Withdrawals",
            result[
                "withdrawals"
            ]
        )


        st.divider()


        # ==================================
        # ANALYSIS 2
        # MONEY FLOW
        # ==================================

        st.subheader(
            "2. Money Flow Analysis"
        )

        col1, col2, col3 = st.columns(3)


        col1.metric(
            "Total Deposited",
            panugan_bank_utils
            .format_currency(
                result[
                    "total_deposited"
                ]
            )
        )


        col2.metric(
            "Total Withdrawn",
            panugan_bank_utils
            .format_currency(
                result[
                    "total_withdrawn"
                ]
            )
        )


        col3.metric(
            "Net Cash Flow",
            panugan_bank_utils
            .format_currency(
                result[
                    "net_cash_flow"
                ]
            )
        )


        st.divider()


        # ==================================
        # ANALYSIS 3
        # ACCOUNT ACTIVITY
        # ==================================

        st.subheader(
            "3. Account Activity Analysis"
        )

        col1, col2, col3 = st.columns(3)


        col1.metric(
            "Largest Transaction",
            panugan_bank_utils
            .format_currency(
                result[
                    "largest_transaction"
                ]
            )
        )


        col2.metric(
            "Average Transaction",
            panugan_bank_utils
            .format_currency(
                result[
                    "average_transaction"
                ]
            )
        )


        col3.metric(
            "Latest Transaction",
            result[
                "latest_transaction"
            ]
        )


        st.caption(
            f"Latest Activity: "
            f"{result['latest_timestamp']}"
        )

""" 
######### Learning Signature ######### 
Programmed by: Sean Panugan
Date Submitted: September 4, 2026
 
Program Description: This program stores the account users listings.
Reflection: I learned to make sure codes aren't dupilcated if possible,
 and at best be changed in a reusable format, hence the write account function.
AI Usage
[ ] No AI Assistance – Completed independently without AI.
[/ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""