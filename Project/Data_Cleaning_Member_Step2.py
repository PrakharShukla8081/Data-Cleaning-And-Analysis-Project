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

engine.execute('''UPDATE `Mem_Demo_Check` SET  Test_Email =Email,Test_Mobile=Mobile, Test_FirstName=FirstName,Test_LastName=LastName,
                      Test_PinCode=PinCode,Test_Address1=Address1,Test_Address2=Address2,Test_EnrollDate=EnrollDate,Test_DateOfBirth=DateOfBirth,
                      Test_StoreCode=StoreCode
                      ;''')



print('columns set successfully for test')

# Clean Mobile Number

# clean number  with leading and trailing spaces

engine.execute('''UPDATE Mem_Demo_Check
                      SET Test_Mobile = TRIM(Test_Mobile)
                      WHERE Test_Mobile IS NOT NULL AND Test_Mobile != '';''')
print('done successfully....(clean numbers start or ends with space)')

# Clean Numbers Having In Between space
engine.execute('''UPDATE Mem_Demo_Check
                          SET Test_Mobile = REPLACE(Test_Mobile, ' ', '')
                          WHERE Test_Mobile IS NOT NULL AND Test_Mobile != '';''')
print('done successfully....(Cleaned Numbers Having Inbetween space)')

# clean numbers start with 0

engine.execute("""UPDATE `Mem_Demo_Check` SET Test_Mobile=SUBSTRING(Test_Mobile,2)
                      WHERE Test_Mobile LIKE '%%0%%' AND Test_Mobile !='' AND LENGTH(TRIM(Test_Mobile))=11;""")
print(' done successfully....(clean numbers start with 0) ')

# clean numbers start with 00

engine.execute('''UPDATE `Mem_Demo_Check` SET Test_Mobile=SUBSTRING(Test_Mobile,3)
                      WHERE Test_Mobile LIKE '%%00%%' AND Test_Mobile !='' AND LENGTH(TRIM(Test_Mobile))=12;''')

print(' done successfully....(clean numbers start with 00) ')

# clean numbers start with 91
engine.execute('''UPDATE Mem_Demo_Check SET Test_Mobile=SUBSTRING(Test_Mobile,3)
                      WHERE Test_Mobile LIKE '%%91%%' AND Test_Mobile !='' AND LENGTH(TRIM(Test_Mobile))=12;''')

print(' done successfully....(clean numbers start with 91) ')


# clean numbers start with +91


engine.execute('''UPDATE Mem_Demo_Check SET Test_Mobile=SUBSTRING(Test_Mobile,4)
                      WHERE Test_Mobile LIKE '%%+91%%' AND Test_Mobile !='' AND LENGTH(TRIM(Test_Mobile))=13;''')

print(' done successfully....(clean numbers start with +91) ')

# clean numbers start with (-)
engine.execute('''UPDATE Mem_Demo_Check
                      SET Test_Mobile =SUBSTRING(Test_Mobile,2)
                    WHERE Test_Mobile LIKE '%%-%%' AND Test_Mobile !='';''')

print(' done successfully....(clean numbers start with (-)) ')

# check the number format

engine.execute(r"""UPDATE Mem_Demo_Check SET`Test_Mobile` =NULL,
    Reason=if(Reason is null, 'Invalid Mobile', concat(Reason,',','Invalid Mobile'))
                       WHERE  TRIM(`Test_Mobile`) NOT REGEXP '^[6-9][0-9]{9}$' AND `Test_Mobile` !='';""")

print('done successfully....(check the number format)')

# Email Cleaning


engine.execute('''UPDATE Mem_Demo_Check
                      SET Test_Email = TRIM(Email)
                      WHERE Test_Email IS NOT NULL AND Test_Email != '';''')
print('done successfully....(clean Email start or ends with space)')




engine.execute(r"""  UPDATE Mem_Demo_Check     SET Test_Email = NULL,Reason=if(Reason is null, 'Invalid Email', concat(Reason,',','Invalid Email'))
           WHERE NOT Test_Email REGEXP '^[A-Za-z0-9._%%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,63}$'; """)

print('done successfully....(check the Email format)')






# Address Cleaning

engine.execute(r"""UPDATE Mem_Demo_Check SET Test_Address1 = TRIM(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE
(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE
(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(`Test_Address1`, '!', ' '), '”', ' '), '#', ' '), '$', ' '), '%%', ' '), '&', ' '),
 '’', ' '), '(', ' '), ')', ' '), '*', ' '), '+', ' '), ',', ' '), '-', ' '), '.', ' '), '/', ' '), ':', ' '), ';', ' '), '<', ' '),
  '=', ' '), '>', ' '), '?', ' '), '@', ' '), '[', ' '), '\\', ' '), ']', ' '), '^', ' '), '_', ' '), '`', ' '), '{', ' '), '|', ' '),
'}', ' '), '~', ' '));""")

print('done successfully....(cleaned address1)')

