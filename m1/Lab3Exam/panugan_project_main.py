import streamlit as st
import pandas as pd
import os

from panugan_project_product import Tool
from panugan_project_data import FileManager


fileManager = FileManager()
wrench = Tool("Wrench", fileManager)

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
    st.subheader("Current Sales Records")

    FILE_PATH = os.path.join(os.path.dirname(__file__),"sales_records.txt")

    if os.path.exists(FILE_PATH):
        data = pd.read_csv(FILE_PATH,names=["Product", "Date", "Amount"])
        st.dataframe(data)

    else:
        st.warning("sales_records.txt does not exist.")

    option = st.radio("Select Action",["Add Sale", "Update Sale", "Delete Sale"],key="sales_action")

    if option == "Add Sale":
        st.subheader("Add Sale")
        date = st.text_input("Date", key="add_date")
        amount = st.number_input(
            "Amount Sold",
            min_value=0,
            key="add_amount"
        )

        if st.button("Add", key="add_btn"):
            wrench.addSale()
            st.success("Sale Added")

    elif option == "Update Sale":
        st.subheader("Update Sale")
        date = st.text_input("Date", key="update_date")
        amount = st.number_input(
            "New Amount",
            min_value=0,
            key="update_amount"
        )

        if st.button("Update", key="update_btn"):
            wrench.updateSale()
            st.success("Sale Updated")

    elif option == "Delete Sale":
        st.subheader("Delete Sale")
        date = st.text_input("Date", key="delete_date")

        if st.button("Delete", key="delete_btn"):
            wrench.deleteSale()
            st.success("Sale Deleted")


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

    if st.button("Generate Graph", key="graph_btn"):
        st.info(
            f"Showing performance from {startDate} to {endDate}"
        )
        st.write("imagine a graph")


elif button == "Exit":
    st.success("Thank you for using She Sells - See Sales")