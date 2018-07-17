import pandas as pd

beers = pd.DataFrame.from_csv("beers.csv")
breweries = pd.DataFrame.from_csv("breweries.csv")

#merging the two datasets
beers_and_breweries = pd.merge(beers, 
                               breweries, 
                               how='inner', 
                               left_on="brewery_id", 
                               right_on="id", 
                               sort=True,
                               suffixes=('_beer', '_brewery'))

#listing the variable types
beers.dtypes

#function that will determine the category of each column
def get_var_category(series):
    unique_count = series.nunique(dropna=False)
    total_count = len(series)
    if pd.api.types.is_numeric_dtype(series):
        return 'Numerical'
    elif pd.api.types.is_datetime64_dtype(series):
        return 'Date'
    elif unique_count==total_count:
        return 'Text (Unique)'
    else:
        return 'Categorical'

def print_categories(df):
    for column_name in df.columns:
        print(column_name, ": ", get_var_category(df[column_name]))
        
print_categories(beers)
print_categories(breweries)

#count the number of observations
length = len(beers["ibu"])
print(length)

#count the number of non-null observations
count = beers["ibu"].count()
print(count)

number_of_missing_values = length - count
pct_of_missing_values = float(number_of_missing_values / length)
pct_of_missing_values = "{0:.1f}%".format(pct_of_missing_values*100)
print(pct_of_missing_values)

#finding the min, max, mode, mean, median value across a variable
print("Minimum value: ", beers["ibu"].min())
print("Maximum value: ", beers["ibu"].max())
print(beers["ibu"].mode())
mean = beers["ibu"].mean()
median = beers["ibu"].median()
standarddev = beers["ibu"].std()
quantile = beers["ibu"].quantile([.25, .5, .75])

#distributioon plots
import seaborn as sns
sns.set(color_codes=True)
sns.set_palette(sns.color_palette("muted"))

sns.distplot(beers["ibu"].dropna());

#calculating the pearson coefficient
beers[["abv", "ibu", "ounces"]].corr()

#describes the text data
beers[["name", "style"]].describe()

#dataset profiling
import pandas_profiling 

pandas_profiling.ProfileReport(beers_and_breweries) 
print (ProfileReport)




















