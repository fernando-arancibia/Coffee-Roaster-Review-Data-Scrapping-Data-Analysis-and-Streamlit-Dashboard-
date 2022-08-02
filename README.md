# Analysis of coffee brands reviews through web scraping


## Introduction

In the following data analysis project, information is extracted through the web scrapping method about reviews of different types of coffees that exist in the market. The main objective is to generate a data framework that allows to obtain information about how these reviews are structured to perform the classification of coffees.

## Objective

- Realize data collection with scrape method of relevant information about Coffee Market for diverses brand of coffees
- Built a data frame with the information selected.

## Methods

For this project the method used is data scraping, also known as web scraping, is the process of importing information from a website into a spreadsheet or local file saved on your computer. It’s one of the most efficient ways to get data from the web, and in some cases to channel that data to another website.
The module/tool used for scrape was Python and the librarie Beautifulsoup(bs4), Pandas for datamanipulation and seaborn for datavisualizations. 

The next step for the task was the following:

- Create the url to get the information using headers.
- Create a function for extract the links for scrappe coffee review.
- Create the function to extract the link.
- Testing the information scraped for complete the scrape process.

After this test all the reviews were extracted with a total of 1920 reviews for further analysis and create the data frame.
In this stage is analized the information for the scrapping proccess. for this task the following steps are performed in order to obtain a collection of data that is suitable for analysis:

- Clean and wrangling the information of the data frame ( create and drop columns, change currency for the prices of coffee).
- Realize descriptive analisis of the information collected (RDA).
- Builts visualizations were performed how is show in the next lines.

## RDA and Data Visualizations

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
















