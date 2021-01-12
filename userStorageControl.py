from foodStorageControl import *

import datetime



USER_DATA_FILE = "userInfoStorage.json"
CALORIES_DATA_FILE = "caloriesDB.json"

def getDayMonthYear():
	x = datetime.datetime.now()
	return str(x.strftime("%d"))+"/"+str(x.strftime("%m"))+"/"+str(x.strftime("%Y"))
	

def getAllDataFromUserDataStorage():
	with open(USER_DATA_FILE) as f:
		foodStorage = json.load(f)
	return foodStorage


def getCurrentDayDataFromUserDataStorage():
	with open(USER_DATA_FILE) as f:
		foodStorage = json.load(f)
	try:
		return foodStorage[getDayMonthYear()]
	except:
		return 0

def sendAllDataToFoodStorage(foodStorage):
	with open(USER_DATA_FILE,"w") as f:
		json.dump(foodStorage,f)


def isDayAlreadyCreated(FILE):
	with open(FILE) as f:
		userFoodData = json.load(f)

	try:
		status = userFoodData[getDayMonthYear()]
		return 1
	except:
		return 0

def isFoodAlreadyPresent(foodName):
	userFoodData = getAllDataFromUserDataStorage()
	for key in userFoodData[getDayMonthYear()].keys():
		if key == foodName:
			return 1
	return 0

def addFoodToUserStorage(foodName,grams):
	#check if food exists in DB
	if(storedFoodReturner(foodName,sendBool = 1)==0):
		print("no such food in DB")
		return

	#check if day has been created
	userFoodData = getAllDataFromUserDataStorage()
	if(isDayAlreadyCreated(USER_DATA_FILE)):
		userFoodData[getDayMonthYear()][foodName] =  grams
		sendAllDataToFoodStorage(userFoodData)
		print("food added")
		return

	else:
		userFoodData[getDayMonthYear()] = {foodName : grams}
		sendAllDataToFoodStorage(userFoodData)
		print("food added")



def removeFoodToUserStorage(foodName):
	# check if food exists in DB
	if(storedFoodReturner(foodName,sendBool = 1)==0):
		print("no such food in DB")
		return
	
	#check if day has been created
	userFoodData = getAllDataFromUserDataStorage()
	if(isDayAlreadyCreated(USER_DATA_FILE)):
		try:
			del userFoodData[getDayMonthYear()][foodName]
			sendAllDataToFoodStorage(userFoodData)
			print("successfully removed")
			return
		except:
			print("no such food in list")

	else:
		print("no list to remove from")


def listCurrentDayFood():
	if(getCurrentDayDataFromUserDataStorage() !=0):
		listOfFood = getCurrentDayDataFromUserDataStorage()
		print("no)| food  | amount")
		for num ,key in enumerate(listOfFood.keys()):
			print(f"%d) | %s  | %sg "%(num+1,key,listOfFood[key]))
	else:
		print("no list")
		

def detailedListCurrentDayFood():
	if(getCurrentDayDataFromUserDataStorage() != 0):
		listOfFood = getCurrentDayDataFromUserDataStorage()
		foodFromDB  = getAllDataFromFoodStorage()
		sumCarb =0 ; sumProtein =0;sumFat =0

		for num ,key in enumerate(listOfFood.keys()):
			print(f"%d) | %s  | %sg | carb-> %d | protein -> %d | fat -> %d"
			%(num+1,key,listOfFood[key],foodFromDB[key]["carb"],foodFromDB[key]["protein"],foodFromDB[key]["fat"]))
			sumCarb += foodFromDB[key]["carb"]
			sumProtein += foodFromDB[key]["protein"]
			sumFat  += foodFromDB[key]["fat"]
		print(f"total carb = %dg\t\ttotal protein = %dg\notal fat = %dg\t\ttotal calories = %dcal"
		%(sumCarb,sumProtein,sumFat,((4*sumCarb)+(4*sumProtein)+(9*sumFat))))
		

	else:
		print("no list")






def getAllDataFromcaloriesDB():
	try:
		with open(CALORIES_DATA_FILE) as f:
			calorieStorage = json.load(f)
		return calorieStorage
	except:
		return 0



def sendAllDataTocaloriesDB(calorieStorage):
	with open(CALORIES_DATA_FILE,"w") as f:
		json.dump(calorieStorage,f)


def createCalorieDB(calorie):
	setCalorie = {"setCalorie" : calorie}
	with open(CALORIES_DATA_FILE,"w") as f:
		json.dump(setCalorie,f)



def setLimitCaloriesInDB(calorie):
	calorieData = getAllDataFromcaloriesDB()
	if( calorieData == 0):
		createCalorieDB(calorie)
	else:
		calorieData["setCalorie"] = calorie
		sendAllDataTocaloriesDB(calorieData)


def getLimitCaloriesInDB():
	calorieData = getAllDataFromcaloriesDB()
	if( calorieData == 0):
		return -1
	else:
		try:
			return calorieData["setCalorie"]
		except:
			return -1
		
		
		

def calObjectCreater(carb,protein,fat,totalCal):
	return {"calories" : totalCal, "carb":carb,"protein":protein,"fat":fat}


def calculateMacrosOfTheDay():
	currentDayData = getCurrentDayDataFromUserDataStorage()
	foodStaorageDB = getAllDataFromFoodStorage()
	protein =0 ; carb =0; fat =0; totalCal=0
	for key in currentDayData.keys():
		protein += ((currentDayData[key]*foodStaorageDB[key]["protein"])/100)
		carb += foodStaorageDB[key]["carb"]
		fat += foodStaorageDB[key]["fat"]
	
	totalCal = (4*protein)+(4*carb)+(9*fat)
	return calObjectCreater(carb,protein,fat,totalCal)



def setCalorieOfDay():
	caloriesDB = getAllDataFromcaloriesDB()
	macroOfTheDay = calculateMacrosOfTheDay()
	dayMonthYear = getDayMonthYear()
	if(isDayAlreadyCreated(CALORIES_DATA_FILE)):
		caloriesDB[dayMonthYear]["carb"] = macroOfTheDay["carb"]
		caloriesDB[dayMonthYear]["protein"] = macroOfTheDay["protein"]
		caloriesDB[dayMonthYear]["fat"] = macroOfTheDay["fat"]
		caloriesDB[dayMonthYear]["calories"] = macroOfTheDay["calories"]
		sendAllDataTocaloriesDB(caloriesDB)
	else:	
		caloriesDB[dayMonthYear] = macroOfTheDay
		sendAllDataTocaloriesDB(caloriesDB)


def getCalorieOfDay():
	caloriesDB = getAllDataFromcaloriesDB()
	if(isDayAlreadyCreated(CALORIES_DATA_FILE)):
		return caloriesDB[getDayMonthYear()]["calories"]
	else:
		return -1

	
def caloriesConsumed():
	if(getLimitCaloriesInDB() != -1 and getCalorieOfDay() != -1):
		setCalorie = getLimitCaloriesInDB()
		calorieOfDay = getCalorieOfDay()
		#if negitive then surplus calorie
		return (setCalorie - calorieOfDay)
	
	else:
		return -1


def getDataForGraph(value = 0):
	storageDB = getAllDataFromcaloriesDB()
	if(storageDB == 0):
		return 0
	del storageDB["setCalorie"]
	if(value):
		temp = [storageDB[date] for date in storageDB.keys() ]
		return temp

	temp = [date for date in storageDB.keys() ]
	return temp








