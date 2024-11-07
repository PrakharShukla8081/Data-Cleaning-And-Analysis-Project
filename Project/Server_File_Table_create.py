import pandas as pd
import os
from sqlalchemy import create_engine
from urllib.parse import quote
import pymysql

pymysql.install_as_MySQLdb()

# Database connection parameters
host = '20.107.3.4'
user = 'Prakhar_Intern'
password = quote('P2@4@#aR4Od69')
database = 'dummy'

# Create an SQLAlchemy engine for MySQL
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
# connection = engine.connect()
# Directory containing CSV or XLSX files

directory = '/home/intern_dataengg2@corp.easyrewardz.com/PycharmProjects/pythonProject/Project/file'

# # Check if the directory exists
if not os.path.isdir(directory):
    raise FileNotFoundError(f"The directory {directory} does not exist.")

# Iterate through files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv") or filename.endswith(".xlsx"):
        file_path = os.path.join(directory, filename)

        # Read CSV or XLSX file based on the extension
        if filename.endswith(".csv"):
            df = pd.read_csv(file_path, encoding='latin1', delimiter=',')  # Specify encoding here
            pd.set_option('display.max_columns', None)  # Show all columns
            pd.set_option('display.max_colwidth', None)  # Show full content of each column
            pd.set_option('display.width', 1000)  # Adjust width to a large value if needed

            print('DataFrame created for CSV format')

            print(df)
        elif filename.endswith(".xlsx"):
            df = pd.read_excel(file_path, engine='openpyxl')
            print('DataFrame created for XLSX format')

        # Insert DataFrame data into MySQL table
        #
        # table_name = 'test_vip_member1'
        # df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
        # print('Data loaded into table successfully')
