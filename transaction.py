import communMethods

class clsTransaction:
    def __init__(self,transactionID, bookingID, returnID, totalDueAmount, transactionDate,db_Manager):
        self._transactionID = transactionID
        self._bookingID = bookingID
        self._returnID = returnID
        self._totalDueAmount = totalDueAmount
        self._transactionDate = transactionDate
        self._db_Manager = db_Manager


    def EmptyTransactionObject(db):
        return clsTransaction( -1,-1,-1,0,'2009-12-22',db)

    def addTransactionInfoToDB(self):
        if self.returnID != -1 :
            TransactionInfo = (self.transactionID ,self.bookingID, self.returnID, self.totalDueAmount, self.transactionDate)
            try: 
                cursor = self._db_Manager.db_connection.cursor()
                query = "INSERT INTO transaction VALUES (%s, %s, %s, %s,%s)"
                cursor.execute(query, TransactionInfo)

                self._db_Manager.db_connection.commit()
                cursor.close()
                return True
            except Exception as e:
                return e 
        return False 
    
    def updateTransactionInfoInDB(self):
        TransactionInfo = (self.bookingID, self.returnID, self.totalDueAmount, self.transactionDate,self.transactionID)
        try: 
            
            cursor = self._db_Manager.db_connection.cursor()
            query = "UPDATE transaction SET  bookingID =%s, returnID =%s,totalDueAmount =%s, transactionDate =%s  WHERE transactionID = %s"
            
            cursor.execute(query, TransactionInfo)
            self._db_Manager.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            return e
    
    def searchTransactionInfoInTransTableByTransID(self,id):
        
        cursor = self._db_Manager.db_connection.cursor()
        query = "select * from transaction where transactionID = %s"            
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        
        cursor.close()

        if result:
            return result
        else:
            return None
    def searchTransactionInfoInTransTableByReturnID(self,id):
        
        cursor = self._db_Manager.db_connection.cursor()
        query = "select * from transaction where returnID = %s"            
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        
        cursor.close()

        if result:
            return result
        else:
            return None
    def searchTransactionInfoInTransTableByBookingID(self,id):
        
        cursor = self._db_Manager.db_connection.cursor()
        query = "select * from transaction where bookingID = %s"            
        cursor.execute(query, (id,))
        result = cursor.fetchall()
        
        cursor.close()

        if result:
            return result
        else:
            return None
        
    def getAllTransactionInfoFromDBTransactionTables(self):
        
        cursor = self._db_Manager.db_connection.cursor()
        query = "select * from transaction"            
        cursor.execute(query )
        result = cursor.fetchall()
        
        cursor.close()

        if result:
            return result
        else:
            return None
      
    def deleteTransactionInfoFromDB(self,id):
        if self.searchTransactionInfoInTransTableByTransID(id):
            try: 
                cursor = self._db_Manager.db_connection.cursor()
                query = "delete from transaction where transactionID = %s"            
                cursor.execute(query, (id,))

                self._db_Manager.db_connection.commit()
                cursor.close()
                return True
            except Exception as e:
                return e
        return False

    @property
    def transactionID(self):
        return self._transactionID

    @transactionID.setter
    def transactionID(self, value):
        self._transactionID = value

    @property
    def bookingID(self):
        return self._bookingID

    @bookingID.setter
    def bookingID(self, value):
        self._bookingID = value

    @property
    def returnID(self):
        return self._returnID

    @returnID.setter
    def returnID(self, value):
        self._returnID = value

    @property
    def totalDueAmount(self):
        return self._totalDueAmount

    @totalDueAmount.setter
    def totalDueAmount(self, value):
        self._totalDueAmount = value

    @property
    def transactionDate(self):
        return self._transactionDate

    @transactionDate.setter
    def transactionDate(self, value):
        self._transactionDate = value
