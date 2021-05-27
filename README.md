# dietTracker
# Helps to track the diet
![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)
![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)

Allows you to build your custom database of food
helps to visualize your consumption over time 

# diet-app            System Manager's Manual      <br />      

# NAME <br />
       diet-app  -  python script designed to  log , analyse and maintain 
       				the consumption of food with a full database controle 
       				to add , remove and update
       
# DESCRIPTION <br />
       python script designed to  log , analyse and maintain 
       the consumption of food with a full database controle 
       to add , remove and update, visualise the progress with 
       graph

# PARAMETERS <br />

diet-app ls  - provides a list of food consumed on the current day <br /><br />
diet-app dls - provides a detailed list of food consumed on the current day <br /><br />
diet-app cal - provides a calorie informaton of food consumed on the current day <br /><br />
diet-app graph - provides the graph to visualise the data <br /><br />
diet-app help  - help <br />
<br />
diet-app setcal <amount>  - to set the calorie limit <br /><br />
diet-app rm  <foodName>   - food to be removed from that day <br /><br />
diet-app rmdb  <foodName> - food to be removed from the data base <br />
<br />
<br />
diet-app add <foodName> <amount> - food to be added to the days list<br /><br />
  
diet-app addtodb <foodName> <carb> <protein> <fat> - food to be added to the data base where carb,protein,fat are given per 100g of that specific food<br /><br />
 <pre>
diet-app updateindb <foodName> <newFoodName> <carb> <protein> <fat> - food to be updated in the data base where carb,protein,fat are given per 100g of that
                                                   specific food . Provide -1 if you don't wanna update that value </pre>


<br />

# Example: <br />
diet-app updateindb brownrice -1 50 30 200 - this updates carb , protein and but not the name





