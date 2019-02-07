import numpy as np
arr = np.arange(12)
#arr: array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])

arr.shape

arr.reshape((4,3), order='C')   # row major (default)

arr1 = np.array([[1,2], [3,4]])
arr2 = np.array([[5,6], [7,8]])
np.concatenate([arr1, arr2], axis = 0)   # row bind (default)


x = np.array([[1,2],[3,4],[5,6]])
y = np.array([0,1])
  #add y to each row of x      x + y:   array([[1, 3],[3, 5],[5, 7]])
  
#important method or attributes of pandas dataframe: 
# unique, values, groupby, apply
pd.unique(df['fruit'])
df['count'].values

df = pd.DataFrame({'key': ['a', 'b', 'c'] * 4,
                   'value': np.arange(12)})
g = df.groupby('key').value
g.mean()

#df columns and index assignment
df = pd.DataFrame(np.random.randn(4, 3), columns=list('bde'),index=['Utah', 'Ohio', 'Texas', 'Oregon'])
df
f = lambda x: x.max() - x.min()   # anonymous function
df.apply(f)     # default 0 or 'index'
df.apply(f, axis='columns')

#Reference:  Wes Mckinney, Python for Data Analysis, O'Reilly (2012).
