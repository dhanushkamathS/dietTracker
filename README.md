# dietTracker
# Helps to track the diet

Allows you to build your custom database of food
helps to visualize your consumption over time 

# diet-app            System Manager's Manual      <br />      

# NAME <br />
       diet-app  -  python script designed to  log , analyse and maintain 
       				the consumption of food with a full database controle 
       				to add , remove and update
       
# DESCRIPTION <br />
       sh script designed to  log , analyse and maintain 
       the consumption of food with a full database controle 
       to add , remove and update, visualise the progress with 
       graph

# PARAMETERS <br />

diet-app ls  - provides a list of food consumed on the current day
diet-app dls - provides a detailed list of food consumed on the current day
diet-app cal - provides a calorie informaton of food consumed on the current day
diet-app graph - provides the graph to visualise the data 
diet-app help  - help

diet-app setcal <amount>  - to set the calorie limit
diet-app rm  <foodName>   - food to be removed from that day
diet-app rmdb  <foodName> - food to be removed from the data base


diet-app add <foodName> <amount> - food to be added to the days list
  
diet-app addtodb <foodName> <carb> <protein> <fat> - food to be added to the data base where carb,protein,fat are given per 100g of that specific food
  
diet-app updateindb <foodName> <newFoodName> <carb> <protein> <fat> - food to be updated in the data base where carb,protein,fat are given per 100g of that
                                                                      specific food . Provide -1 if you don't wanna update that value


# Example: <br />
diet-app updateindb brownrice -1 50 30 200 - this updates carb , protein and but not the name





