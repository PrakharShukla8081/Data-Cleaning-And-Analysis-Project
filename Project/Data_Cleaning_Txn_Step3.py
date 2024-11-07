





import pandas as pd
import os
from sqlalchemy import create_engine
from urllib.parse import quote
import pymysql

from Pandas_Library.Pandas_1 import query

pymysql.install_as_MySQLdb()

# Database connection parameters
host = '20.107.3.4'
user = 'Prakhar_Intern'
password = quote('P2@4@#aR4Od69')
database = 'dummy'

# Create an SQLAlchemy engine for MySQL
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# - - - - - -


# First query
query1 = ''' SELECT COUNT(*) FROM Txn_Fixed_Table; '''
df1 = pd.read_sql_query(query1, engine)

# Second query
query2 = ''' SELECT MIN(test_txndate), MAX(test_txndate) FROM Txn_Fixed_Table; '''
df2 = pd.read_sql_query(query2, engine)

# Third query
query3 = ''' select count(distinct store) from Txn_Fixed_Table '''
df3 = pd.read_sql_query(query3, engine)

# Fourth query
query4 = ''' select COUNT(DISTINCT billno,test_txndate,test_storecode)AS Bills from Txn_Fixed_Table; '''
df4 = pd.read_sql_query(query4, engine)

# Fifth query
query5 = ''' SELECT COUNT(DISTINCT Mobile) FROM Txn_Fixed_Table WHERE Test_Mobile IS NULL OR Test_Mobile=''; '''
df5 = pd.read_sql_query(query5, engine)

# Sixth query
query6 = ''' SELECT COUNT(*) AS total_duplicates FROM (SELECT test_mobile FROM Txn_Fixed_Table GROUP BY test_mobile HAVING COUNT(*) > 1) AS duplicates; '''
df6 = pd.read_sql_query(query6, engine)



# Seventh query
query7 = ''' select ROUND(SUM(ItemNetAmount))AS Sales from Txn_Fixed_Table;'''
df7 = pd.read_sql_query(query7, engine)



# Combine results into a single DataFrame
output = pd.DataFrame({
    'Total_Records': df1.iloc[0, 0],
    'Min_Enroll_Date': df2.iloc[0, 0],
    'Max_Enroll_Date': df2.iloc[0, 1],
    'Distinct_Stores': df3.iloc[0, 0],
    'Total_Bills': df4.iloc[0, 0],
    'Invalid_Mobile': df5.iloc[0, 0],
    'Total_Duplicates': df6.iloc[0, 0],
    'Total_Sales': df7.iloc[0, 0],
}, index=[0])
#
# 'Total_Records',

#  Total Records
# Earliest Bill Date
# Latest Bill Date
# Distinct Stores
# Total Bills
# Total Sales
# Distinct Invalid Mobiles


#
# Save the combined DataFrame to a single CSV file
output.to_csv('summarydata.csv', index=False)
print("Data saved to 'output_combined_demoMad.csv'")
# -----===


# Save the DataFrame to a CSV file in the D drive
output.to_csv(r'/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report_Txn/SummaryData.csv', index=False)

print("Data saved to '/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report_Txn/SummaryData.csv'")


query8 = ''' SELECT test_txndate,test_storecode, COUNT(DISTINCT test_mobile)AS Customers,
	COUNT(DISTINCT billno,test_txndate,Test_storecode)AS Bills,SUM(itemqty)AS ItemQty,
	ROUND(SUM(ItemNetAmount))AS Sales
	FROM `Txn_Fixed_Table` WHERE test_mobile IS NOT NULL AND test_mobile !='' 
	GROUP BY test_txndate,test_storecode 
	ORDER BY test_txndate,test_storecode;'''
df8 = pd.read_sql_query(query8, engine)

print("Query executed successfully")

# Display the DataFrame in the console
print("Query output8:")
print("Print EnrollDate is null")
print(df8)

# Save the DataFrame to a CSV file
df8.to_csv('output_file8.csv', index=False)
print("Data saved to 'output_file.csv'")



# Save the DataFrame to a CSV file in the D drive
df8.to_csv(r'/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report_Txn/output_file8.csv', index=False)

print("Data saved to '/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report/output_file8.csv'")

#--------------------   --------



query9 = ''' SELECT test_txndate,test_storecode,
	COUNT(DISTINCT billno,test_txndate,test_storecode)AS Bills,SUM(itemqty)AS SKUS,
	ROUND(SUM(ItemNetAmount))AS Sales
	FROM `Txn_Fixed_Table` WHERE test_mobile IS NULL OR test_mobile =''
	GROUP BY test_txndate,test_storecode 
	ORDER BY test_txndate,test_storecode;'''
df9 = pd.read_sql_query(query9, engine)

print("Query executed successfully")

# Display the DataFrame in the console
print("Query output9:")
print("Print EnrollDate is null")
print(df9)

# Save the DataFrame to a CSV file
df9.to_csv('output_file9.csv', index=False)
print("Data saved to 'output_file.csv'")



# Save the DataFrame to a CSV file in the D drive
df9.to_csv(r'/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report_Txn/output_file9.csv', index=False)

print("Data saved to '/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report/output_file9.csv'")


#-------------------------------------------------------------------------------------------


query10 = ''' select distinct store from Txn_Fixed_Table'''
df10 = pd.read_sql_query(query10, engine)

print("Query executed successfully")

# Display the DataFrame in the console
print("Query output10:")
print("Print EnrollDate is null")
print(df10)

# Save the DataFrame to a CSV file
df10.to_csv('output_file10.csv', index=False)
print("Data saved to 'output_file.csv'")



# Save the DataFrame to a CSV file in the D drive
df10.to_csv(r'/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report_Txn/output_file10.csv', index=False)

print("Data saved to '/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report/output_file10.csv'")


#
# -----


query11= ''' 
SELECT DISTINCT Mobile FROM Txn_Fixed_Table WHERE Test_Mobile IS NULL OR Test_Mobile=''; '''
df11 = pd.read_sql_query(query11, engine)

print("Query executed successfully")

# Display the DataFrame in the console
print("Query output11:")
print("Print EnrollDate is null")
print(df11)

# Save the DataFrame to a CSV file
df11.to_csv('output_file11.csv', index=False)
print("Data saved to 'output_file.csv'")



# Save the DataFrame to a CSV file in the D drive
df11.to_csv(r'/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report_Txn/output_file11.csv', index=False)

print("Data saved to '/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report/output_file11.csv'")




query12=  '''  SELECT COUNT(*) AS total_duplicates
FROM (
    SELECT test_mobile
    FROM `Txn_Fixed_Table`
    GROUP BY test_mobile
    HAVING COUNT(*) > 1
) AS duplicates;   '''

df12 = pd.read_sql_query(query12, engine)

print("Query executed successfully")

# Display the DataFrame in the console
print("Query output12:")
print("Print EnrollDate is null")
print(df12)

# Save the DataFrame to a CSV file
df12.to_csv('output_file12.csv', index=False)
print("Data saved to 'output_file.csv'")



# Save the DataFrame to a CSV file in the D drive
df12.to_csv(r'/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report_Txn/output_file12.csv', index=False)

print("Data saved to '/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report/output_file11.csv'")





