import mysql.connector as sql
import sys
sys.path.insert(0,'D:/Vaishali Bokadiya/Python/CarConnect/EXCEPTION')
from DatabaseException import DatabaseConnectionException

# Class for connecting to the database
class DBPropertyUtil:
    @staticmethod
    def get_connection_string():
        try:
            mydb = sql.connect(host='localhost',user='root',password='Vaishali@1234',database='CarConnect')
        except DatabaseConnectionException as e:
            print(e.message)
        else:
            print('Successfully connected to the database.')
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
            print("Cursor created successfully")
            return mycursor, mydb