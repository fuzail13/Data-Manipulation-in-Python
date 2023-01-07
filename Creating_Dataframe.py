import numpy as np
import pandas as pd

#First Way
data = np.random.random(size=(5,3))
print(data)

#Creating DataFrame by Second Way
df = pd.DataFrame(data=data, columns=["A","B","C"])
print(df)

#Creating DataFrame by dictionary - Third Way

df= pd.DataFrame(data={"A":[1,2,3],"B":["John","Alex","Lucy"]})
print(df)

#Creating Structured DataFrame Array

dtype = [("A",np.int),("B",(np.str,20))]
data = np.array([(1,"John"),(2,"Alex"),(3,"Lucy")], dtype=dtype)
print(data)
print(dtype)

data = [{"A":1,"B":"John"},{"A":2,"B":"Alex"},{"A":3,"B":"Lucy"}]
df = pd.DataFrame(data)
print(df)