import pymysql
 
connection = pymysql.connect(

    host="127.0.0.1",

    user="root",

    password="Sbi@2001",

    database="student_management"

)
 
print("✅ Database Connected Successfully!")
 