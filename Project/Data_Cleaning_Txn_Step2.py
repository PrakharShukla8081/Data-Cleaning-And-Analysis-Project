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

print("Connection Created")



# Set Column For Test

engine.execute('''UPDATE `Txn_Fixed_Table` SET Test_StoreCode=StoreCode,Test_TxnDate=TxnDate,
                      Test_Mobile=Mobile
				       ''')
print('columns set successfully for test')



 #   clean StoreCode  with leading and trailing spaces

engine.execute('''UPDATE Txn_Fixed_Table
                              SET Test_StoreCode = TRIM(Test_StoreCode)
                              WHERE Test_StoreCode IS NOT NULL AND Test_StoreCode != '';''')
print('done successfully....(clean StoreCode leading and trailing spaces)')

# Clean Mobile Number

# clean number  with leading and trailing spaces

engine.execute('''UPDATE Txn_Fixed_Table
                      SET Test_Mobile = TRIM(Test_Mobile)
                      WHERE Test_Mobile IS NOT NULL AND Test_Mobile != '';''')
print('done successfully....(clean numbers start or ends with space)')

# Clean Numbers Having In Between space
engine.execute('''UPDATE Txn_Fixed_Table
                          SET Test_Mobile = REPLACE(Test_Mobile, ' ', '')
                          WHERE Test_Mobile IS NOT NULL AND Test_Mobile != '';''')
print('done successfully....(Cleaned Numbers Having Inbetween space)')

# clean numbers start with 0

engine.execute("""UPDATE `Txn_Fixed_Table` SET Test_Mobile=SUBSTRING(Test_Mobile,2)
                      WHERE Test_Mobile LIKE '%%0%%' AND Test_Mobile !='' AND LENGTH(TRIM(Test_Mobile))=11;""")
print(' done successfully....(clean numbers start with 0) ')

# clean numbers start with 00

engine.execute('''UPDATE `Txn_Fixed_Table` SET Test_Mobile=SUBSTRING(Test_Mobile,3)
                      WHERE Test_Mobile LIKE '%%00%%' AND Test_Mobile !='' AND LENGTH(TRIM(Test_Mobile))=12;''')

print(' done successfully....(clean numbers start with 00) ')

# clean numbers start with 91
engine.execute('''UPDATE Txn_Fixed_Table SET Test_Mobile=SUBSTRING(Test_Mobile,3)
                      WHERE Test_Mobile LIKE '%%91%%' AND Test_Mobile !='' AND LENGTH(TRIM(Test_Mobile))=12;''')

print(' done successfully....(clean numbers start with 91) ')

# clean numbers start with 91
engine.execute('''UPDATE Txn_Fixed_Table SET Test_Mobile=SUBSTRING(Test_Mobile,3)
                      WHERE Test_Mobile LIKE '%%91%%' AND Test_Mobile !='' AND LENGTH(TRIM(Test_Mobile))=12;''')

print(' done successfully....(clean numbers start with 91) ')

# clean numbers start with +91


engine.execute('''UPDATE Txn_Fixed_Table SET Test_Mobile=SUBSTRING(Test_Mobile,4)
                      WHERE Test_Mobile LIKE '%%+91%%' AND Test_Mobile !='' AND LENGTH(TRIM(Test_Mobile))=13;''')

print(' done successfully....(clean numbers start with +91) ')

# clean numbers start with (-)
engine.execute('''UPDATE Txn_Fixed_Table
                      SET Test_Mobile =SUBSTRING(Test_Mobile,2)
                    WHERE Test_Mobile LIKE '%%-%%' AND Test_Mobile !='';''')

print(' done successfully....(clean numbers start with (-)) ')

# check the number format

engine.execute(r"""UPDATE Txn_Fixed_Table SET`Test_Mobile` =NULL,
    Reason=if(Reason is null, 'Invalid Mobile', concat(Reason,',','Invalid Mobile'))
                       WHERE  TRIM(`Test_Mobile`) NOT REGEXP '^[6-9][0-9]{9}$' AND `Test_Mobile` !='';""")

print('done successfully....(check the number format)')




# Change Date Format
engine.execute('''UPDATE Txn_Fixed_Table
                       SET Test_TxnDate=DATE_FORMAT(DATE(STR_TO_DATE(Test_TxnDate,'%%d-%%m-%%Y')),'%%Y-%%m-%%d')''')
print('Date Format Changed')







