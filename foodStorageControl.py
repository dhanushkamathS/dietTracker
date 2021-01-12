import json

#add food to inventory
FOOD_INVENTORY_FILE = "foodStorage.json"

def getAllDataFromFoodStorage():
	with open(FOOD_INVENTORY_FILE) as f:
		foodStorage = json.load(f)
	return foodStorage

def sendAllDataToFoodStorage(foodStorage):
	with open(FOOD_INVENTORY_FILE,"w") as f:
		json.dump(foodStorage,f)


def storedFoodReturner(foodName,sendBool=0):
	with open(FOOD_INVENTORY_FILE) as f:
		foodStorage = json.load(f)

	for value in foodStorage.keys():
		if(value == foodName):
			if(sendBool):
				return 1
			else:
				return foodStorage[value]
	if(sendBool):
		return 0
	return foodStorage
	
def fooObjectCreater(carb,protein,fat):
	return {"carb":carb,"protein":protein,"fat":fat}

def addFoodToInventory(foodName,carbs,protein,fat):
	if(storedFoodReturner(foodName,1)):
		print("already exists")
		return
	foodStorage = storedFoodReturner(foodName)
	
	newFoodToAdd = {"carb":carbs,"protein":protein,"fat":fat} 

	foodStorage[foodName] = newFoodToAdd

	sendAllDataToFoodStorage(foodStorage)
	print("food added to DB")



def removeFoodFromInventory(foodName,printer=1):
	if(storedFoodReturner(foodName,1) == 0):
		print("food does not exist")
		return
	foodStorage = getAllDataFromFoodStorage()
	del foodStorage[foodName]
	sendAllDataToFoodStorage(foodStorage)
	if(printer):
		print("food removed from DB")



def updateFoodInInventory(foodName,newFoodName=-1,carbs=-1,protein=-1,fat=-1):
	if(storedFoodReturner(foodName,1) == 0):
		print("food does not exist")
		return
	foodStorage = getAllDataFromFoodStorage()
	newCarbs = foodStorage[foodName]["carb"] if carbs ==-1 else carbs
	newProtein = foodStorage[foodName]["protein"] if protein ==-1 else protein
	newFat = foodStorage[foodName]["fat"] if fat ==-1 else fat

	updatedFood = fooObjectCreater(newCarbs,newProtein,newFat)

	removeFoodFromInventory(foodName,0)

	setFoodNameAs = foodName if newFoodName == -1 else newFoodName

	foodStorage[setFoodNameAs] = updatedFood

	sendAllDataToFoodStorage(foodStorage)
	print("DB has been updated")


def ListFoodInInventory():
	foodStorage = getAllDataFromFoodStorage()
	if(foodStorage != 0):
		for num ,key in enumerate(foodStorage.keys()):
			print(f"%d) | %s  | carb-> %d | protein -> %d | fat -> %d\n"
			%(num+1,key,foodStorage[key]["carb"],foodStorage[key]["protein"],foodStorage[key]["fat"]))


	else:
		print("no list")



	







