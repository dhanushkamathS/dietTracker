manual = """diet-app            System Manager's Manual            

NAME
        diet-app  -  sh script designed to  log , analyse and maintain\n\tthe consumption of food with a full database controle\n\tto add , remove and update
       
DESCRIPTION
        sh script designed to  log , analyse and maintain\n\tthe consumption of food with a full database controle\n\tto add , remove and update, visualise the progress with graph

PARAMETERS

diet-app ls  - provides a list of food consumed on the current day\n
diet-app dls - provides a detailed list of food consumed on the current day\n
diet-app cal - provides a calorie informaton of food consumed on the current day\n
diet-app graph - provides the graph to visualise the data\n
diet-app help  - help\n

diet-app setcal <amount>  - to set the calorie limit\n
diet-app rm  <foodName>   - food to be removed from that day\n
diet-app rmdb  <foodName> - food to be removed from the data base\n


diet-app add <foodName> <amount> - food to be added to the days list\n
diet-app addtodb <foodName> <carb> <protein> <fat> - food to be added to the data base where carb,protein,fat are given per 100g of that specific food\n
diet-app updateindb <foodName> <newFoodName> <carb> <protein> <fat> - food to be \t\t\tupdated in the data base,
\t\t\tprovide -1 if you don't wanna update that value


example:
diet-app updateindb brownrice -1 50 30 200 - this updates carb ,\n\t\t\tprotein and but not the name"""

def helps():
	print(manual)



  
