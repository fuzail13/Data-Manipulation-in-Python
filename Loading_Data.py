import numpy as np
import pandas as pd
import pickle

filepath = 'D:\Data Manipulation in Python\P87-S2-Dataset-Basics-Resources'
filename = 'heart.csv'
picklefile = 'D:\\Data Manipulation in Python\\P87-S2-Dataset-Basics-Resources\\heart.pkl'
file = filepath +"\\"+ filename

df = pd.read_csv(file)
print(df)
#It will return only top 5 rows.
print(df.head())

#For 2D Array.
data = np.loadtxt(file,delimiter=",",skiprows=1)
print(data)

#For Numpy Structured Array
data = np.genfromtxt(file,delimiter=",",dtype=None,names=True,encoding="utf-8-sig")
print(data)

#Printing the datatype of each & every columns.
print(data.dtype)

#Manual Loading

def loading_file(file):
    with open(file,encoding="utf-8-sig") as f:
        data, cols = [],[]
        for i, line in enumerate(f.read().splitlines()):
            if i == 0:
                cols += line.split(",")
            else:
                data.append([float(x) for x in line.split(",")])
        df = pd.DataFrame(data, columns=cols)
    return df
print(loading_file(file))

df = pd.read_pickle(picklefile)
print(df.head())




