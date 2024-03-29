#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import plotly.express as px
from textblob import TextBlob


# In[2]:


pip install TextBlob


# In[3]:


import numpy as np
import pandas as pd
import plotly.express as px
from textblob import TextBlob


# In[6]:


import pandas as pd
df = pd.read_csv('netflix_titles.csv')
print(df)


# In[7]:


df.head()


# In[8]:


df.head()


# In[9]:


print(df.shape)


# In[10]:


print(df.columns)


# In[11]:


import plotly.express as px
z = df.groupby('rating').size().reset_index(name = 'count')
pieChart=px.pie(z, values = 'count', names =  'rating', title = 'Distribution of content rating on netflix',
                color_discrete_sequence = px.colors.qualitative.Set3)

pieChart.show()


# In[21]:


df['director'] = df['director'].fillna('No Director Specified')

filtered_directors = pd.DataFrame()
filtered_directors = df['director'].str.split(',' ,expand = True).stack()
filtered_directors = filtered_directors.to_frame()
filtered_directors.columns = ['Director']

directors = filtered_directors.groupby(['Director']).size().reset_index(name = 'Total Content')
directors = directors[directors.Director!= 'No Director Specified']
directors = directors.sort_values(by = ['Total Content'] , ascending = False)


directorsTop5 = directors.head()
directorsTop5 = directorsTop5.sort_values(by = ['Total Content'])



fig1 = px.bar(directorsTop5 , x = 'Total Content' , y = 'Director' ,title = 'Top 5 Directors on Netflix')

fig1.show()


# In[29]:


df['cast'] = df['cast'].fillna('No Cast Specified')
filtered_cast = pd.DataFrame()

filtered_cast = df['cast'].str.split(',' , expand = True).stack()

filtered_cast = filtered_cast.to_frame()

filtered_cast.columns = ['Actor']

actors = filtered_cast.groupby(['Actor']).size().reset_index(name = 'Total Content')
actors = actors[actors.Actor != 'No Cast Specified']
actors = actors.sort_values(by = ['Total Content'] , ascending = False)
actorsTop5 = actors.head()
actorsTop5 = actorsTop5.sort_values(by = ['Total Content'])


fig2 = px.bar(actorsTop5  , x = 'Total Content' , y= 'Actor' , title = 'Top 5 Actors on Netflix')

fig2.show()


# In[30]:



df1 = df[['type' , 'release_year']]
df1 = df1.rename(columns = {"release_year":"Release Year"})
df2 = df1.groupby(['Release Year' , 'type']).size().reset_index(name = 'Total Content')
df2 = df2[df2['Release Year']>=2010]

fig3 = px.line(df2 , x = "Release Year" , y = "Total Content", color = 'type' ,
               title = 'Trend of Content produced Over the years on Netflix')


fig3.show()


# In[31]:


dfx = df[['release_year' , 'description']]
dfx = dfx.rename(columns = {'release_year' : 'Release Year'})

for index , row in dfx.iterrows():
    z = row['description']
    testimonial = TextBlob(z)
    p = testimonial.sentiment.polarity
    if p==0:
        sent = "Neutral"
    elif p>0:
        sent = 'Positive'
    else :
        sent = 'Negative'
    
    dfx.loc[[index , 2] , 'Sentiment'] = sent
    
    

dfx = dfx.groupby(['Release Year' , 'Sentiment']).size().reset_index(name = 'Total Content')

dfx = dfx[dfx['Release Year']>=2015]

fig4 = px.bar(dfx , x = "Release Year" , y = "Total Content" , color = "Sentiment" , 
             title = "Sentiment of Content on Netflix")

fig4.show()


# In[ ]:




