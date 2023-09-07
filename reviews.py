#Add imports to script
import pandas as pd

#open and read data file
df = pd.read_csv("data\winemag-data-130k-v2.csv", index_col=0)

#capturing country counts as series, converting into DataFrame  and renaming country cloumn to count
country_count = df.groupby('country')['country'].count().to_frame(name='count')
#capturing average points as series, converting into DataFrame  and rounding to 1 precision
avg_points = df.groupby('country').points.mean().round(1).to_frame()
#merging two DataFrames on country and sorting by count descending
wine_reviews = country_count.merge(avg_points, how='inner', on='country')\
    .sort_values(by = 'count',ascending= False).reset_index()
# saving to csv file in data folder
wine_reviews.to_csv('data/reviews-per-country.csv',index=False)



