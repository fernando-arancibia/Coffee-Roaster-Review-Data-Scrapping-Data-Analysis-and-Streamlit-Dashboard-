# coffee review with scrapping method



Coffee Market Analisis for Top Rates doing Scrapping

Introduction

This project will attempt to analyze the Coffee Market according to the website coffeereview.com from the reviews of more of 1920 brand of coffees.

Objective

-Realize data collection with scrape method of relevant information about Coffee Market for brand of coffees
-Built a data frame with the information selected.

![image](https://user-images.githubusercontent.com/84011018/127627969-00805b3e-2141-4aca-b684-79bab29a53cc.png)

Methods

-For this project the method used is data scraping, also known as web scraping, is the process of importing information from a website into a spreadsheet or local file saved on your computer. It’s one of the most efficient ways to get data from the web, and in some cases to channel that data to another website.

![image](https://user-images.githubusercontent.com/84011018/127629459-6e7567ac-774e-405c-bc14-283275856932.png)
 
For this project the tool used for scrape was Python and the librarie Beautifulsoup(bs4). This was my general method for scraping data, using Google Chrome, looking for selector for the information needed. As an example the data needed for scrape is refer to the image below.

![image](https://user-images.githubusercontent.com/84011018/127628986-9befe917-d390-4db2-a9ac-5df55f32b77f.png)

The next step for the task was the following:

-Create the url to get the information using headers
-Create a function for extract the links for scrappe coffee review
-Create the function to extract the link
-Testing the information scraped for complete the scrape process.

In this step of testing was improve some task like checking the link for connect to the site, extracting one review for one link and some information like the name of coffee, roaster name and rating of review.

![image](https://user-images.githubusercontent.com/84011018/127633734-1453616d-737f-45b5-a7b3-ac9adf968cf0.png)

After this test all the reviews were extracted with a total of 1920 reviews for further analysis and create the data frame.

![image](https://user-images.githubusercontent.com/84011018/127634313-5f021b49-1bdb-4512-b313-e74d6bc7c9a6.png)

#### In this stage is analized the information for the scrapping proccess. for this task the following steps are performed in order to obtain a collection of data that is suitable for analysis:

#### -Clean and wrangling the information of the data frame ( create and drop columns, change currency for the prices of coffee)
#### -Realize descriptive analisis of the information collected (RDA)


After this stage builts visualizations were performed how is show in the next lines.

Count of coffees for rating

![image](https://user-images.githubusercontent.com/84011018/127635875-515da5ed-600c-46af-a40f-9ed2bb1b4a57.png)

In this chart is posible to see the number of coffees and show that 500 hundred aprox. are in the rating of 93.0 points of rating,
arround 450 coffees are in the rating 94.0 points and 300 coffes aporx are in the category of 92.0. From 95.0 to 98.0 are 270 coffees.

Then grouping the diferent coffees by roast level with five categories that are shows below

![image](https://user-images.githubusercontent.com/84011018/127637354-7ac884b9-ff9a-414c-bfd2-944851f27c50.png)

In the next chart is show the count of coffees by roast level showing showing that arround 1200 coffees are in the classsfication of medium-Light Level
and light and medium roast are arround 200 values.

![image](https://user-images.githubusercontent.com/84011018/127638362-166543e7-9c5c-4366-9044-3f658a878bcd.png)

Then is analized the features of the coofees among them considered acidity, body and aftertaste. about this features is possible to see
the cooffes with roast level medium-dark has a punctuaction of 9.0 points of 10.0 for body feature and acidity.
Similar values are shoes for Medium roast level but in aftertaste feature has the higher cualification with 8.0 points of 10.0

![image](https://user-images.githubusercontent.com/84011018/127638572-969ac3b7-e1a1-4999-be90-e80f4c486c77.png)

![image](https://user-images.githubusercontent.com/84011018/127638938-a96176d2-f436-4429-a936-cb9db4577cd4.png)

![image](https://user-images.githubusercontent.com/84011018/127638660-e8321619-14ed-4dad-abde-26d9e69e0f31.png)

For last is showing the number of coffees brands for  Roaster company and is posible to see that tree roaster companies are in top with an ammount upper of one hundreds coffee brands. 

![image](https://user-images.githubusercontent.com/84011018/127639240-dcc62276-9343-4989-b350-ceab394752b5.png)

For more information about this topic you can see the followiing links

https://github.com/Gungogit/coffee_review
https://public.tableau.com/app/profile/fernando4052


















