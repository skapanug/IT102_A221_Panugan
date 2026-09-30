import streamlit as st
import pandas as pd
import os

from panugan_project_product import Tool
from panugan_project_data import FileManager

fileManager = FileManager()

st.markdown("""
<style>
.stApp {
    background-color: #1a0d0d;
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #2b1111;
}

h1, h2, h3 {
    color: #ff8c00;
}
</style>
""", unsafe_allow_html=True)

st.title("She Sells - See Sales")

button = st.sidebar.radio(
    "Navigation",
    ["Sales Records", "Sales Performance", "Exit"],
    key="nav"
)

if button == "Sales Records":

    st.header("Sales Records")

    FILE_PATH = os.path.join(
        os.path.dirname(__file__),
        "sales_records.txt"
    )

    if os.path.exists(FILE_PATH):

        data = pd.read_csv(
            FILE_PATH,
            names=["Product", "Date", "Amount"]
        )

        st.subheader("Current Sales Records")
        st.dataframe(data)

        existingProducts = sorted(
            data["Product"].unique().tolist()
        )

    else:

        st.subheader("Current Sales Records")
        st.info("No sales records found.")

        existingProducts = []

    productChoice = st.selectbox(
        "Select Product",
        existingProducts + ["Create New Product"]
    )

    if productChoice == "Create New Product":

        productName = st.text_input(
            "Enter Product Name"
        )

    else:

        productName = productChoice

    if productName:

        product = Tool(
            productName,
            fileManager
        )

        option = st.radio(
            "Select Action",
            [
                "Add Sale",
                "Update Sale",
                "Delete Sale"
            ],
            key="sales_action"
        )

        if option == "Add Sale":

            st.subheader("Add Sale")

            date = st.date_input(
                "Date",
                key="add_date"
            )

            amount = st.number_input(
                "Amount Sold",
                min_value=0,
                key="add_amount"
            )

            if st.button("Add"):

                product.addSale(
                    date.strftime("%Y-%m-%d"),
                    amount
                )

                st.success("Sale Added")
                st.rerun()

        elif option == "Update Sale":

            st.subheader("Update Sale")

            if os.path.exists(FILE_PATH):

                productData = data[
                    data["Product"] == productName
                ]

                if not productData.empty:

                    selectedDate = st.selectbox(
                        "Select Record",
                        productData["Date"].tolist()
                    )

                    newAmount = st.number_input(
                        "New Amount",
                        min_value=0,
                        key="update_amount"
                    )

                    if st.button("Update"):

                        product.updateSale(
                            selectedDate,
                            newAmount
                        )

                        st.success("Sale Updated")
                        st.rerun()

                else:

                    st.warning(
                        "No records found for this product."
                    )

        elif option == "Delete Sale":

            st.subheader("Delete Sale")

            if os.path.exists(FILE_PATH):

                productData = data[
                    data["Product"] == productName
                ]

                if not productData.empty:

                    selectedDate = st.selectbox(
                        "Select Record To Delete",
                        productData["Date"].tolist()
                    )

                    if st.button("Delete"):

                        product.deleteSale(
                            selectedDate
                        )

                        st.success("Sale Deleted")
                        st.rerun()

                else:

                    st.warning(
                        "No records found for this product."
                    )

elif button == "Sales Performance":

    st.header("Sales Performance")

    startDate = st.date_input(
        "Start Date",
        key="start_date"
    )

    endDate = st.date_input(
        "End Date",
        key="end_date"
    )

    if st.button(
        "Generate Graph",
        key="graph_btn"
    ):

        st.info(
            f"Showing performance from {startDate} to {endDate}"
        )

        st.write("Imagine a graph here.")

elif button == "Exit":

    st.success(
        "Thank you for using She Sells - See Sales"
    )