import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.chdir('C:\\Users\\Sarwono\\PycharmProjects\\pythonProject1')


st.title('Plot of Pinguin')
st.markdown('$a^2=b^2+c^2+d^2$')
penguin_file = st.file_uploader('Select Your Local Penguins CSV (default provided)')
if penguin_file is not None:
  penguins_df = pd.read_csv(penguin_file)
else:
  penguins_df= pd.read_csv('penguins.csv')
df=pd.read_csv('penguins.csv')
# choose the gender of penguins

df=df.dropna()
st.write(df.head())
gender=st.selectbox('What gender from penguins?',['all','male','female'])
# if statement
if gender=='all':
  df=df
elif gender=='male':
  df=df[df['sex']=='male']
else:
  df=df[df['sex']=='female']

s_animal=st.selectbox('What animal you choose?', ['Adelie', 'Gentoo', 'Chinstrap'])

s_xaxis = st.selectbox('What do want the x variable to be?',
  ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
s_yaxis = st.selectbox('What about the y?',
  ['bill_depth_mm', 'bill_length_mm', 'flipper_length_mm', 'body_mass_g'])
markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap":'o'}
sns.set_style('darkgrid')
fig,ax=plt.subplots()
#df=df[df['species']==s_animal]
ax=sns.scatterplot(data = df,x=df[s_xaxis],y=df[s_yaxis],hue = 'species', markers = markers)
plt.xlabel(s_xaxis)
plt.ylabel(s_yaxis)
plt.title('Scattar plot of {} Penguins'.format(s_animal))
st.pyplot(fig)