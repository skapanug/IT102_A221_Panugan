import streamlit as st
from supabase import create_client


class FileManager:

    SUPABASE_URL = "https://avhmcliomusuvvwepock.supabase.co"

    SUPABASE_KEY = "sb_publishable_-3lVyLSfP3ejc6H-3JD8rQ_d1ZNeiM6"

    def __init__(self):

        self.supabase = create_client(
            self.SUPABASE_URL,
            self.SUPABASE_KEY
        )


    def loadRecords(self, productName):

        response = (
            self.supabase
            .table("sales_records")
            .select("*")
            .eq("username", st.session_state.user)
            .eq("product", productName)
            .execute()
        )

        records = []

        for row in response.data:

            records.append([
                row["product"],
                row["date"],
                row["amount"]
            ])

        return records


    def addRecord(self, productName, date, amount):

        self.supabase.table(
            "sales_records"
        ).insert(
            {
                "username": st.session_state.user,
                "product": productName,
                "date": date,
                "amount": amount
            }
        ).execute()


    def updateRecord(self, productName, date, amount):

        self.supabase.table(
            "sales_records"
        ).update(
            {
                "amount": amount
            }
        ).eq(
            "product",
            productName
        ).eq(
            "date",
            date
        ).execute()


    def deleteRecord(self, productName, date):

        self.supabase.table(
            "sales_records"
        ).delete().eq(
            "product",
            productName
        ).eq(
            "date",
            date
        ).execute()
    def registerUser(self, username, password):

        existingUser = (
            self.supabase
            .table("users")
            .select("*")
            .eq("username", username)
            .execute()
        )

        if existingUser.data:

            return False

        self.supabase.table(
            "users"
        ).insert(
            {
                "username": username,
                "password": password
            }
        ).execute()

        return True


    def loginUser(self, username, password):

        user = (
            self.supabase
            .table("users")
            .select("*")
            .eq("username", username)
            .eq("password", password)
            .execute()
        )

        return len(user.data) > 0