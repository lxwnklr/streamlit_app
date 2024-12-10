import streamlit as st
import datetime
import pandas as pd
from helpers import connect_to_collection

def registration_page():
    # create an empty container
    placeholder = st.empty()

    # creating a form to collect information
    with placeholder.form("registration_form"):
        st.subheader("Register user")
        user_name = st.text_input("Enter user name")
        password = st.text_input("Password", type="password")
        repeat_password = st.text_input("Repeat Password", type="password")
        name = st.text_input("Enter your name")
        age = st.number_input("Enter your age", step=1, min_value=18)

        submit_button = st.form_submit_button("Register")

    if submit_button:
        db_name = "streamlit"
        collection_name = "test2"

        #db = client[db_name]
        collection = connect_to_collection(db_name, collection_name)

        # reading data about the users
        user_data = pd.DataFrame(list(collection.find()))
        user_names = list(user_data.username)

        # add some validation
        if len(password) < 1 and len(user_name) < 1:
            st.error("Enter a username and a password", icon="🔥")
        elif password != repeat_password:
            st.error("Passwords do not match", icon="🔥")
        elif user_name in user_names:
            st.error("USER NAME EXISTS", icon="🔥")
        else:
            document = {"username": user_name, "password": password, "name": name, "age": age,
                        "created_at": datetime.datetime.now()}

            collection.insert_one(document)

            placeholder.empty()
            st.image(
                "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDFkbG53bHR2cWN6dzI1NWcxYWVjazRocWNtanlkc2gzanNuaXBvdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tHIRLHtNwxpjIFqPdV/giphy.webp")
