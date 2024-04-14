import mysql.connector

class clsCarRentalDBManger:
    _instance = None

    def __init__(self):
        if not clsCarRentalDBManger._instance:
            self.connect_to_database()
            clsCarRentalDBManger._instance = self

    def connect_to_database(self):
        try:
            self.db_connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ass2@moha",
                database="carrental",
    			auth_plugin='mysql_native_password'

            )
            return True
        except mysql.connector.Error as e:
            return e
 
    def close_connection(self):
        try:
            self.db_connection.close()
            return "Database connection closed"
        except AttributeError:
            return "No database connection to close"
 