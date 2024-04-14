from booking import clsBooking

class clsCustomer:
    def __init__(self, customerID, fullName, contactInfo, licenseNumber,db_Manager, isEmptyObject = False):
        if isEmptyObject:
            self._customerID = -1
        else :
            self._customerID = customerID

        self._fullName = fullName
        self._contactInfo = contactInfo
        self._licenseNumber = licenseNumber
        self._db_Manager = db_Manager

    
    def EmptyCustomerObject(db):
        return clsCustomer( -1,"","","",db,True)

    def addCustomerInfoToDB(self):
        if self.customerID != -1:
            CustomerInfo = (self.customerID, self.fullName, self.contactInfo, self.licenseNumber)
            try: 
                cursor = self._db_Manager.db_connection.cursor()
                query = "INSERT INTO customer VALUES (%s, %s, %s, %s)"
                cursor.execute(query, CustomerInfo)

                self._db_Manager.db_connection.commit()
                cursor.close()
                return True
            except Exception as e:
                return e 
        return False 
                   
    def updateCustomerInfoInDB(self ):
        CustomerInfo = (  self.fullName, self.contactInfo, self.licenseNumber,self.customerID)
        try: 
            cursor = self._db_Manager.db_connection.cursor()
            query = "UPDATE customer SET fullName =%s, contactInfo =%s, licenseNumber =%s  WHERE customerID = %s"
            cursor.execute(query, CustomerInfo)
            self._db_Manager.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            return e
    
    def searchCustomerInfoInCustomersTaleByCustomerID(self,id):
        
        cursor = self._db_Manager.db_connection.cursor()
        query = "select * from customer where customerID = %s"            
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        
        cursor.close()

        if result:
            return result
        else:
            return None
    def searchCustomerInfoInCustomersTaleByLicenseNumber(self,number):
        
        cursor = self._db_Manager.db_connection.cursor()
        query = "select * from customer where licenseNumber = %s"            
        cursor.execute(query, (number,))
        result = cursor.fetchone()
        
        cursor.close()

        if result:
            return result
        else:
            return None
    def searchCustomerInfoInCustomersTaleByFullname(self,name):
        
        cursor = self._db_Manager.db_connection.cursor()
        query = "select * from customer where fullname = %s"            
        cursor.execute(query, (name,))
        result = cursor.fetchall()
        
        cursor.close()

        if result:
            return result
        else:
            return None
        
    def getAllCustomerInfoFromCustomesTable(self):
        
        cursor = self._db_Manager.db_connection.cursor()
        query = "select * from customer"            
        cursor.execute(query )
        result = cursor.fetchall()
        
        cursor.close()

        if result:
            return result
        else:
            return None
    
    def _deleteCustomerIDfromCustomersTable(self,id):
        c = clsBooking.EmptyBookingObject(self._db_Manager)
        records = c.searchBookingInfoInDBbyCustomerID(id)
        if records != None:
            for rec in records:
                c.deleteBookingInfoFromDB(rec[0]) 
        
    def deleteCustomerInfoFromDB(self,id):
        if self.searchCustomerInfoInCustomersTaleByCustomerID(id):
            try: 
                self._deleteCustomerIDfromCustomersTable(id)
                cursor = self._db_Manager.db_connection.cursor()
                query = "delete from customer where customerID = %s"            
                cursor.execute(query, (id,))

                self._db_Manager.db_connection.commit()
                cursor.close()
                return True
            except Exception as e:
                return e
        return False
 


    @property
    def customerID(self):
        return self._customerID

    @customerID.setter
    def customerID(self, value):
        self._customerID = value

    @property
    def fullName(self):
        return self._fullName

    @fullName.setter
    def fullName(self, value):
        self._fullName = value

    @property
    def contactInfo(self):
        return self._contactInfo

    @contactInfo.setter
    def contactInfo(self, value):
        self._contactInfo = value

    @property
    def licenseNumber(self):
        return self._licenseNumber

    @licenseNumber.setter
    def licenseNumber(self, value):
        self._licenseNumber = value
