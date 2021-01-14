import numpy as np

a = np.array([[1,2,3],[1,2,np.nan]])
b = np.array([[1,np.nan,3],[1,2,np.nan]])
x = np.nanmin(np.concatenate([a,b]),axis=0)

print(x)


#arr1 = np.random.randint(1,25,size=(5,5))

#a = arr1[0:1,1]
#b = arr1[1:2,2]
#c = arr1[2:3,3]
#d = arr1[3:4,4]

#print(arr1)
#print("\n")
#print(a)
#print(b)
#print(c)
#print(d)