import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


dato1 = np.array([""])
datos3d = np.array([[[1,2,3,4],[9,8,7,6]],[[4,3,2,1],[6,7,8,9]],[[4,5,6,7],[8,7,6,5]]])
datosNdim = np.array([1,2,3,4,5], ndmin=5)
a1d = np.random.randint(10,size=(4,10))
a2d = np.random.randint(10,size=(4,5))
a3d = np.random.randint(100,size=(4,4,4))
a4d = np.random.randint(25,size=(3,2,2,2,2,2))

## porperties of the Arrays
dimension = a1d.ndim
forma = a3d.shape
totalitems = a4d.size

## Slicing arrays
silce_1 = a3d[1:1,0:1,0:0]

for dato in a4d:
    print(dato,",")    
print(dimension,forma,totalitems)    

##contatenation of arrays 
## np.concatenate()
## np.vstack()
## np.hstack()
## Copying arrays 
a1_copy = a1d.copy()
a1_copy[0] = 25
print(np.hstack([a1d,a2d])) 
invertido = np.hstack([a1d,a2d])
dimesion2=invertido.size
## Reshape array needs to be same elements size
print(a1d,"\n",a2d)
print(dimesion2,invertido.shape)
print(invertido.reshape(10,6))

## random data distribution
##x = np.random.choice(data_array,p=[],size=(rows,columns,...n dimension))
## random permutation with pandas
permutado1=np.random.permutation(invertido)
test1 = np.random.normal(loc=10,scale=10,size=(1000))
##test2 = np.random.binomial(,)
test3 = np.random.poisson(lam=50,size=1000)
test4 = np.random.uniform(size=1000)
print("Shufled array :")
print(permutado1)
sns.kdeplot(test1,  label='normal')
sns.displot(test3,  label='Poisson')
sns.displot(test4)
plt.show()