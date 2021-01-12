import sys
from  foodStorageControl import addFoodToInventory ,removeFoodFromInventory ,updateFoodInInventory,ListFoodInInventory
from userStorageControl import listCurrentDayFood,detailedListCurrentDayFood,caloriesConsumed,getCalorieOfDay,getLimitCaloriesInDB,setLimitCaloriesInDB,removeFoodToUserStorage,addFoodToUserStorage
from graph import createGraph
from manual import *

def  main():

	#no arguments
	if(len(sys.argv) == 1):
		helps()
		return
	
	# with one arguments
	if(len(sys.argv) == 2):

		argument = str(sys.argv[1])

		if(argument == "ls"):
			listCurrentDayFood()
			return
		elif(argument == "dls"):
			detailedListCurrentDayFood()
			return
		elif(argument == "lsdb"):
			ListFoodInInventory()
			return
			
		elif(argument == "cal"):
			if(caloriesConsumed() == -1):
				print("calorie not set")
				return
			if(caloriesConsumed() == 0):
				print(f"set calorie : %d cal consumed : %d cal balanced : %d cal"%(getLimitCaloriesInDB(),getCalorieOfDay(),caloriesConsumed()))
			elif(caloriesConsumed()<0):
				print(f"set calorie : %d cal consumed : %d cal surplus : +%d cal"%(getLimitCaloriesInDB(),getCalorieOfDay(),caloriesConsumed()*-1))

			else:
				print(f"set calorie : %d cal consumed : %d cal deficit : -%d cal"%(getLimitCaloriesInDB(),getCalorieOfDay(),caloriesConsumed()))


		elif(argument == "graph"):
			createGraph()
			return
		elif(argument == "help"):
			helps()
			return
		else:
			print("invalid command")
			return

	#with two arguments
	if(len(sys.argv) == 3):
		argument = sys.argv[1]
		if(argument == "setcal"):
			try:
				setLimitCaloriesInDB(int(sys.argv[2]))
				print("calorie set")
				return
			except:
				print("invalid input")
				return
		if(argument == "rm"):
			removeFoodToUserStorage(sys.argv[2])
			return
		if(argument == "rmdb"):
			removeFoodFromInventory(sys.argv[2])
			return
		else:
			print("invalid command")
			return

	#with three arguments
	if(len(sys.argv) == 4):
		argument = sys.argv[1]
		if(argument == "add"):
			try:
				addFoodToUserStorage(sys.argv[2],int(sys.argv[3]))
				return
			except:
				print("invalid command")
				return
		else:
			print("invalid command")
			return
    #with five arguments
    #addFoodToInventory(foodName,carbs,protein,fat)
	if(len(sys.argv) == 6):
		argument = sys.argv[1]
		if(argument == "addtodb"):
			try:
				addFoodToInventory(sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))
				return
			except:
				print("invalid command")
				return
		else:
			print("invalid command")
			return

	#with six arguments
	if(len(sys.argv) == 7):
		argument = sys.argv[1]
		if(argument == "updateindb"):
			try:
				newname = sys.argv[3] if(sys.argv[3] != "-1") else -1
				updateFoodInInventory(sys.argv[2],newname,int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]))
				return
			except:
				print("invalid command")
				return
		else:
			print("invalid command")
			return

	else:
		print("invalid command")
		return
			












	

