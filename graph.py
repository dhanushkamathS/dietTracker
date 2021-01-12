from userStorageControl import getDataForGraph as graphData
# import datetime as dt
import matplotlib.pyplot as plt
# import matplotlib.dates as mdates



def createGraph():
	key = graphData(0)
	value = graphData(1)
	caloriesArray = [calorie["calories"] for calorie in value]
	carbsArray = [calorie["carb"] for calorie in value]
	proteinsArray = [calorie["protein"] for calorie in value]
	fatsArray = [calorie["fat"] for calorie in value]

	#graph creation

	#x-axis
	# x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in key]
	# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
	# plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=3))
	plt.plot(key,caloriesArray, color = 'green', label = 'calories',marker = 'o')
	plt.plot(key,carbsArray, color = 'blue', label = 'carb',marker = 'o')
	plt.plot(key,proteinsArray, color = 'red', label = 'protein',marker = 'o')
	plt.plot(key,fatsArray, color = 'yellow', label = 'fat',marker = 'o')
	plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1),ncol=4)
	# plt.gcf().autofmt_xdate()
	plt.show()
	

		

