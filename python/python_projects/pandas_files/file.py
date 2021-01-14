import os
import pandas as pd

main_folder = os.path.dirname(__file__)
df_file = os.path.join(main_folder,"italy-covid-daywise.csv")

main_fold = os.path.dirname(__file__)
location_file = os.path.join(main_fold,"locations.csv")

covid_df = pd.read_csv(df_file)

location_df = pd.read_csv(location_file)

#df_info = covid_df.info()
#print(covid_df.loc[243])
####

total_deaths = covid_df.new_deaths.sum()

new_death_cases = covid_df[covid_df.new_deaths > 500].copy()

#print(new_death_cases.info())

#covid_df["positive_rate"] = covid_df.new_cases / covid_df.new_tests
#######

#covid_df.at[143,"new_cases"] = (covid_df.at[142,"new_cases"]+
#                                covid_df.at[144,"new_cases"])/2
#print(covid_df.at[143,"new_cases"])
######

covid_df["date"] = pd.to_datetime(covid_df.date)

covid_df["year"] = pd.DatetimeIndex(covid_df.date).year
covid_df["month"] = pd.DatetimeIndex(covid_df.date).month
covid_df["day"] = pd.DatetimeIndex(covid_df.date).day
covid_df["weekday"] = pd.DatetimeIndex(covid_df.date).weekday

covid_df_february = covid_df[covid_df.month == 2]

covid_df_february_metrics =  covid_df_february[["new_cases","new_deaths","new_tests"]]

covid_df_february_totals = covid_df_february_metrics.sum()

print(covid_df_february_totals)


# mean of new cases for every day
for i in range(0,7):
    average_day = covid_df[covid_df.weekday == i].new_cases.mean()
    #print(average_day)
    
monthly_groups = covid_df.groupby("month")

#print(monthly_groups[["new_cases","new_deaths","new_tests"]].sum())

covid_df["total_cases"] = covid_df.new_cases.cumsum()
covid_df["total_deaths"] = covid_df.new_deaths.cumsum()
covid_df["total_tests"] = covid_df.new_tests.cumsum()

#print(covid_df)

#print(location_df)

location_df[location_df.location == "Chile"]

covid_df["location"] = "Chile"


merged_df = covid_df.merge(location_df,on="location")


merged_df["cases_per_million"] = merged_df.total_cases * 1e6 / merged_df.population
merged_df["deaths_per_million"] = merged_df.total_deaths * 1e6 / merged_df.population
merged_df["tests_per_million"] = merged_df.total_tests * 1e6 / merged_df.population



result_df = merged_df[['date',
                    'new_cases', 
                    'total_cases', 
                    'new_deaths', 
                    'total_deaths', 
                    'new_tests', 
                    'total_tests', 
                    'cases_per_million', 
                    'deaths_per_million', 
                    'tests_per_million']]

result_df.to_csv("results.csv",index=None)

print(merged_df)


