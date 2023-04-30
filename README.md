# Data scrapping, data analysis, and Streamlit dashboard for Coffee Roaster Review ☕


## Introduction.🪂

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
- Add location coordenates for coffee roaster with geopy
- Realize descriptive analisis of the information collected (RDA).
- Builts visualizations for understand the data obtained.

After finish the analysis of data a 'csv' file was created for build the streamlit app.

## Create a Dashboard with Streamlit. :bar_chart:

To create the streamlit app, we used the data already analyzed in the previous process and created an interactive dashboard. In this dashboard you can interact with the sidebar that allows you to select the Rating, Roast Grade and Coffee Roaster categories. 
With this selection, the number of brands of coffee per roaster company as well as the price of each coffee is visualized with bar graphs. In addition, a map has been added where the location of the roasting company is displayed.

### Percentage of coffees according to rating rank.

According to the information obtained from the web scrape it is observed that the cafes are classified by rating, so it is observed that there are four classifications according to the web page. Cafes with a rating higher than 95 rating points obtain 5.4% of the total. A percentage corresponding to 73.5% places the majority of the coffee shops in the range of 92 - 95 rating points. Cafes with 90 - 92 rating points have 18.9% and <89 points 2.1%.

![image](https://user-images.githubusercontent.com/84011018/182372164-ee8f1e9e-6cd9-4ea5-a00c-25b12f6a5de5.png)



### Distribution of coffees according to rating rank

To complement the information, it is observe the distribution of the coffee shops according to rating.
In this chart is posible to see the number of coffees and show that 500 hundred aprox. are in the rating of 93.0 points of rating,
arround 450 coffees are in the rating 94.0 points and 300 coffes aporx are in the category of 92.0. From 95.0 to 98.0 are 270 coffees.

![image](https://user-images.githubusercontent.com/84011018/182369503-350e7693-92d2-4d43-83b4-5eb5d471c117.png)

### Distribution of coffees according to roast level

Now considering the roasting level, it can be observed that the distribution is mostly made up of medium-light roasted coffees and below are the other classifications, so it is understood that the market or the consumer prefers this type of coffee.

![image](https://user-images.githubusercontent.com/84011018/182391439-e11c57be-db29-4918-9f3f-ed34db2facf4.png)

After this information, it is important to determine how many coffees found in the reviews correspond to each roasting level. It can be observed that about 1200 coffees correspond to the medium-light level. The levels corresponding to medium and light obtain a number of 300 to 200 coffees respectively. The medium-dark dark and very dark levels have a slight participation in the distribution.

![image](https://user-images.githubusercontent.com/84011018/182391345-ec2540b7-d78d-4a2e-9466-ef7ee25f7e6b.png)


### Top Companies in terms of Average Ratings

Taking the average of the coffee rating grouped for each roaster it is possible to obtain the roasting companies that obtain the highest rating on the basis of the reviews. the folowing table show the roaster companies and is respectively ranking

![image](https://user-images.githubusercontent.com/84011018/182383902-cf7d4e4f-7af3-45d8-819f-77d5359bf0fe.png)

Another interesting point to analyze is the number of brands of coffee produced by each roasting company. In the graph it can be observed that the first three companies have >100 brands of coffee represented. Then the other companies, starting from the fourth position, have <60 brands of coffee.

![image](https://user-images.githubusercontent.com/84011018/182386316-4a6c5d58-5961-496b-9d4a-0d0d7b47f698.png)

### Properties of Coffee

In terms of the classifications that stand out in the reviews such as aroma, flavor, body, acidity/structure and aftertaste, a clear pattern can be observed at the moment of classifying each property. The higher the classification, the higher the rating the coffee obtains.

![image](https://user-images.githubusercontent.com/84011018/182389208-04bd60bd-b775-48b3-9333-3760ec4caccc.png)
![image](https://user-images.githubusercontent.com/84011018/182389267-faa1d9a6-dace-4704-8fa5-a3198ab499d1.png)
![image](https://user-images.githubusercontent.com/84011018/182389312-7f5dec75-afe6-4c3f-bddf-7565b6deab81.png)
![image](https://user-images.githubusercontent.com/84011018/182389335-d1e6f351-3da9-4707-8ce6-d772229f8f49.png)

### Location

Grouping the information on the locations that produce the most coffee, it can be observed that the majority of the roasting companies are located in the United States according to the resensions.
The location that produces the most coffees with a number of 130 coffees is located in Madison, Wisconsin, followed by Chia-Yi in Taiwan with 118 and then Sacramento California with 77 coffee brands.

![image](https://user-images.githubusercontent.com/84011018/182395333-f57a03bb-c14a-4a2e-968c-a1c03dfeeb26.png)
















