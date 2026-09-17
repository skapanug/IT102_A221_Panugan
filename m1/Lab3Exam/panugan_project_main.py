import streamlit as st

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
    color: #ff4d4d;
}
</style>
""", unsafe_allow_html=True)

st.title("She Sells - See Sales")


button = st.sidebar.radio(
    "Navigation",
    [
        "Sales Records",
        "Sales Performance",
        "Exit"
    ]
)


if button == "Sales Records":
    st.subheader("Current Sales Records")
    import os
    BASE_DIR = os.path.dirname(__file__)
    FILE_PATH = os.path.join(BASE_DIR, "sales_records.txt")
    with open(FILE_PATH, "r") as file:
     st.text(file.read())
    try:
        with open("sales_records.txt", "r") as file:
            st.text(file.read())

    except FileNotFoundError:
        st.warning("sales_records.txt does not exist.")

    st.header("Sales Records")
    wrench.loadSalesRecords()
    option = st.radio(
        "Select Action",
        ["Add Sale","Update Sale","Delete Sale","Back"]
    )

 
    if option == "Add Sale":
        st.subheader("Add Sale")
        date = st.text_input("Date")
        amount = st.number_input(
            "Amount Sold",
            min_value=0
        )

        if st.button("Submit Add"):
            wrench.addSale()
            st.success("Sale Added")


    elif option == "Update Sale":
        st.subheader("Update Sale")
        date = st.text_input("Date")
        amount = st.number_input("New Amount",min_value=0)

        if st.button("Submit Update"):
            wrench.updateSale()
            st.success("Sale Updated")

    
    elif option == "Delete Sale":
        st.subheader("Delete Sale")
        date = st.text_input("Date")
        if st.button("Submit Delete"):
            wrench.deleteSale()
            st.success("Sale Deleted")


elif button == "Sales Performance":
    st.header("Sales Performance")
    startDate = st.date_input("Start Date")
    endDate = st.date_input("End Date")

    if st.button("Generate Graph"):
        st.write(f"Performance from {startDate} to {endDate}")
        st.info("Graph Placeholder")


elif button == "Exit":
    st.write("Exiting Goodbye!")