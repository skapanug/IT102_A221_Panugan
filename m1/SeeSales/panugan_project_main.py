import streamlit as st
import pandas as pd
import os
import plotly.graph_objects as go
import matplotlib.pyplot as plt

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)


from panugan_project_product import (
    Tool,
    AverageChangePredictor
)
from panugan_project_data import FileManager
from panugan_project_login import (
    loginScreen,
    signupScreen
)
from auth_controller import AuthController
from sales_controller import SalesController
from prediction_controller import PredictionController


st.set_page_config(
    layout="wide"
)

fileManager = FileManager()
authController = AuthController(
    fileManager
)

predictionController = PredictionController(
    AverageChangePredictor()
)

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

if "user" not in st.session_state:

    st.session_state.user = ""

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&display=swap');

h1,
h2,
h3,
label,
p {
    font-family: Georgia, serif !important;
}

[data-testid="stDataFrame"],
[data-testid="stDataFrame"] *,
.js-plotly-plot,
.js-plotly-plot * {
    font-family: Arial, sans-serif !important;
}

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

/* ALL SELECTBOXES */

[data-testid="stSelectbox"] > div > div {
    background-color: #F7E8E8 !important;
}

[data-testid="stSelectbox"] div {
    color: #8d1021 !important;
}

[data-testid="stSelectbox"] svg {
    color: #8d1021 !important;
}

/* DATE INPUT */

[data-testid="stDateInput"] input {
    color: #8d1021 !important;
    -webkit-text-fill-color: #8d1021 !important;
}

[data-testid="stDateInput"] > div > div {
    background-color: #F7E8E8 !important;
}

/* NUMBER INPUT */

[data-testid="stNumberInput"] input {
    color: #8d1021 !important;
    -webkit-text-fill-color: #8d1021 !important;
}

