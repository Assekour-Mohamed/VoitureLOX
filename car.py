import communMethods 
from booking import clsBooking
class clsCar:
    def __init__(self,carID, make, model, year, milage, plateNumber, carCategoryID, rntlPriceDay, isAvailableForRent,DB_CarManager  ):    
           
        self._carID = carID
        self._make = make
        self._model = model 
        self._year = year 
        self._milage = milage 
        self._plateNumber = plateNumber 
        self._carCategoryID  = carCategoryID 
        self._rntlPriceDay = rntlPriceDay 
        self._isAvailableForRent = isAvailableForRent 
        self._db_Manager = DB_CarManager

    @property
    def DB_CarManager(self):
        return self._db_Manager
    @property
    def carID(self):
        return self._carID
    @property
    def make(self):
        return self._make
    @make.setter
    def make(self, value):
        self._make = value
    @property
    def model(self):
        return self._model
    @model.setter
    def model(self, value):
        self._model = value
    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, value):
        self._year = value
    @property
    def milage(self):
        return self._milage
    @milage.setter
    def milage(self, value):
        self._milage = value
    @property
    def plateNumber(self):
        return self._plateNumber
    @plateNumber.setter
    def plateNumber(self, value):
        self._plateNumber = value
    @property
    def carCategoryID(self):
        return self._carCategoryID
    @carCategoryID.setter
    def carCategoryID(self, value):
        self._carCategoryID = value
    @property
    def rntlPriceDay(self):
        return self._rntlPriceDay
    @rntlPriceDay.setter
    def rntlPriceDay(self, value):
        self._rntlPriceDay = value
    @property
    def isAvailableForRent(self):
        return self._isAvailableForRent
    @isAvailableForRent.setter
    def isAvailableForRent(self, value):
      self._isAvailableForRent = value 
   
    def EmptyCar(db):
        return clsCar(-1,"","",0,0,"",0,0.0, 0,db)

    def getCarIDandOldMilage(self,returnID):
        cursor = self._db_Manager.db_connection.cursor()
        query = ''' select cars.carID , cars.milage  from cars 
                    join booking on booking.carID = cars.carID 
                    join transaction on transaction.BookingID = booking.bookingID
                    join returndetails on returndetails.returnID = transaction.returnID
                    where returndetails.returnID =  %s;    '''  
        cursor.execute(query, (returnID,))
        result = cursor.fetchone()
        
        cursor.close()

        return result
    
    def updateMilageInDb(self,returnRecordID, newMilage):
        carIDandOldMilage =self.getCarIDandOldMilage(returnRecordID)
        if carIDandOldMilage is not None:
            if newMilage > carIDandOldMilage[1]:
                try: 
                    cursor = self.DB_CarManager.db_connection.cursor()
                    query = "UPDATE cars SET milage = %s WHERE carID = %s"
                    cursor.execute(query, (newMilage,carIDandOldMilage[0]))
                    self.DB_CarManager.db_connection.commit()
                    cursor.close()
                    return True
                except Exception as e:
                    print(e)

    def addCarInfoToDB(self):
        if self.carID != -1:
            carinfo = (self.carID, self.make, self.model, self.year, self.milage, self.plateNumber, self.carCategoryID, self.rntlPriceDay, self.isAvailableForRent)
            try: 
                cursor = self.DB_CarManager.db_connection.cursor()
                query = "INSERT INTO cars VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, carinfo)

                self.DB_CarManager.db_connection.commit()
                cursor.close()
                return True
            except Exception as e:
                return e 
        return False 
                  
    def updateCarInfoInDB(self):
        carinfo = (self.make, self.model, self.year, self.milage, self.plateNumber, self.carCategoryID, self.rntlPriceDay, self.isAvailableForRent,self.carID)
        try: 
            cursor = self.DB_CarManager.db_connection.cursor()
            query = "UPDATE cars SET make = %s, model = %s, year = %s, milage = %s, plateNumber = %s, carCategoryID = %s, rntlPriceDay = %s, isAvailableForRent = %s WHERE carID = %s"
            cursor.execute(query, carinfo)
            self.DB_CarManager.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
   
    def searchCarInfoInCarstableByCarID(self,id):
        
        cursor = self.DB_CarManager.db_connection.cursor()
        query = "select * from cars where carID = %s"            
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        
        cursor.close()

        if result:
            return result
        else:
            return None
    def searchCarInfoInCarstableByMake(self,make):
        
        cursor = self.DB_CarManager.db_connection.cursor()
        query = "select * from cars where make = %s"            
        cursor.execute(query, (make,))
        result = cursor.fetchall()
        cursor.close()
        if result:
            return result
        else:
            return None
        
    def searchCarInfoInCarstableByPlate(self,plate):
        
        cursor = self.DB_CarManager.db_connection.cursor()
        query = "select * from cars where platenumber = %s"             
        cursor.execute(query, (plate,))
        result = cursor.fetchone()
        cursor.close()
        if result:
            return result
        else:
            return None
        
   
    def searchCarInfoInCarstableBycarCategoryID(self,id):
        
        cursor = self.DB_CarManager.db_connection.cursor()
        query = "select * from cars where carCategoryID = %s"            
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        
        cursor.close()

        if result:
            return result
        else:
            return None
        
    def getAllCarsInfoFromDBcarsTable(self ):
        
        cursor = self.DB_CarManager.db_connection.cursor()
        query = "select * from cars "            
        cursor.execute(query )
        result = cursor.fetchall()
        
        cursor.close()

        if result:
            return result
        else:
            return None
        

    def _deleteCarIDFromBookingsTable(self,id):
        b = clsBooking.EmptyBookingObject(self.DB_CarManager)
        records = b.searchBookingInfoInDBbyCarID(id)
        if records != None:
            for rec in records:
                b.deleteBookingInfoFromDB(rec[0])

    def _deleteCarIDFromCarsTable(self,id):
        try: 
            self._deleteCarIDFromBookingsTable(id)
            cursor = self.DB_CarManager.db_connection.cursor()
            query = "delete from cars where carID = %s"            
            cursor.execute(query, (id,))
            self.DB_CarManager.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            return e
    def deleteCarInfoFromDB(self,id):
        if self.searchCarInfoInCarstableByCarID(id):
            res = self._deleteCarIDFromCarsTable(id)
            return res
        return False

 