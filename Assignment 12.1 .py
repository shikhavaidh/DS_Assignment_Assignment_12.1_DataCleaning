
# coding: utf-8

# In[256]:

#Assignment 13.1
#It happens all the time: someone gives you data containing malformed strings, Python, lists and missing data.
# How do you tidy it up so you can get on with the analysis? 
#Take this monstrosity as the DataFrame to use in the following puzzles: 
    #df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis', 
        #'Brussels_londOn'], FlightNumber': [10045, np.nan, 10065, np.nan, 10085], 
        #'RecentDelays': [[23,47],[],[24,43,87],[13],[67,32]],
        #'Airline':['KLM(!)','<Air France> (12)', '(British Airways. )',
        #'12. Air France', '"Swiss Air"']}) 
        
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#%matplotlib inline
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis', 'Brussels_londOn'], 'FlightNumber': [10045, np.nan, 10065, np.nan, 10085], 'RecentDelays': [[23,47],[],[24,43,87],[13],[67,32]],'Airline':['KLM(!)','<Air France> (12)', '(British Airways. )','12. Air France', '"Swiss Air"']})
df
#df['FlightNumber']=df['FlightNumber'][0], df['FlightNumber'][0] + 10, df['FlightNumber'][2], df['FlightNumber'][2] + 10, df['FlightNumber'][4]
df


# In[252]:

#1. Some values in the the FlightNumber column are missing. These numbers are meant to increase by 10 with each row so 
#10055 and 10075 need to be put in place. Fill in these missing numbers and make the 
#column an integer column (instead of a float column).

import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#%matplotlib inline
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis', 'Brussels_londOn'], 'FlightNumber': [10045, np.nan, 10065, np.nan, 10085], 'RecentDelays': [[23,47],[],[24,43,87],[13],[67,32]],'Airline':['KLM(!)','<Air France> (12)', '(British Airways. )','12. Air France', '"Swiss Air"']})


for i in range(0, len(df)):
    #df['FlightNumber'][i]
    if np.isnan(df['FlightNumber'][i]):
        df['FlightNumber'][i]=  df['FlightNumber'][i-1]+10
    else:
        df['FlightNumber'][i]        
df['FlightNumber']=df['FlightNumber'].astype(int)

df        


# In[253]:

#2. The From_To column would be better as two separate columns! Split each string on
#the underscore delimiter _ to give a new temporary DataFrame with the correct values.              
#Assign​ ​the​ ​correct​ ​column​ ​names​ ​to​ ​this​ ​temporary​ ​DataFrame. 
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#%matplotlib inline
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN', 'londON_StockhOlm', 'Budapest_PaRis', 'Brussels_londOn'], 'FlightNumber': [10045, np.nan, 10065, np.nan, 10085], 'RecentDelays': [[23,47],[],[24,43,87],[13],[67,32]],'Airline':['KLM(!)','<Air France> (12)', '(British Airways. )','12. Air France', '"Swiss Air"']})

df['From'], df['To'] = df['From_To'].str.split('_', 1).str#.title()

#3. Notice how the capitalisation of the city names is all mixed up in this temporary 
#DataFrame. Standardise the strings so that only the first letter is uppercase (e.g. "londON"​ ​should​ ​become​ ​"London".) 
df['From']=df['From'].str.title()
df['To']=df['To'].str.title()
df


# In[254]:

#4. Delete the From_To column from df and attach the temporary DataFrame from the previous​ ​questions. 
df.drop('From_To', axis=1, inplace=True)
df


# In[255]:

#5. In the RecentDelays column, the values have been entered into the DataFrame as a list. 
#We would like each first value in its own column, each second value in its own 
#column,​ ​and​ ​so​ ​on.​ ​If​ ​there​ ​isn't​ ​an​ ​Nth​ ​value,​ ​the​ ​value​ ​should​ ​be​ ​NaN. 


dfDelay =df['RecentDelays'].apply(lambda row: pd.Series(row))
dfDelay.columns = ['Delay 1', 'Delay 2', 'Delay 3']
dfDelay

#Expand the Series of lists into a DataFrame named delays, rename the columns delay_1,
#delay_2,​ ​etc.​ ​and​ ​replace​ ​the​ ​unwanted​ ​RecentDelays​ ​column​ ​in​ ​df​ ​with​ ​delays. 
 
dfNew = df.join(dfDelay)
dfNew.drop('RecentDelays', axis=1, inplace=True)

dfNew


# In[ ]:



