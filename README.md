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

















