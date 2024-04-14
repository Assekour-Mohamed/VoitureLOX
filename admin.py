
class clsAdmin:
    def __init__(self, adminID, fullName, contactInfo, Password,db_Manager, isEmptyObject = False):
        if isEmptyObject:
            self._adminID = -1
        else :
            self._adminID = adminID

        self._fullName = fullName
        self._contactInfo = contactInfo
        self._Password = Password
        self._db_Manager = db_Manager

    
    def EmptyadminObject(db):
        return clsAdmin( -1,"","","",db,True)

    def addadminInfoToDB(self):
        if self.adminID != -1:
            adminInfo = (self.adminID, self.fullName, self.contactInfo, self.Password)
            try: 
                cursor = self._db_Manager.db_connection.cursor()
                query = "INSERT INTO admin VALUES (%s, %s, %s, %s)"
                cursor.execute(query, adminInfo)

                self._db_Manager.db_connection.commit()
                cursor.close()
                return True
            except Exception as e:
                return e 
        return False 
                  
    def updateadminInfoInDB(self,adminID_toUpdate):
        if self.adminID != -1 and self.searchadminInfoInadminsTaleByCID(adminID_toUpdate):
            adminInfo = (  self.fullName, self.contactInfo, self.Password,adminID_toUpdate)
            try: 
                cursor = self._db_Manager.db_connection.cursor()
                query = "UPDATE admin SET fullName =%s, contactInfo =%s, Password =%s  WHERE adminID = %s"

                cursor.execute(query, adminInfo)

                self._db_Manager.db_connection.commit()
                cursor.close()
                return True
            except Exception as e:
                return e
        return False
    
    def searchadminInfoInadminsTaleByCID(self,id):
        
        cursor = self._db_Manager.db_connection.cursor()
        query = "select * from admin where adminID = %s"            
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        
        cursor.close()

        if result:
            return result
        else:
            return None
    
    def searchadminInfoInadminsTaleByIDandPassword(self,id,pwd):
        
        cursor = self._db_Manager.db_connection.cursor()
        query = "select * from admin where adminID = %s and password = %s"            
        cursor.execute(query, (id,pwd))
        result = cursor.fetchone()
        
        cursor.close()

        if result:
            return result
        else:
            return None
        
    def getAlladminInfoFromCustomesTable(self):
        
        cursor = self._db_Manager.db_connection.cursor()
        query = "select * from admin"            
        cursor.execute(query )
        result = cursor.fetchall()
        
        cursor.close()

        if result:
            return result
        else:
            return None
    
        
    def deleteadminInfoFromDB(self,id):
        if self.searchadminInfoInadminsTaleByCID(id):
            try: 
                cursor = self._db_Manager.db_connection.cursor()
                query = "delete from admin where adminID = %s"            
                cursor.execute(query, (id,))

                self._db_Manager.db_connection.commit()
                cursor.close()
                return True
            except Exception as e:
                return e
        return False
    
    @property
    def adminID(self):
        return self._adminID

    @adminID.setter
    def adminID(self, value):
        self._adminID = value

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
    def Password(self):
        return self._Password

    @Password.setter
    def Password(self, value):
        self._Password = value
