from datetime import datetime
import re
dateformat ="%Y-%m-%d"
def validate_date(date_string):
		pattern = r'^\d{4}-\d{2}-\d{2}$'
		if re.match(pattern, date_string):
				return True
		else:
				return False
def validateStartAndEndDates(start , end):
	 
	if validate_date(start) == False:
		return False
	elif validate_date(end) == False:
		return False
	elif (datetime.strptime(start,dateformat).date() >= datetime.strptime(end,dateformat).date()):
		return False
	else:
		return	True

def validateDecimal(number,BPoint, APoint):
	pattern = r'^\d{1,' + str(BPoint) + r'}(\.\d{0,' + str(APoint) + '})?$'
	if re.match(pattern,number):
		return True
	return False
 

def validatePhone(email):
	if re.match(r'^\+\d{3}\s\d{9}$', email):
		return True
	return False

def  validateReturnInputs(returnDate,rntelDays,milage,checkNotes):
	if not (  returnDate and rntelDays and milage,checkNotes):
		return ("Fill your input(s) ")
	elif validate_date(returnDate) == False:
		return( "wrong return date format correct date : YYYY-MM-DD")
	elif rntelDays.isnumeric() == False :
		return( "Should enter number in rental days")
	
	elif milage.isnumeric() == False :
		return( "Should enter number in rental days")
	
	elif len(checkNotes) >500:
		return( "CheckNotes should not pass 500 letter")
	 
	else :
		return True
	
def validateCustomerInputs(fullname,conatct,licenseNumber):
	if not (  fullname and conatct and licenseNumber):
		return ("Fill your input(s) ")
	elif len(fullname) > 20:
		return( "Fullname  should not pass 10 letters")
	elif len(conatct) > 16  :
		return( "Contact should not pass 16 letters")
	elif validatePhone(conatct) == False:
		return "Invalid contact correct format +333 222222222 "
	elif len(licenseNumber) > 10:
		return( "Lisence number  should not pass 10 letters")
	else :
		return True
	
def validateBookingInputs(CustomerID,CarID,StartDate,EndDate,PupLoction,DropOffLoction,Days,priceDay,amount,checkNotes):
	if not (CustomerID and CarID and StartDate and EndDate and PupLoction and DropOffLoction and Days and priceDay and amount and checkNotes):
		return ("Fill your input(s) ")
	elif len(CustomerID) > 10:
		return( "Customer id shoul not pass 10 letters")
	elif CarID.isnumeric() == False:
		return( "should enter just Numbers in car id")
	elif validate_date(StartDate) == False:
		return( "wrong start date format correct date : YYYY-MM-DD")
	elif datetime.strptime(StartDate,'%Y-%m-%d').date() < datetime.now().date(): 
		return( "wrong start date")
	if validate_date(EndDate) == False:
		return( "wrong end date format correct date : YYYY-MM-DD")
	elif datetime.strptime(EndDate,'%Y-%m-%d').date() < datetime.now().date(): 
		return( "wrong end date")
	elif len(PupLoction) > 45:
		return( "Pick up location should not pass 45 letter")
	elif len(DropOffLoction) > 45:
		return( "Drop off location should not pass 45 letter")
	elif len(DropOffLoction) > 45:
		return( "Drop off location should not pass 45 letter")
	elif Days.isnumeric() == False:
		return( "rental Days should be number")
	elif validateDecimal(priceDay,3,2) == False:
		return( "Price day should be between :1.0 999.99")
	elif validateDecimal(amount,5,2) == False:
		return( "Amount should be between :1.0 99999.99")
	elif len(checkNotes) >500:
		return( "CheckNotes should not pass 500 letter")
	else :
		return True

def validateCarInputs(id,make, model, year, milage, plateNumber , rntlPriceDay):
	if not(id and make and model and year and milage and plateNumber and rntlPriceDay):
		return ("Fill your input(s) ")
	elif len(id) > 10:
		return( "Customer id shoul not pass 10 letters")
	elif year != None: 
		if year.isnumeric() == True:	
			if int(year) > datetime.now().date().year or int(year) <1950:	
				return("Invalid year")
		else:
			return "Year should be a number"
	if len(make) > 45:
		return("make should not pass 45 letter")
	elif len(model) > 45:
		return("model should not pass 45 letter")
	elif len(plateNumber) > 45:
		return("plate number should not pass 45 letter")
	elif milage.isnumeric() == False:
		return("rental Days should be number")
	elif validateDecimal(rntlPriceDay,3,2) == False:
		return("Price day should be between :1.0 999.99")
	else :
		return True
		
def validateTransactionInputs(BookID,RetrunID,Amount):
	if not(BookID and RetrunID and Amount ):
		return ("Fill your input(s) ")
	elif BookID.isnumeric() ==False:
		return( "Booking id should be number")
	elif RetrunID.isnumeric() ==False:
		return( "Return id should be number")
	elif validateDecimal(Amount,5,2) == False:
		return("Price day should be between :1.0 999.99")
	else :
		return True

	
	
		
		