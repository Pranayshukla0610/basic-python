
import pandas as pd
import numpy as np

a = pd.DataFrame()
a["Id"] = [1,2,3,4,5]
a["name"] = ["A","B","C","D","E"]
a["sex"] = ["M","F","F","F","M"]
a["age"] = [11,33,55,77,88]
a

b = pd. DataFrame()
b["Id"] = [2,3,4,5,6]
b["location"] = ["B","C","D","E","F"]
b["sex"] = ["M","F","F","F","M"]
b["height"] = [33,55,77,88,63]
b

a
b

Divya = pd.merge(a,b, on="Id",how= "outer",indicator=True)
Divya = pd.merge(a,b, on="sex",how= "outer",indicator=True)
Divya = pd.merge(a,b, on="Id",how= "outer",indicator=True)
Divya = pd.merge(a,b, on="sex",how= "outer",indicator=True)

a
a.drop(["sex","Id"], axis=1)
a

a.drop(a.columns[ [0,1] ],axis= 1)

data = pd.DataFrame()
data["name"] = ["A","B","C","D","E","F","G","H","I","J"]
data["age"] = [22,9,5,39,50,17,26,33,43,48]
data["sex"] = ["F","M","M","F","F","M","F","M","F","M"]
data

data["new"] = 1
data
data["new"] = np.where(data["age"]>=30, "old","young")
data

data["new"] = np.where( (  (data["age"]<30) &(data["sex"]=="M")),"Young M","Others")  
data

data["new"] = np.where( (  (data["age"]<30) & (data["sex"]=="M")),"Young",data["new"] )
data

data["new"] = np.where( ((data["age"]<30) & (data["sex"]=="F")),"Young F",data["new"] )
data    

data["new"] = np.where(((data["age"]>=30) & (data["sex"]=="F")),"Mature",data["new"])
data

data.loc[(data["age"]<30) & (data["sex"]=="F"),"GPT"] = "Young F"
data
data.loc[(data["age"]>=30) & (data["sex"]=="F"),"GPT"] = "Mature"
data

Sunny = data.copy()
Sunny     
     
data.columns.values[2] = "Sex"
data
data.rename(columns={"Sex":'Gender'},inplace=True)                       
data     
     
c = pd.DataFrame()
c["Id"] = [0,1,2,3,4,5,6,7,8,9]
c["name"] = ["A","B","C","D","E","F","G","H","I","J"]
c["sex"] = ["M","M","M","M","M","F","F","F","F","F"]  
c["age"] = [33,23,25,34,36,28,29,31,27,30] 
c  
     

data["new"] = np.where(data["age"] <30,"Young","Old")  
data  
     
import pandas as pd     
import numpy as np     

a["Id"] = [1,2,3,4,5]
a["name"] = ["A","B","C","D","E"]
a["sex"] = ["M","F","F","F","M"]
a["age"] = [11,33,35,77,88]
a


b["Id"] = [2,3,4,5,6]
b["name"] = ["B","C","D","E","F"]
b["location"] = ["Mumbai","Kanpur","Gurgaon","Kolkata","Delhi"]
b["sex"] = ["F","F","F","M","M"]
b


pd.merge(a,b,on="Id",how="outer",indicator="true")     
     
c= c.drop("age",axis=1)   
c 

c.drop(c.columns[[0,1]],axis=1)
     
c["new"] = np.where(c["age"]<30,"Young","old")     
c     

c["new"] = np.where( ( (c["age"]>=30)&(c["sex"] =="F") ),"Mature",c["new"])     
c     
c.loc(c["age"]<30) & (c.sex == "M"), "kane"      

c["gender"] = c["sex"].replace(["M","F"],["Male","Female"])     
c     

c.drop_duplicates(subset="sex")     
c.loc[c.duplicated(subset="sex")== True,]
c.sort_values(["age","sex"],ascending=[0,1])     

from pandasql import sqldf
pysqldf(""" select age,sex
            from c """   )    
            
data=pd.DataFrame()
data["name"] = ["A","B","C","D","E","F","G","H","I","J"]
data["sex"] = ["F","M","M","F","F","M","F","M","F","M"] 
data["age"] = [22,9,5,39,50,17,26,33,43,48]      
data    
     
data["new"] = np.where(data["age"] >=30,"old","young")    
data     

data["new"] =np.where( ( (data["age"] >=30 ) & (data["sex"]=="M")),"Old M","Others")    
data     

data["new"] = np.where( ((data["age"] <30) & (data["sex"]=="F")),"Young F","Others")     
data     

data["new"] = np.where( ((data["age"] >=30) & (data["sex"]=="F")),"Mature",data["new"])     
data     
data["new"] = np.where( ((data["age"] <30) & (data["sex"]=="M")),"Young M",data["new"])     
data     
data.drop("age",axis=1,inplace=True)     
data     
data.loc[(data.age <30) & (data.sex =="F"),"Romeo"] = "Young F"     
data     
data.loc[(data.age >=30) & (data.sex  =="F"),"Romeo"] = "Mature"     
data     
data.loc[(data.age <30) & (data.sex =="M"),"Romeo"] = "Young M"     
data     
data.loc[(data.age >=30) & (data.sex =="M"),"Romeo"] = "Old M"     
data     
data=data.drop("Romeo",axis=1)     
data     
     
data["Id"] = [1,2,3,4,5,6,7,8,9,10]
data["name"] = ["A","B","C","D","E","F","G","H","I","J"]
data[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]    