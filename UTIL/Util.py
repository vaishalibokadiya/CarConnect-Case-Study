import mysql.connector as sql
import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/CarConnect/EXCEPTION')

from DatabaseException import DatabaseConnectionException

import os
from dotenv import load_dotenv

load_dotenv()

# Class for connecting to the database
class DBPropertyUtil:
    @staticmethod
    def get_connection_string():
        try:
            host=os.getenv("HOST")
            user=os.getenv("USER")
            password=os.getenv("PASSWORD")
            database=os.getenv("DATABASE")

            mydb = sql.connect(host=host,user=user,password=password,database=database)
        except DatabaseConnectionException as e:
            print(e.message)
        else:
            # print('Successfully connected to the database.')
            return mydb
    

# Class for getting cursor
class DBConnUtil:
    @staticmethod
    # takes mydb and returns the cursor and mydb
    def get_connection_object(mydb):
        try:
            mycursor = mydb.cursor()
            
        except:
            print("Error in getting cursor object")
        else:
            # print("Cursor created successfully")
            return mycursor, mydb