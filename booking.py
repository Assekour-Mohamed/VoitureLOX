import communMethods
from transaction import clsTransaction
class clsBooking:
    def __init__(self,bookingID, customerID, carID, rentalStartDate,rentalEndDate, pickupLocation, dropOffLocation, rentalDays, rntlPriceDay, totalDueAmount, checkNotes, db_Manager ):
        
        self._bookingID = bookingID
        
        self._customerID = customerID
        self._carID = carID
        self._rentalStartDate = rentalStartDate
        self._rentalEndDate = rentalEndDate
        self._pickupLocation = pickupLocation
        self._dropOffLocation = dropOffLocation
        self._rentalDays = rentalDays
        self._rntlPriceDay = rntlPriceDay
        self._totalDueAmount = totalDueAmount
        self._checkNotes = checkNotes
        self._db_Manager = db_Manager

    def EmptyBookingObject(db):
        return clsBooking(-1,-1,-1,'2000-01-01','2000-01-02',"","",0,0.0, 0,"",db)
    def calculDueAmount(self, numDays, priceDay):
        return numDays * priceDay


    def addBookingInfoToDB(self):
        if self.carID != -1:
            BookingInfo = (self.bookingID,self.customerID, self.carID, self.rentalStartDate, self.rentalEndDate, self.pickupLocation, self.dropOffLocation, self.rentalDays, self.rntlPriceDay, self.totalDueAmount, self.checkNotes  )
            try: 
                cursor = self._db_Manager.db_connection.cursor()
                query = "INSERT INTO booking VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, BookingInfo)

                self._db_Manager.db_connection.commit()
                cursor.close()
                return True
            except Exception as e:
                return e 
        return False 
                  
    def updateBookingInfoInDB(self ):
 
            BookingInfo = ( self.customerID, self.carID, self.rentalStartDate, self.rentalEndDate, self.pickupLocation, self.dropOffLocation, self.rentalDays, self.rntlPriceDay, self.totalDueAmount, self.checkNotes ,self.bookingID)
            try: 
                cursor = self._db_Manager.db_connection.cursor()
                query = "UPDATE booking SET  customerID  = %s, carID  = %s, rentalStartDate = %s,rentalEndDate = %s, pickupLocation = %s, dropOffLocation = %s, rentalDays = %s, rntlPriceDay = %s, totalDueAmount = %s, checkNotes = %s  WHERE bookingID = %s"

                cursor.execute(query, BookingInfo)

                self._db_Manager.db_connection.commit()
                cursor.close()
                return True
            except Exception as e:
                return e
     
    def searchBookingInfoInDBbyBookingID(self,id): 
        cursor = self._db_Manager.db_connection.cursor()
        query = "select * from booking where bookingID = %s"            
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        
        cursor.close()

        if result:
            return result
        else:
            return None
        
    def searchBookingInfoInDBbyCarID(self,id): 
        cursor = self._db_Manager.db_connection.cursor()
        query = "select * from booking where carID = %s"            
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        
        cursor.close()

        if result:
            return result
        else:
            return None
        
    def searchBookingInfoInDBbyCustomerID(self,id): 
        cursor = self._db_Manager.db_connection.cursor()
        query = "select * from booking where customerID = %s"            
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        
        cursor.close()

        if result:
            return result
        else:
            return None
      
    

    def getAllBookingsInfoFromDBBookingsTable(self ):
        
        cursor = self._db_Manager.db_connection.cursor()
        query = "select * from booking "            
        cursor.execute(query)
        result = cursor.fetchall()
        
        cursor.close()

        if result:
            return result
        else:
            return None
     
    def _deleteBookingIDFromTransactionTable(self,id):
        b = clsTransaction.EmptyTransactionObject(self._db_Manager)
        records = b.searchTransactionInfoInTransTableByBookingID(id)
        print()
        if records != None:
            for rec in records:
                b.deleteTransactionInfoFromDB(rec[0])

    def deleteBookingInfoFromDB(self,id):
        if self.searchBookingInfoInDBbyBookingID(id):
            try:  
                self._deleteBookingIDFromTransactionTable(id)
                cursor = self._db_Manager.db_connection.cursor()
                query = "delete from booking where bookingID = %s"            
                cursor.execute(query, (id,))

                self._db_Manager.db_connection.commit()
                cursor.close()
                return True
            except Exception as e:
                return e
        return False
 
    @property
    def bookingID(self):
        return self._bookingID

    @bookingID.setter
    def bookingID(self, value):
        self._bookingID = value

    @property
    def customerID(self):
        return self._customerID

    @customerID.setter
    def customerID(self, value):
        self._customerID = value

    @property
    def carID(self):
        return self._carID

    @carID.setter
    def carID(self, value):
        self._carID = value

    @property
    def rentalStartDate(self):
        return self._rentalStartDate

    @rentalStartDate.setter
    def rentalStartDate(self, value):
        self._rentalStartDate = value

    @property
    def rentalEndDate(self):
        return self._rentalEndDate

    @rentalEndDate.setter
    def rentalEndDate(self, value):
        self._rentalEndDate = value

    @property
    def pickupLocation(self):
        return self._pickupLocation

    @pickupLocation.setter
    def pickupLocation(self, value):
        self._pickupLocation = value

    @property
    def dropOffLocation(self):
        return self._dropOffLocation

    @dropOffLocation.setter
    def dropOffLocation(self, value):
        self._dropOffLocation = value

    @property
    def rentalDays(self):
        return self._rentalDays

    @rentalDays.setter
    def rentalDays(self, value):
        self._rentalDays = value

    @property
    def rntlPriceDay(self):
        return self._rntlPriceDay

    @rntlPriceDay.setter
    def rntlPriceDay(self, value):
        self._rntlPriceDay = value

    @property
    def totalDueAmount(self):
        return self._totalDueAmount

    @totalDueAmount.setter
    def totalDueAmount(self, value):
        self._totalDueAmount = value

    @property
    def checkNotes(self):
        return self._checkNotes

    @checkNotes.setter
    def checkNotes(self, value):
        self._checkNotes = value
