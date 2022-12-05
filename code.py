#impoer libraries
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
#____________________________________________
#load data
df=pd.read_csv('D:\\python project\\Child Mortality\\Child Mortality.csv')
#____________________________________________
#take a look
df.info()
df.isna().sum()
df.duplicated().sum()
df.describe()
#_________________________________________
#fix problems
df.set_index('Unnamed: 0')  # change index
df=df.drop(['Unnamed: 1','Unnamed: 0'],axis=1)  #drop usless columns
df=df.dropna()
df['Total Population']=df['Total Population']*1000   #fix population column
df['Mortality Rate\r']=df['Child Mortality(1 to 4)']/df['Total Population']  #add a new column
df=df.drop(df[df.Gender=='Total'].index) #drop usless rows
#_______________________
#Create a new table to analyze the data by gender separatelycreate a new data to anal
df=df.rename(columns={'Child Mortality(1 to 4)':'Child Mortality','Mortality Rate\r':'Mortality Rate'}) #change columns name
dfm=df[df['Gender']=='Male']  #make a new dataframe for male
dfm=dfm.rename(columns={'Child Mortality':'Male Mortality','Total Population':'Male Population','Mortality Rate':'Male Mortality Rate'}) #chnge names

dff=df[df['Gender']=='Female']  #make a new dataframe for female
dff=dff.rename(columns={'Child Mortality':'Female Mortality','Total Population':'Female Population','Mortality Rate':'Female Mortality Rate'})  #chnge names

dft=pd.merge(dfm,dff,on=['Country','Year'],how='outer')  #merge male and female dataframe
#______________________________
#a=pd.DataFrame(dft['Year'].value_counts().sort_values())
#plt.bar(x=a.index,y=a['Year'])
dft['Year'].value_counts().sort_values() #cheak year column
#_________________________
dft=dft[dft['Year']>1990] #slice data based on year column
dft['Country'].value_counts().sort_values() #cheak country column


dft['Country'] = dft['Country'].str.replace('\(.*?\)','') #fix country column

dft.to_csv('D:\\python project\\Child Mortality\\clean_Child_Mortality.csv') #save data

#____________________________

