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

print("Connection Created")

# First query
query1 = ''' SELECT COUNT(*) FROM Mem_Demo_Check; '''
df1 = pd.read_sql_query(query1, engine)

# Second query
query2 = ''' SELECT MIN(test_enrolldate), MAX(test_enrolldate) FROM Mem_Demo_Check; '''
df2 = pd.read_sql_query(query2, engine)

# Third query
query3 = ''' SELECT COUNT(DISTINCT Email) FROM Mem_Demo_Check WHERE Test_Email IS NULL OR Test_Email=''; '''
df3 = pd.read_sql_query(query3, engine)

# Fourth query
query4 = ''' SELECT COUNT(DISTINCT FirstName) FROM Mem_Demo_Check WHERE Test_FirstName NOT REGEXP '^[a-zA-Z. ]+$' AND Test_FirstName!=''; '''
df4 = pd.read_sql_query(query4, engine)

# Fifth query
query5 = ''' SELECT COUNT(DISTINCT Mobile) FROM Mem_Demo_Check WHERE Test_Mobile IS NULL OR Test_Mobile=''; '''
df5 = pd.read_sql_query(query5, engine)

# Sixth query
query6 = ''' SELECT COUNT(*) AS total_duplicates FROM (SELECT test_mobile FROM Mem_Demo_Check GROUP BY test_mobile HAVING COUNT(*) > 1) AS duplicates; '''
df6 = pd.read_sql_query(query6, engine)

# Combine results into a single DataFrame
output = pd.DataFrame({
    'Total_Records': df1.iloc[0, 0],
    'Min_Enroll_Date': df2.iloc[0, 0],
    'Max_Enroll_Date': df2.iloc[0, 1],
    'Invalid_Email': df3.iloc[0, 0],
    'Invalid_FirstName': df4.iloc[0, 0],
    'Invalid_Mobile': df5.iloc[0, 0],
    'Total_Duplicates(Mobile)': df6.iloc[0, 0],
}, index=[0])

# # Save the combined DataFrame to a single CSV file
# output.to_csv('Summary.csv', index=False)
# print("Data saved to 'output_combined_demoMad.csv'")




# # Save the DataFrame to a CSV file in the D drive
output.to_csv(r'/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report/Report/summary.csv', index=False)
print("Data saved to '/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report/Report/summary.csv'")


# -------------------------------------------------------------------------------------------------------------------------------



query7 = (
    "SELECT Mobile,test_mobile,COUNT(test_mobile) FROM `Mem_Demo_Check` GROUP BY test_mobile HAVING COUNT(test_mobile) >1 ")

# Execute the query and load the data into a DataFrame
df = pd.read_sql_query(query7, engine)
print("Query executed successfully")

# Display the DataFrame in the console
print("Query output7:")
print(df)

# # Save the DataFrame to a CSV file
# df.to_csv('output_file1.csv', index=False)
# print("Data saved to 'output_file.csv'")


# Save the DataFrame to a CSV file in the D drive
df.to_csv(r'/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report/Report/output_file1.csv', index=False)

print("Data saved to '/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_ReportReport/output_file1.csv'")




query8 = '''
SELECT YEAR(test_enrolldate),
MONTH(test_enrolldate),COUNT(test_mobile) FROM `Mem_Demo_Check`
GROUP BY YEAR(test_enrolldate),MONTH(test_enrolldate)
ORDER BY YEAR(test_enrolldate),MONTH(test_enrolldate);'''

# Execute the query and load the data into a DataFrame
df = pd.read_sql_query(query8, engine)
print("Query executed successfully")

# Display the DataFrame in the console
print("Query output8:")
print(df)
# Save the DataFrame to a CSV file
# df.to_csv('output_file2.csv', index=False)
# print("Data saved to 'output_file.csv'")


# Save the DataFrame to a CSV file in the D drive
df.to_csv(r'/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report/Report/output_file2.csv', index=False)

print("Data saved to '/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report/Report/output_file2.csv'")



#  DISTINCT Store Code= Null

query9 = '''SELECT DISTINCT storecode FROM `Mem_Demo_Check` WHERE storecode IS NULL OR storecode='';'''

# Execute the query and load the data into a DataFrame
df = pd.read_sql_query(query9, engine)
print("Query executed successfully")

# Display the DataFrame in the console
print("Query output9:")
print(" Print Null  Store Code ")
print(df)
# # Save the DataFrame to a CSV file
# df.to_csv('output_file3.csv', index=False)
# print("Data saved to 'output_file.csv'")
#

# Save the DataFrame to a CSV file in the D drive
df.to_csv(r'/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report/Report/output_file3.csv', index=False)

print("Data saved to '/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report/Report/output_file3.csv'")



query10 = '''
select distinct(Email) from Mem_Demo_Check
where Test_Email IS NULL OR Test_Email='';'''


# Execute the query and load the data into a DataFrame
df = pd.read_sql_query(query10, engine)
print("Query executed successfully")

# Display the DataFrame in the console
print("Query output10:")
print(" Print Null Email")
print(df)

# # Save the DataFrame to a CSV file
# df.to_csv('output_file4.csv', index=False)
# print("Data saved to 'output_file.csv'")


# Save the DataFrame to a CSV file in the D drive
df.to_csv(r'/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report/Report/output_file4.csv', index=False)

print("Data saved to '/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report/Report/output_file4.csv'")





query11=(''' select Distinct(Mobile) from Mem_Demo_Check
where Test_Mobile IS NULL OR Test_Mobile='';''')


# Execute the query and load the data into a DataFrame
df = pd.read_sql_query(query11, engine)
print("Query executed successfully")

# Display the DataFrame in the console
print("Query output11:")
print("Print Invalid Mobile")
print(df)

# # Save the DataFrame to a CSV file
# df.to_csv('output_file5.csv', index=False)
# print("Data saved to 'output_file.csv'")


# Save the DataFrame to a CSV file in the D drive
df.to_csv(r'/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report/Report/output_file5.csv', index=False)

print("Data saved to '/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report/Report/output_file5.csv'")



query12=(''' SELECT DISTINCT FirstName  FROM `Mem_Demo_Check`
    WHERE Test_FirstName NOT REGEXP '^[a-zA-Z. ]+$' AND Test_FirstName!='';
''')


# Execute the query and load the data into a DataFrame
df = pd.read_sql_query(query12, engine)
print("Query executed successfully")

# Display the DataFrame in the console
print("Query output12:")
print("Invalid First name")
print(df)

# # Save the DataFrame to a CSV file
# df.to_csv('output_file6.csv', index=False)
# print("Data saved to 'output_file.csv'")


# Save the DataFrame to a CSV file in the D drive
df.to_csv(r'/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report/Report/output_file6.csv', index=False)

print("Data saved to '/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report/Report/output_file6.csv'")



query13=('''select Mobile,EnrollDate from Mem_Demo_Check
where Test_EnrollDate IS NULL  OR Test_EnrollDate='';
''')


# Execute the query and load the data into a DataFrame
df = pd.read_sql_query(query13, engine)
print("Query executed successfully")

# Display the DataFrame in the console
print("Query output13:")
print("Print EnrollDate is null")
print(df)

# # Save the DataFrame to a CSV file
# df.to_csv('output_file7.csv', index=False)
# print("Data saved to 'output_file.csv'")


# Save the DataFrame to a CSV file in the D drive
df.to_csv(r'/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report/Report/output_file7.csv', index=False)

print("Data saved to '/home/intern_dataengg2@corp.easyrewardz.com/Desktop/DQR_Report/Report/output_file7.csv'")