[data-testid="stNumberInput"] > div > div {
    background-color: #F7E8E8 !important;
}
</style>
""", unsafe_allow_html=True)


if not st.session_state.logged_in:

    page = st.session_state.get(
    "auth_page",
    "Login"
    )   

    if page == "Login":

        (
            username,
            password,
            loginButton
        ) = loginScreen()

        if loginButton:

            if authController.login(
                username,
                password
            ):

                st.session_state.logged_in = True

                st.session_state.user = username

                st.rerun()

            else:

                st.error(
                    "Invalid username or password."
                )

    else:

        (
            username,
            password,
            confirmPassword,
            signupButton
        ) = signupScreen()

        if signupButton:

            if password != confirmPassword:

                st.error(
                    "Passwords do not match."
                )

            else:

                success = authController.register(
                    username,
                    password
                )

                if success:

                    st.success(
                        "Account created."
                    )

                else:

                    st.error(
                        "Username already exists."
                    )

    st.stop()
button = st.sidebar.radio(
    "Navigation",
    ["Sales Records", "Sales Performance"],
    key="nav"
)

st.sidebar.markdown("---")

if st.sidebar.button("Logout"):

    st.session_state.logged_in = False

    st.session_state.user = ""

    st.rerun()



if button == "Sales Records":
    st.header("Sales Records")
    response = (
    fileManager.supabase
    .table("sales_records")
    .select("*")
    .eq(
        "username",
        st.session_state.user
        )
        .execute()
    )

    data = pd.DataFrame(response.data)

    if not data.empty:

            data.rename(
                columns={
                    "product": "Product",
                    "date": "Date",
                    "amount": "Amount"
                },
                inplace=True
            )

            productList = sorted(
                data["Product"].astype(str).unique().tolist()
            )

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
            "Enter Product Name"
        ).strip()

    else:

        productName = productChoice

    if productName:

        product = Tool(
        productName,
        fileManager
        )

        salesController = SalesController(
            product
        )

        st.subheader(f"{productName} Records")

        filteredData = data[
            data["Product"] == productName
        ]

        filteredData = filteredData[
            ["Product", "Date", "Amount"]
        ]

        if not filteredData.empty:

            st.dataframe(
                filteredData,
                use_container_width=True,
                hide_index=True
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
                salesController.addSale(date.strftime("%Y-%m-%d"),amount)
                st.session_state["message"] = (f"{productName} sale added.")
                st.rerun()




    
        elif option == "Update Sale":
            st.subheader("Update Sale")
            if not filteredData.empty:
                selectedDate = st.selectbox("Select Record",filteredData["Date"].tolist(),key="update_record")

                newAmount = st.number_input("New Amount",min_value=0,key="update_amount")






                if st.button("Update"):
                    salesController.updateSale(selectedDate,newAmount)
                    st.session_state["message"] = (f"{productName} record updated.")
                    st.rerun()

            else:
                st.warning("No records available.")






        elif option == "Delete Sale":
            st.subheader("Delete Sale")
            if not filteredData.empty:
                selectedDate = st.selectbox("Select Record To Delete",filteredData["Date"].tolist(),key="delete_record")

                if st.button("Delete"):
                    salesController.deleteSale(selectedDate)
                    st.session_state["message"] = (f"{productName} record deleted.")
                    st.rerun()

            else:
                st.warning("No records available.")






elif button == "Sales Performance":

    st.header("Sales Performance")

    response = (
    fileManager.supabase
    .table("sales_records")
    .select("*")
    .eq(
        "username",
        st.session_state.user
        )
        .execute()
    )

    data = pd.DataFrame(response.data)

    if not data.empty:

        data.rename(
            columns={
                "product": "Product",
                "date": "Date",
                "amount": "Amount"
            },
            inplace=True
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

        if "show_graph" not in st.session_state:

             st.session_state.show_graph = False

        if st.button(
            "Generate Graph",
            key="graph_btn"
        ):

            st.session_state.show_graph = True

        if st.session_state.show_graph:

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

                amounts = chartData["Amount"].tolist()


                predictedAmount = predictionController.generatePrediction(
                    amounts
                )


                lastDate = chartData["Date"].iloc[-1]

                predictedDate = (
                    lastDate +
                    pd.Timedelta(days=1)
                )

                fig = go.Figure()

                fig.add_trace(
                    go.Scatter(
                        x=chartData["DisplayDate"],
                        y=chartData["Amount"],
                        mode="lines+markers",
                        name="Actual Sales",
                        line=dict(
                            color="#66b3ff",
                            width=3
                        )
                    )
                )

                fig.add_trace(
                    go.Scatter(
                        x=[
                            chartData["DisplayDate"].iloc[-1],
                            predictedDate.strftime("%b %d")
                        ],
                        y=[
                            amounts[-1],
                            predictedAmount
                        ],
                        mode="lines+markers",
                        name="Prediction",
                        line=dict(
                            color="rgba(102,179,255,0.5)",
                            width=3,
                            dash="dash"
                        )
                    )
                )

                fig.update_layout(
                    paper_bgcolor="#080d18",
                    plot_bgcolor="#080d18",
                    font_color="white",
                    legend=dict(
                        font=dict(color="white")
                    )
                )

                st.plotly_chart(
                            fig,
                            use_container_width=True
                        )

                graphDates = chartData["DisplayDate"].tolist()

                graphAmounts = chartData["Amount"].tolist()

                graphDates.append(
                    predictedDate.strftime("%b %d")
                )

                predictionAmounts = graphAmounts.copy()

                predictionAmounts.append(
                    predictedAmount
                )

                plt.figure(figsize=(8, 4))

                plt.plot(
                    chartData["DisplayDate"],
                    chartData["Amount"],
                    marker="o",
                    color="blue",
                    label="Actual Sales"
                )

                plt.plot(
                    [
                        chartData["DisplayDate"].iloc[-1],
                        predictedDate.strftime("%b %d")
                    ],
                    [
                        graphAmounts[-1],
                        predictedAmount
                    ],
                    linestyle="--",
                    color="navy",
                    marker="o",
                    label="Prediction"
                )

                plt.legend()

                plt.tight_layout()

                plt.savefig(
                    "sales_graph.png"
                )

                plt.close()

                filteredData = filteredData[
                    ["Product", "Date", "Amount"]
                ]
          
    
                filteredData["Date"] = (
                    filteredData["Date"]
                    .dt.strftime("%Y-%m-%d")
                )
                st.dataframe(
                    filteredData,
                    use_container_width=True,
                    hide_index=True
                )
                

                pdf = SimpleDocTemplate(
                        "sales_report.pdf"
                    )

                styles = getSampleStyleSheet()

                content = []

                content.append(
                    Paragraph(
                        f"{selectedProduct} Sales Report",
                        styles["Heading1"]
                    )
                
                )
                content.append(
                    Image(
                        "sales_graph.png",
                        width=400,
                        height=250
                    )
                )

                content.append(
                    Spacer(1, 12)
                )

                content.append(
                    Paragraph(
                        f"Predicted Next Sale: {predictedAmount:.0f}",
                        styles["BodyText"]
                    )
                )

                content.append(
                    Spacer(1, 12)
                )

                recordsText = "<br/>".join([
                    f'{row["Product"]} | {row["Date"]} | {row["Amount"]}'
                    for _, row in filteredData.iterrows()
                ])

                content.append(
                    Paragraph(
                        recordsText,
                        styles["BodyText"]
                    )
                )

                pdf.build(content)

                with open(
                    "sales_report.pdf",
                    "rb"
                ) as file:

                    pdfBytes = file.read()

                st.download_button(
                    "Download PDF",
                    data=pdfBytes,
                    file_name="sales_report.pdf",
                    mime="application/pdf"
                )
                                
            else:

                st.warning(
                    "No records found for the selected range."
                )

    else:

        st.warning(
            "No records found."
        )