engine.execute(r"""UPDATE Mem_Demo_Check SET Test_Address2 = TRIM(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(`Test_Address2`, '!', ' '), '”', ' '), '#', ' '), '$', ' '), '%%', ' '), '&', ' '), '’', ' '), '(', ' '), ')', ' '), '*', ' '), '+', ' '), ',', ' '), '-', ' '), '.', ' '), '/', ' '), ':', ' '), ';', ' '), '<', ' '), '=', ' '), '>', ' '), '?', ' '), '@', ' '), '[', ' '), '\\', ' '), ']', ' '), '^', ' '), '_', ' '), '`', ' '), '{', ' '), '|', ' '),
    '}', ' '), '~', ' '));""")
print('done successfully....(cleaned address2)')


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------


# Name Cleaning

# Removing leading and trailing spaces and replacing single quotes with spaces for FirstName

engine.execute('''UPDATE Mem_Demo_Check SET Test_FirstName=REPLACE(TRIM(FirstName),"'",' ');''')
print(
    "done successfully....(cleaned leading and trailing spaces and replacing single quotes with spaces for FirstName )")

# Removing leading and trailing spaces and replacing single quotes with spaces for LastName

engine.execute('''UPDATE Mem_Demo_Check SET Test_LastName=REPLACE(TRIM(LastName),"'",' ');''')
print(
    'done successfully....(cleaned leading and trailing spaces and replacing single quotes with spaces for LastName )')

# Replacing special characters

engine.execute(
    r"""UPDATE Mem_Demo_Check SET Test_FirstName = TRIM(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(`Test_FirstName`, '!', ' '), '”', ' '), '#', ' '), '$', ' '), '%%', ' '), '&', ' '), '’', ' '), '(', ' '), ')', ' '), '*', ' '), '+', ' '), ',', ' '), '-', ' '), '.', ' '), '/', ' '), ':', ' '), ';', ' '), '<', ' '), '=', ' '), '>', ' '), '?', ' '), '@', ' '), '[', ' '), '\\', ' '), ']', ' '), '^', ' '), '_', ' '), '`', ' '), '{', ' '), '|', ' '),'}', ' '), '~', ' '));""")
print('done successfully....(cleaned replace special character FirstName ')

engine.execute(
    r"""UPDATE Mem_Demo_Check SET Test_LastName = TRIM(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(`Test_LastName`, '!', ' '), '”', ' '), '#', ' '), '$', ' '), '%%', ' '), '&', ' '), '’', ' '), '(', ' '), ')', ' '), '*', ' '), '+', ' '), ',', ' '), '-', ' '), '.', ' '), '/', ' '), ':', ' '), ';', ' '), '<', ' '), '=', ' '), '>', ' '), '?', ' '), '@', ' '), '[', ' '), '\\', ' '), ']', ' '), '^', ' '), '_', ' '), '`', ' '), '{', ' '), '|', ' '),'}', ' '), '~', ' '));""")

print('done successfully....(cleaned replace special character LastName')

#  The first letter is capitalized, and the rest are in Lowercase

engine.execute('''UPDATE Mem_Demo_Check 
                  SET Test_FirstName =CONCAT(UPPER(SUBSTRING(Test_FirstName,1,1)),
                   LOWER(SUBSTRING(Test_FirstName, 2)));''')

print('done successfully....(The first letter is capitalized, '' and the rest are in Lowercase for  FirstName')
print('done successfully....(The first letter is capitalized, and the rest are in Lowercase for  LastName')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
engine.execute('''UPDATE Mem_Demo_Check
                     SET Test_FirstName =CONCAT(UPPER(SUBSTRING(Test_FirstName,1,1)),
                      LOWER(SUBSTRING(Test_FirstName, 2)));''')

print('done successfully....(The first letter is capitalized, '' and the rest are in Lowercase for  FirstName')

engine.execute('''UPDATE Mem_Demo_Check SET Test_PinCode='',Reason=if(Reason is null, 'Invalid PinCode', concat(Reason,',','Invalid PinCode'))
                      WHERE Test_PinCode ='0';''')
print('done successfully....(replace null pincode with blank)')
#
# check pincode format
engine.execute(r"""UPDATE Mem_Demo_Check
                     SET Test_PinCode = REGEXP_REPLACE(Test_PinCode, '[^0-9]', '')
                     WHERE LENGTH(TRIM(Test_PinCode)) >= 6 AND LENGTH(TRIM(Test_PinCode)) <= 10; -- Ensure PIN code length is within a valid range
                    """)
print('done successfully....(check pincode format )')
#
# engine.execute('''UPDATE Mem_Demo_Check
#                       SET Test_EnrollDate=DATE_FORMAT(DATE(STR_TO_DATE(Test_EnrollDate,'%%d-%%m-%%Y')),'%%Y-%%m-%%d');''')
# print('Date Format Changed')
#


engine.execute('''UPDATE Mem_Demo_Check SET Test_DateOfBirth='Null',Reason=if(Reason is null, 'Invalid Birth Date', concat(Reason,',','Invalid Birth Date'))
    WHERE Test_DateOfBirth='0000000' or Test_DateOfBirth='0' ; ''')

print('done successfully....(replace null with blank  for dob)')


#