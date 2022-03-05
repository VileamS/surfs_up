# surfs_up
Project overview
  An investor wants to learn more about the weather before committing to build a Surf and Ice Cream shop in Oahu, Hawaii. The investor's main concern is the precipitation forcing the shop to close too frequently. To analyze Hawaii's weather data, SQLAlchemy was used to query the SQLite database.
. Explain the structures, interactions, and types of data of a provided dataset.
. Differentiate between SQLite and PostgreSQL databases.
. Use SQLAlchemy to connect to and query a SQLite database.
. Use statistics like minimum, maximum, and average to analyze data.
Results
. June Statistics for the Temperature and Precipitation
. The mean temperature of 75°F for June is higher than the mean temperature of 71°F for December. However, the opposite is true for precipitation. December had the higher precipitation of .22 inches while June had .14 inches.
. Grouping the data into 15 bins, the histograms visually show how the frequency centers around the two different means. For consistency of the graphs, the ranges of the axes were generated as the same for easier comparison using the minimum and maximum numbers from the descriptive statistics. Using the same range for the temperatures, June appears to have a slight left skew, where December is more symmetrical.
Summary
  The investor's main concern was getting rained out too frequently. Comparing the June and December weather patterns, the temperatures and precipitation means are reasonably close. The temperature data is not strongly skewed for either month. The ratio of the temperatures to the precipitation for the two months is also reasonably similar with few outliers over 3 inches of precipitation. The data supports opening a Surf and Ice Cream shop year-round.
