# Data Scrapping, Data Analysis, and Streamlit dashboard for Coffee Roaster Review ☕


## Introduction.

The following data analysis project is created to practice and gain more experience and knowledge in data analysis. For this project, everything begins with the collection of information that is extracted through the web scrapping method on the reviews of the different types of coffees that exist in the market, from a specific web page. 
The main objective is to generate a data framework that allows us to obtain information on how these reviews are structured in order to classify the different brands of coffees. The information about the process is documented in the notebooks in this repository.

## Objective.🎯

- Realize data collection with data scrape method of relevant information about Coffee Market for diverses brand of coffees.
- Clean and Wrangling the data fron data scrapping.
- Built a data frame with the information selected for create visualization and dashboard.

## Methods.📝

This project project starts with obtaining data from a web page using data scraping and then storing it as a 'csv' file. The module/tool used for scrape was Python and the librarie use was Beautifulsoup(bs4), Pandas for data cleaning and manipulation, matplotlib and seaborn for data visualizations, and finally to create an app with a Streamlit interactive dashboard.

The steps for the data scrapping task was the following:

- Create the url to get the information using headers.
- Create a function for extract the links for scrappe coffee review.
- Create the function to extract the link.
- Testing the information scraped for complete the scrape process.

After this test all the reviews were extracted with a total of 1920 reviews for further analysis and create the 'csv' file.

## Data exploration and cleaning.🔭

In this stage the data information is analized from the scrapping proccess. For this task the following steps are performed in order to obtain a collection of data that is suitable for analysis:

- Clean and wrangling the information of the data frame ( create and drop columns, change currency for the prices of coffee).

In order to have more detailed information about coffee prices, new columns were created. 
In this case price and quantity are separated in two new columns.

````
###create new columns to have price and quantity separated###
price= df['Est. Price'].str.split('[/]', expand=True)
price.columns = ['price', 'quantity']
df = pd.concat([df, price], axis=1)
df.drop(['Est. Price'], axis=1, inplace=True)
````

In the case of separating the price from the currency, a regex formula was used to achieve this separation and a new column was created.
````
# Create currency column for extract diferents currencies values from price column###
df['currency'] = df['price'].str.extract(('([a-zA-Z]\w{0,})'),expand = True)
df['currency'].unique()

array([nan, 'HKD', 'NT', 'pesos', 'CAD', 'USD', 'US', 'HK', 'LAK', 'IDR',
       'AUD', 'AED', 'NTD', 'Euros', 'KRW', 'THB', 'RMB'], dtype=object)
````

then the different prices were converted into a single currency,
in this case into eur and change value type to float.

````
### Transform diferents currencies to eur value
df['price_'] = df['price_'].replace(['N'],'0.030')
df['price_'] = df['price_'].replace(['$'],'0.85')
df['price_'] = df['price_'].replace(['H'],'0.11')

### Change value type of price from object to float
df['price2'] = df['price2'].astype(float)
````

the same for the weight measure was standardized to grams.

````
### Standardizing different measures to grams
df['unit'] = df['unit'].replace(['ounces'],'28.70')
df['unit'] = df['unit'].replace(['grams'],'1.00')
df['unit'] = df['unit'].replace(['bottle'],'220.0')
````

More information about cleaning process can be found in the Jupiter notebook 
'Review_Cleaning_and_Descriptive_analisis.ipynb'

- Add location coordenates for coffee roaster with geopy

To extract the geographic coordinates we used the geopy library and the Nominatim geocoder. 
Time librarie was also used to prevent the server from blocking the download of information due to the amount of georeferences requested.

````
import geopy.geocoders
from geopy.geocoders import Nominatim
import time
from time import sleep

geolocator = Nominatim(user_agent="wieder")

df_loc= pd.DataFrame(columns=['location'])
location_list=[]

for local in df['Roaster Location']:
  try:
    sleep(1)
    loc = geolocator.geocode(local).raw
    location_list.append(loc)
  except Exception as e:
    print(e)
    
 ````
 
- Realize descriptive analisis of the information collected (RDA).

After cleaning and organizing the data, descriptive analysis was performed. 
The dataframe information details that there are 1482 non-null data and the respective data types for each column. 
These data are correct and we can continue working with them.

