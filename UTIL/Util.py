import mysql.connector as sql

class DBPropertyUtil:
    @staticmethod
    def get_connection_string():
        # host=input("Enter host name: ")
        # user=input("Enter user name: ")
        # password=input("Enter password: ")
        # database=input("Enter database name: ")
        try:
            # mydb = sql.connect(host=host,user=user,password=password,database=database)
            mydb = sql.connect(host='localhost',user='root',password='Vaishali@1234',database='CarConnect')
        except:
            print("Unable to connect to the database.")
        else:
            print('Successfully connected to the database.')
            return mydb
    
class DBConnUtil:
    @staticmethod
    def get_connection_object(mydb):
        try:
            mycursor = mydb.cursor()
            
        except:
            print("Error in getting cursor object")
        else:
            print("Cursor created successfully")
            return mycursor, mydb