# SQLAlchemy-challenge

<img width="705" alt="Screen Shot 2024-05-04 at 11 19 55 AM" src="https://github.com/JelenaRaonic/sqlalchemy-challenge/assets/159960361/bf0ea55a-161d-4373-aa44-0f42080ec307">

### This project has 2 parts:
### Part1: Analyse and Explore Climate Data
a) Precipitation Analysis - by finding the most recent date in the dataset and using this date I look into previous 12 months of precipitation data by querying the previous 12 months of data. Loading the query results into Pandas DataFrame and plotting these results to get following image as well as to summuary statistics for the precipitation data.
![Figure1](https://github.com/JelenaRaonic/sqlalchemy-challenge/assets/159960361/681fbb33-7b3c-43dc-bad6-9fbc738ef9c0)

b) Station Analysis - designing query to calculate the total number of stations in the dataset and designing query to find most active station and calculate lowest, highest and average temperatures on the most active station. Last is to design a query to get the previous 12 months of temperature observation data (tobs) and plot the results in histogram with bins=12. The result is shown through this image.
![Figure2](https://github.com/JelenaRaonic/sqlalchemy-challenge/assets/159960361/fad77ef2-bf07-4a18-92a0-f69988b03772)

### Part2: Design Climate App
Here I design a Flask API besed on queries that I did in my prevous analysis.I created different roots and all of them work properly. Please when accessing last 2 routes start and end date should be inputed in proper format stated on homepage. By entering start date or start and end date you can get results with calculated min, avg and max for the given period. 

<img width="525" alt="Screen Shot 2024-05-07 at 12 41 27 PM" src="https://github.com/JelenaRaonic/sqlalchemy-challenge/assets/159960361/72576c47-7644-4421-aeee-44106cc53285">

This was interested project to work on, and I appreciate help from LA in the part API dynamic route - how to accept the dates as a paramenters from the URL. 



