from datetime import datetime
import re
def generatID_ByDate():
  dt = datetime.now() 
  id = int(str(dt.year % 1000 + dt.month + dt.day)+ str( dt.hour + dt.minute)+ str(dt.second))
  return id 

 
def generateID_ByIncrementLastID(db_Manager,table,colID):
  mycursor = db_Manager.db_connection.cursor()

  sql = f'SELECT MAX({colID}) FROM {table}'  
  mycursor.execute(sql )
  result = mycursor.fetchone()
  max_id = result[0] if result[0] is not None else 0
  mycursor.close()    
  return max_id + 1

def currentDate():
  return datetime.now().date()
 
def validate_date(date_string):
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(pattern, date_string):
        return True
    else:
        return False
 