from transaction import clsTransaction
from car import clsCar
import loginInfo
class clsReturnDetails:
    def __init__(self,returnID, returnDate, rentalDays, carMilage, finalCheckNotes,db_Manager):
        self._returnID = returnID
        self._returnDate = returnDate
        self._actuelRentalDays = rentalDays
        self._carMilage = carMilage
        self._finalCheckNotes = finalCheckNotes
        self._db_Manager = db_Manager
   

    def EmptyReturnObject(db):
        return clsReturnDetails(-1, '2000-01-01',0,0,"",db)
    def updateCarMilageInCarsTable(self):
        emptyCar = clsCar.EmptyCar(loginInfo.DB_Mang)
        emptyCar.updateMilageInDb(self.returnID,self.carMilage)
    
    def addReturnInfoToDB(self):
        if self.returnID != -1:
            ReturnInfo = (self.returnID, self.returnDate, self.rentalDays, self.carMilage, self.finalCheckNotes)
            try: 
                cursor = self._db_Manager.db_connection.cursor()
                query = "INSERT INTO returndetails VALUES (%s, %s, %s, %s,%s)"
                cursor.execute(query, ReturnInfo)

                self._db_Manager.db_connection.commit()
                cursor.close()
                return True
            except Exception as e:
                return e 
        return False 
    
    def updateReturnInfoInDB(self):
            ReturnInfo = (self.returnDate, self.rentalDays, self.carMilage, self.finalCheckNotes,self.returnID)
            try: 
                cursor = self._db_Manager.db_connection.cursor()
                query = "UPDATE returndetails SET returnDate =%s, rentalDays =%s, carMilage =%s,finalCheckNotes =%s  WHERE ReturnID = %s"
                
                cursor.execute(query, ReturnInfo)

                self._db_Manager.db_connection.commit()
                cursor.close()
                return True
            except Exception as e:
                return e
    
    def seaechReturnInfoInReturnsTableRyReturnID(self,id):
        
        cursor = self._db_Manager.db_connection.cursor()
        query = "select * from returndetails where ReturnID = %s"            
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        
        cursor.close()

        if result:
            return result
        else:
            return None
        
    def getAllReturnInfoInReturnsTable(self):
        
        cursor = self._db_Manager.db_connection.cursor()
        query = "select * from returndetails"            
        cursor.execute(query )
        result = cursor.fetchall()
        
        cursor.close()

        if result:
            return result
        else:
            return None
        
    def _deleteReturnIDfromTransTable(self,id):
        c = clsTransaction.EmptyTransactionObject(self._db_Manager)
        records = c.searchTransactionInfoInTransTableByReturnID(id)
        if records != None:
            for rec in records:
                c.deleteTransactionInfoFromDB(rec[0]) 
        
        
    def deleteReturnInfoFromDB(self,id):
        if self.seaechReturnInfoInReturnsTableRyReturnID(id):
            try: 
                self._deleteReturnIDfromTransTable(id)
                cursor = self._db_Manager.db_connection.cursor()
                query = "delete from returndetails where ReturnID = %s"            
                cursor.execute(query, (id,))

                self._db_Manager.db_connection.commit()
                cursor.close()
                return True
            except Exception as e:
                return e
        return False
    @property
    def returnID(self):
        return self._returnID

    @returnID.setter
    def returnID(self, value):
        self._returnID = value

    @property
    def returnDate(self):
        return self._returnDate

    @returnDate.setter
    def returnDate(self, value):
        self._returnDate = value

    @property
    def rentalDays(self):
        return self._actuelRentalDays

    @rentalDays.setter
    def rentalDays(self, value):
        self._actuelRentalDays = value

    @property
    def carMilage(self):
        return self._carMilage

    @carMilage.setter
    def carMilage(self, value):
        self._carMilage = value

    @property
    def finalCheckNotes(self):
        return self._finalCheckNotes

    @finalCheckNotes.setter
    def finalCheckNotes(self, value):
        self._finalCheckNotes = value