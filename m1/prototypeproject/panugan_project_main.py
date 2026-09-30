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

        productList = sorted(
            data["Product"].unique().tolist()
        )

    else:

        data = pd.DataFrame(
            columns=["Product", "Date", "Amount"]
        )

        productList = []

    productChoice = st.selectbox(
        "Select Product",
        productList + ["Create New Product"]
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

        st.subheader(f"{productName} Records")

        filteredData = data[
            data["Product"] == productName
        ]

        if not filteredData.empty:

            st.dataframe(
                filteredData,
                use_container_width=True
            )

        else:

            st.info(
                "No records found for this product."
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

        # ADD SALE
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

        # UPDATE SALE
        elif option == "Update Sale":

            st.subheader("Update Sale")

            if not filteredData.empty:

                selectedDate = st.selectbox(
                    "Select Record",
                    filteredData["Date"].tolist(),
                    key="update_record"
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
                    "No records available to update."
                )

        # DELETE SALE
        elif option == "Delete Sale":

            st.subheader("Delete Sale")

            if not filteredData.empty:

                selectedDate = st.selectbox(
                    "Select Record To Delete",
                    filteredData["Date"].tolist(),
                    key="delete_record"
                )

                if st.button("Delete"):

                    product.deleteSale(
                        selectedDate
                    )

                    st.success("Sale Deleted")

                    st.rerun()

            else:

                st.warning(
                    "No records available to delete."
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