````
<class 'pandas.core.frame.DataFrame'>
Int64Index: 1482 entries, 0 to 1682
Data columns (total 19 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   Rating             1482 non-null   float64
 1   Roaster            1482 non-null   object 
 2   Roaster Location   1481 non-null   object 
 3   Roast              1482 non-null   object 
 4   Name               1482 non-null   object 
 5   Coffee Origin      1482 non-null   object 
 6   Aroma              1482 non-null   float64
 7   Body               1482 non-null   float64
 8   Flavor             1482 non-null   float64
 9   Acidity/Structure  1216 non-null   float64
 10  Aftertaste         1482 non-null   float64
 11  Agtron             1482 non-null   float64
 12  Agtron scale       1482 non-null   float64
 13  euro               1482 non-null   float64
 14  euro/gr            1482 non-null   float64
 15  Review Date        1482 non-null   object 
 16  lat                1482 non-null   object 
 17  lon                1482 non-null   object 
 18  display_name       1482 non-null   object 
dtypes: float64(10), object(9)
memory usage: 231.6+ KB
````

The table shows the data classified with statistical parameters. It is observed that the average rating corresponds to 92.93 points. The minimum value corresponds to 83.0 rating points and the maximum to 98.0 rating points.
Another example is the value in eur/gr. where the average value corresponds to 0.093 euros/gr. and the maximum value to 16.5 euros/gr.

|     | Rating | Aroma |	Body |	Flavor |	Acidity/Structure |	Aftertaste | Agtron |	Agtron scale |	euro |	euro/gr |
| --- | --- | --- | --- | --- | ---| --- | --- | --- | --- | --- |
| count |	1482.000000 |	1482.000000 |	1482.000000 |	1482.000000 |	1216.000000 |	1482.000000 | 1482.000000 | 1482.000000 |	1482.000000 |	1482.000000 |
| mean	| 92.938596	| 8.805668 | 8.581646 | 8.939946 | 8.483553 |	8.081646 | 58.529015 | 74.304318 |	19.241494 |	0.093338 |
| std	| 1.707000 |	0.45308 |	0.516193 |	0.383360 |	0.560475 | 0.496525 |	135.727592 |	7.411861 |	23.533087 |	0.470286 |
| min	| 83.000000 |	7.000000 | 6.000000 | 7.000000 | 6.000000 | 6.000000	| 0.000000 | 37.000000 | 0.006960 |	0.000028 |
| 25%	| 92.000000 |	9.000000 | 8.000000 |	9.000000 | 8.000000	| 8.000000	| 52.000000	| 71.000000	| 12.750000	| 0.039464 |
| 50%	| 93.000000	| 9.000000	| 9.000000	| 9.00000	| 9.000000	| 8.000000	| 55.000000	| 76.000000	| 15.300000	| 0.046893 |
| 75%	| 94.000000	| 9.000000	| 9.000000	| 9.000000	| 9.000000	| 8.000000	| 58.000000	| 78.000000	| 18.700000	| 0.069892 | 
| max	| 98.000000	| 10.000000	| 10.000000	| 10.000000	| 10.000000	| 9.000000	| 5252.000000	| 105.000000	| 595.000000	| 16.500000 |


- Visualizations for understand the data obtained.

In order to better understand the table, some visualizations were created to better understand the data obtained. In this visualization a pie chart is drawn to determine in what proportion the coffee brands are distributed according to their rating. For this purpose, buckets were made according to the rating. Four ranges were created and are shown below:

````
# Coffee Category 

range_1 = df[df['Rating'] < 89]
range_2 = df[(df['Rating'] >= 89.1 ) & (df.Rating < 92)]
range_3 = df[(df['Rating'] >= 92.1 ) & (df.Rating < 95)]
range_4 = df[df['Rating'] >= 95.1 ]
-----------------------------------------------------------
# Pie chart plot

label_names=['< 89','90-92','92-95','> 95']
sizes = [range_1.shape[0],range_2.shape[0],range_3.shape[0],range_4.shape[0]]
explode = (0.05,0.05,0.05,0.05)
my_circle=plt.Circle((0,0),0.0,color='white')
plt.figure(figsize=(7,7))
plt.pie(sizes,labels=label_names,explode=explode,autopct='%1.1f%%',pctdistance=0.85,startangle=90,shadow=True)
fig=plt.gcf()
fig.gca().add_artist(my_circle)
labels= ['Ratings < 89', 'Ratings 90-92','Ratings 92-95','Ratings > 95']
plt.legend(labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()
````

The figure shows that 72% of the coffee brands are grouped in the category of 92-95 rating points. Then 17% are located in the 90-92 category. Finally, 2.5% corresponds to <89 points and 5.4% to >95 rating points.

![image](https://github.com/fernando-arancibia/Data-scrapping-Data-Analysis-and-Streamlit-dashboard-for-Coffee-Roaster-Review/assets/84011018/7bf5b3ca-0f37-4b85-badb-b6cfc13974d1)

To understand the proportion of coffee brands according to the rating, a histogram is created to see the distribution of the number of coffee brands according to the rating scale. 

````
plt.figure(figsize=(12,6))
sns.countplot(data=df,x='Rating')
plt.xlabel("\nRatting")
plt.ylabel("Numbers of Coffees")
plt.title("Distribution of Coffees in terms of Ratings \n")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
````

The figure shows that most of the coffee brands are evaluated between 92 and 95 rating points. The number of coffee brands between 92.0, 93.0, 94.0 rating classifications exceeds approximately one thousand brands.

![image](https://github.com/fernando-arancibia/Data-scrapping-Data-Analysis-and-Streamlit-dashboard-for-Coffee-Roaster-Review/assets/84011018/f5804bf3-91ea-44f2-89e8-dbc86062241b)


More analysis and visualizations can be found in the Jupiter notebook 
'Review_Cleaning_and_Descriptive_analisis.ipynb'
After finish the analysis of data a 'coffee_2.csv' file was created for build the streamlit app.

## Create a Dashboard with Streamlit. :bar_chart:

To create the streamlit app, is used the data 'coffee_2.csv' already analyzed in the previous process and created an interactive dashboard. 

For running the app the following libraies must be installed in your enviroment. 

````
import pandas as pd
import plotly.express as px
import streamlit as st
````
For activate the browser you have to tipe in the terminal or powershell:

````
streamlit run app.py
````
In this dashboard you can interact with the sidebar that allows you to select the Rating, Roast Grade and Coffee Roaster categories. 
With this selection, the number of brands of coffee per roaster company as well as the price of each coffee is visualized with bar graphs. 

![image](https://github.com/fernando-arancibia/Data-scrapping-Data-Analysis-and-Streamlit-dashboard-for-Coffee-Roaster-Review/assets/84011018/ec14bf89-4bf8-4327-a8f8-cd32f4289e50)

In addition, a map has been added where the location of the roasting company is displayed.

![image](https://github.com/fernando-arancibia/Data-scrapping-Data-Analysis-and-Streamlit-dashboard-for-Coffee-Roaster-Review/assets/84011018/12104a89-70a0-4fb7-9b79-edae8f21adf3)

All de code for the dashboard is in the app.py file


















