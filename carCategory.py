import communMethods
from car import clsCar
class clsCarCategory:
     

    def __init__(self,catID, categoryName,DB_CategoryManager):
        
        
        self._categoryID = catID

        self._categoryName = categoryName
        self._DB_CategoryManager = DB_CategoryManager

    @property
    def categoryID(self):
        return self._categoryID

    @categoryID.setter
    def categoryID(self, value):
        self._categoryID = value

    @property
    def categoryName(self):
        return self._categoryName

    @categoryName.setter
    def categoryName(self, value):
        self._categoryName = value

  
    def EmptyCarCategoryObject(db):
        return clsCarCategory(-1,"",db)

    def addCategoryInfoToDB(self):
        if self.categoryID != -1:
            categoryInfo = (self.categoryID, self.categoryName)
            try: 
                cursor = self._DB_CategoryManager.db_connection.cursor()
                query = "INSERT INTO carcategory VALUES (%s, %s)"
                cursor.execute(query, categoryInfo)

                self._DB_CategoryManager.db_connection.commit()
                cursor.close()
                return True
            except Exception as e:
                return e 
        return False 
    def toTuple(self):
        return (self.categoryID, self.categoryName)
    def updateCategoryInfoInDB(self):
       
        categoryInfo = (self.categoryName,self.categoryID)
        try: 
            cursor = self._DB_CategoryManager.db_connection.cursor()
            query = "UPDATE carcategory SET  categoryName = %s where categoryID = %s "
            cursor.execute(query, categoryInfo)
            self._DB_CategoryManager.db_connection.commit()
            cursor.close()
            return True
        except Exception as e:
            return e
    
   
    def searchCategoryInfoInTableById(self,id):
        
        cursor = self._DB_CategoryManager.db_connection.cursor()
        query = "select * from carcategory where categoryID = %s"            
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        
        cursor.close()

        if result:
            return clsCarCategory(result[0],result[1],self._DB_CategoryManager)
        else:
            return self.EmptyCarCategoryObject()
        
    def searchCategoryInfoInTableByName(self,name):
        
        cursor = self._DB_CategoryManager.db_connection.cursor()
        query = "select * from carcategory where categoryName = %s"            
        cursor.execute(query, (name,))
        result = cursor.fetchone()
        
        cursor.close()

        if result:
            return clsCarCategory(result[0],result[1],self._DB_CategoryManager)
        else:
            return self.EmptyCarCategoryObject()
    
    def getAllCategorysInfoFromTable(self):
        
        cursor = self._DB_CategoryManager.db_connection.cursor()
        query = "select * from carcategory "            
        cursor.execute(query )
        result = cursor.fetchall()
        
        cursor.close()

        if result:
            return result
        else:
            return None
    def getAllCategorysNamesFromTable(self):
        
        cursor = self._DB_CategoryManager.db_connection.cursor()
        query = "select categoryName from carcategory "            
        cursor.execute(query )
        result = cursor.fetchall()
        
        cursor.close()

        if result:
            return result
        else:
            return None
        
        
    def _deleteCarCategoryIDFromCarsTable(self,id):
        b = clsCar.EmptyCar(self._DB_CategoryManager)
        records = b.searchCarInfoInCarstableBycarCategoryID(id)
        if records != None:
            for rec in records:
                b.deleteCarInfoFromDB(rec[0])

    def deleteCategoryInfoFromDB(self,id):
        if self.searchCategoryInfoInTableById(id):
            try: 
                self._deleteCarCategoryIDFromCarsTable(id)
                cursor = self._DB_CategoryManager.db_connection.cursor()
                query = "delete from carcategory where categoryID = %s"            
                cursor.execute(query, (id,))

                self._DB_CategoryManager.db_connection.commit()
                cursor.close()
                return True
            except Exception as e:
                return e
        return False

 