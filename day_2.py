import matplotlib as mpl
import numpy as np
import pandas as pd
import sklearn as sk
import statsmodels as sm

list = [2, 3, 4, 5]

# Task: Add 1 to each number in a list


def addone(list):
    """Option 1: Create an empty list and append each value + 1 from the old list"""
    new_list = []
    for l in list:
        new_list.append(l + 1)

    return new_list


new = addone(list)

print(new)

# Alternative:
def add_one(x):
    """Directly pasting in the same list.
    More efficient when working with big data, because
    the allocated space is already there."""
    for i, value in enumerate(x):
        x[i] = value + 1
    return x


# Third option:
list = [l + 1 for l in list]
print(list)


# Arrays

list2 = [4,3,2,1]
x1 = np.array(list)
x2 = np.array(list2)

x1 + x2

# Generate array
np.arange(1,10)

# Add a "linear space" -> equally spread values between values
np.linspace(0,10,15)  # Add .astype(int) if you don't want floats

# Generate random numbers
np.random.normal(100, 5, 100).astype(int)

# Add the next number to a list
list = [1,2,3,5,6,2]

def addrange(list):
    addition = np.arange(1, len(list) + 1)
    l_as_array = np.array(list)
    new = addition + l_as_array

    return new

addrange(list)

## Prettier solution from other student: 
def addrange(list):
    newlist = np.array([i+1 for i in range(len(list))])
    return newlist+np.array(list)

addrange(list)

# Get every third object
list[::3]

# Check which elements meet a criteria -> masking with boolean arrays
x = np.array(list)
mask = x <= 3
x[mask]
x[x == 2]  # Can also be done directly

## Replace within the list based on criteria
x[x < 2] = 0
x

# Check mean
np.mean(x)
x.mean() #  Works both ways

# Missing values
x[x == 0] = np.nan()

x = np.array([3, 5, np.nan, 3, 2])
x.mean() # by default NaN is not omitted, so mean with nan is not possible

# How to omit NaNs
## Solution 1: filter put NaNs
x[~np.isnan(x)].mean()

## Solution 2: NaN-friendly functions
np.nanmean(x)  # Also possible for other math ops like sum, median, diff, etc.


# Exercise 12
vector = np.random.normal(100, 50, 100)
x = [2, 3, 4, 1, 3, 4, 8510, -102247, 2]
def drop_outlier(vector):
    """ Replaces values that are superior or inferior to 3*SD by NaN """
    vector = np.array(vector).astype(float)
    sd = np.nanstd(vector) * 3
    mean = np.nanstd(vector)
    vector[(mean - sd > vector) | (vector > mean + sd)] = np.nan

    return vector

drop_outlier(x)

def describe(vector):
    """ Return a string with the mean, SD, and number of outliers """
    mean = np.nanmean(vector)
    sd = np.nanstd(vector)
    outliers = len(vector[np.isnan(vector)])

    return str(f'Mean: {mean}, SD: {sd}, Outliers: {outliers}')

describe(vector)

### For pretty printing: np.round(x, 2)


# Dataframes
data = {"x1": [1, 2, 3], "x2": [6, 5, 4], "x3": ["A", "A", "B"]}
data = pd.DataFrame(data)
data

# If you extract just one column it outputs a series instead of df
data['x1']
# You can get around this by calling it as a list inside of the list:
data[['x1']]  # No difference for me, check later!

# Call index
data.index
data.index = range(2,5)  # Changes the index, can also be changed to letters etc

# Location to filter
data.loc[data['x1'] >= 2]
data.loc[0:2] # Dependent on self-set index
data.iloc[0:2] # Uses the indexed order independent of indivualised names of the indeces

# Read csvs into Pandas
df = pd.read_csv('iris.csv')
df.head()

# Check how many unique values there are in a column (function from numpy)
df['Species'].unique()

# Describe function
df.describe()
df['Species'].describe()

# Plotting
df.plot.hist(subplots = True)  # Allows separate histograms
df.plot.hist(bins = 100, alpha = 0.5)  # Allows better overview of overlap in one histogram

df.plot.scatter(x = 'Sepal.Length', y = 'Sepal.Width')
