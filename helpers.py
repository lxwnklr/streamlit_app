from pymongo.mongo_client import MongoClient
import streamlit as st

def connect_to_mongo():
    # load the user and db password from the secrets.toml file
    user = st.secrets['db_username']
    password = st.secrets['db_password']

    # This is my database connection string, for a cluster called tb-ii
    uri = f"mongodb+srv://{user}:{password}@tb-ii.nri38.mongodb.net/?retryWrites=true&w=majority&appName=tb-ii"

    # Let's connect to our cluster
    client = MongoClient(uri)

    try:
        # print a message to say the
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")

        return client
    except Exception as e:
        # if connection was not made, then you will see an error message in your terminal
        print(e)


def connect_to_collection(db_name, collection_name):
    # connect to cluster
    client = connect_to_mongo()

    db_name = "streamlit"
    collection_name = "test2"

    # connect to the collection
    db = client[db_name]
    collection = db[collection_name]

    return collection

# connect to MongoDB
client = connect_to_mongo()