## libraries 
from sqlalchemy import create_engine, text
from pymongo import MongoClient
import pandas as pd 
import dotenv
import os 

dotenv.load_dotenv()

MYSQL_CONFIG = {
    'username': os.environ['mysql_username'],
    'password': os.environ['mysql_password'],
    'host'    : os.environ['mysql_hostname'],
}

MONGO_DB_CONFIG = {
    'username': os.environ['mongo_username'],
    'password': os.environ['mongo_password'],
    'hostname' : os.environ['mongo_hostname'],
    'appName' : os.environ['mongo_appName'],
    'port'    : os.environ['mongo_port']
}

DB_NAME = 'project_test'

def check_folder(fname = 'analysis_data'):
    if fname not in os.listdir():
        print(f"Download the analysis_data folder from here : {https://drive.google.com/drive/folders/1BrAQD46z9uVs4QXoTM3cGTnPyffiumoT?usp=drive_link}")
        exit()

def reset_sqlite_database(engine, dbname : str):
    with engine.connect() as connection:
        connection.execute(text(f"DROP DATABASE IF EXISTS {dbname}"))
        connection.execute(text(f"CREATE DATABASE {dbname}"))
    print(f'Recreated the database : [{dbname}]')

def main():

    data_folder = 'analysis_data'
    transaction_filename = os.path.join(data_folder, 'transactions_data.csv')
    cards_filename = os.path.join(data_folder, 'cards_data.csv')
    users_filename = os.path.join(data_folder, 'users_data.csv')

    transaction_df = pd.read_csv(transaction_filename)
    cards_df = pd.read_csv(cards_filename)
    users_df = pd.read_csv(users_filename)

    db_url = f"mysql+mysqlconnector://{MYSQL_CONFIG['username']}:{MYSQL_CONFIG['password']}@{MYSQL_CONFIG['host']}:3306"
    engine = create_engine(db_url)
    reset_sqlite_database(engine, dbname = DB_NAME)
    db_url = f"mysql+mysqlconnector://{MYSQL_CONFIG['username']}:{MYSQL_CONFIG['password']}@{MYSQL_CONFIG['host']}:3306/{DB_NAME}"
    engine = create_engine(db_url)

    users_df.to_sql('users', con=engine, if_exists='replace', method='multi')
    cards_df.to_sql('cards', con=engine, if_exists='replace', method='multi')
    transaction_df.to_sql('transactions', con=engine, if_exists='replace', method='multi')

    uri = f'mongodb://{MONGO_DB_CONFIG["hostname"]}:{MONGO_DB_CONFIG["port"]}/?directConnection=true&serverSelectionTimeoutMS=2000&appName={MONGO_DB_CONFIG["appName"]}+2.3.3'
    client = MongoClient(uri)
    db = client[DB_NAME]
    users_collection = db['users']
    cards_collection = db['cards']
    transactions_collection = db['transactions']

    users_collection.insert_many(users_df.to_dict(orient='records'), ordered= False)
    cards_collection.insert_many(cards_df.to_dict(orient='records'), ordered= False)
    transactions_collection.insert_many(transaction_df.to_dict(orient='records'), ordered= False)


if __name__ == "__main__":
    check_folder()
    main()