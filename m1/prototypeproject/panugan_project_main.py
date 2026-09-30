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
        data = pd.read_csv(FILE_PATH,names=["Product", "Date", "Amount"])

        productList = sorted(data["Product"].astype(str).unique().tolist())

    else:

        data = pd.DataFrame(
            columns=["Product", "Date", "Amount"]
        )

        productList = []

    st.subheader("Select Product")

    productChoice = st.selectbox(
        "Product",
        productList + ["➕ Create New Product"],
        key="product_select"
    )

    if productChoice == "➕ Create New Product":

        productName = st.text_input(
            "Enter Product Name",
            key="new_product"
        ).strip()

        if productName:

            st.session_state["selected_product"] = productName

    else:

        productName = productChoice

        st.session_state["selected_product"] = productName
        productName = st.session_state.get(
            "selected_product",
            productName
        )

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

        if "message" in st.session_state:

            st.success(
                st.session_state["message"]
            )

            del st.session_state["message"]

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
            date = st.date_input("Date",key="add_date")

            amount = st.number_input("Amount Sold",min_value=0,key="add_amount")

            if st.button("Add"):
                product.addSale(date.strftime("%Y-%m-%d"),amount)
                st.session_state["message"] = (f"{productName} sale added.")
                st.rerun()




    
        elif option == "Update Sale":
            st.subheader("Update Sale")
            if not filteredData.empty:
                selectedDate = st.selectbox("Select Record",filteredData["Date"].tolist(),key="update_record")

                newAmount = st.number_input("New Amount",min_value=0,key="update_amount")

                if st.button("Update"):
                    product.updateSale(selectedDate,newAmount)
                    st.session_state["message"] = (f"{productName} record updated.")
                    st.rerun()

            else:
                st.warning("No records available.")






        elif option == "Delete Sale":
            st.subheader("Delete Sale")
            if not filteredData.empty:
                selectedDate = st.selectbox("Select Record To Delete",filteredData["Date"].tolist(),key="delete_record")

                if st.button("Delete"):
                    product.deleteSale(selectedDate)
                    st.session_state["message"] = (f"{productName} record deleted.")
                    st.rerun()

            else:
                st.warning("No records available.")





elif button == "Sales Performance":

    st.header("Sales Performance")

    FILE_PATH = os.path.join(
        os.path.dirname(__file__),
        "sales_records.txt"
    )

    if os.path.exists(FILE_PATH):

        data = pd.read_csv(
            FILE_PATH,
            names=["Product", "Date", "Amount"]
        )

        products = sorted(
            data["Product"].unique().tolist()
        )

        selectedProduct = st.selectbox(
            "Select Product",
            products,
            key="graph_product"
        )

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

            filteredData = data[
                data["Product"] == selectedProduct
            ].copy()

            filteredData["Date"] = pd.to_datetime(
                filteredData["Date"]
            )

            filteredData = filteredData[
                (filteredData["Date"] >= pd.to_datetime(startDate))
                &
                (filteredData["Date"] <= pd.to_datetime(endDate))
            ]

            filteredData = filteredData.sort_values(
                by="Date"
            )

            if not filteredData.empty:

                st.subheader(
                    f"{selectedProduct} Sales Trend"
                )

                chartData = filteredData.copy()

                chartData["DisplayDate"] = (
                    chartData["Date"]
                    .dt.strftime("%b %d")
                )

                chartData = chartData.set_index(
                    "DisplayDate"
                )

                st.line_chart(
                    chartData["Amount"]
                )

                st.dataframe(
                    filteredData,
                    use_container_width=True
                )

            else:

                st.warning(
                    "No records found for the selected range."
                )

    else:

        st.warning(
            "sales_records.txt does not exist."
        )

elif button == "Exit":

    st.success(
        "Thank you for using She Sells - See Sales"
    )