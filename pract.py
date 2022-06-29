#importing libraries and a set of names (only single name)
import pandas as pd
import csv
import random
names = pd.read_csv('name_data.csv')

data= []

#creating random students data (triple name+ ID + three random grades)

for r in range (0,2000):
    list = []
    
    #creating first name
    
    x =  random.randint(0,6700)
    list.append(x)
    name1 = names.iloc[x,0]
    g1 = names.iloc[x,1]
    n = 0
    
    #creating the second name

    while n ==0:
        x = random.randint(0,6700)
        g2 =names.iloc[x,1]
        name2 = names.iloc[x,0]
        
        if g2== "boy":
            if x not in list:
                list.append(x)
                break
                
    #creating the last name
    while n==0:
        x = random.randint(0,6700)
        g3 = names.iloc[x,1]
        name3 = names.iloc[x,0]
      
        if g3== "boy":
            if x not in list:
                break
                    
    name = name1 + " " + name2 + " " + name3
    
    #creating the ID with format 2021-----
    
    l = 5-len(str(r+1))
    id = "2021" + "0"*l + str(r+1)
    
    #creating random values for each student
    
    r2 = str(random.randint(0,100))
    r3 = str(random.randint(0,100))
    r4 = str(random.randint(0,100))
    
    #appending on the data list
    
    data.append([name,g1,id,r2,r3,r4])
   
#conerting the data list into a dataframe

df = pd.DataFrame(data, columns=['Name', 'gender','id','G1','g2','g3'])

print(df)

# You can convert the dataframe to a CSV file by activating the following command
#df.to_csv("out.csv")