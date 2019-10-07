# 1year_RON-EUR_exchange_rate
This program will generate a .csv file with the evolution of the RON/EUR exchange rate in one year

The websitewhere the data is scraped is : https://www.cursvalutar.ro

Using datetime library we obtain the current day month and year, than we get the date one year earlier.
With these two dates, we acces the url with the requested data and get the html code of the specified page.

In the table section of the code is the needed data.
All this data is collected, put into a data frame and filtered (keep only the day and the value of the exchange rate).

FInally, the dataframe is exported to a .csv file for further usage.

