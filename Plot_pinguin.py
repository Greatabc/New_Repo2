import streamlit as st
import pandas as pd
import os
os.chdir('C:\\Users\\Sarwono\\PycharmProjects\\pythonProject1')
import streamlit as st
import pandas as pd
st.title("Palmer's Penguins")
#import our data
penguins_df = pd.read_csv('penguins.csv')
st.write(penguins_df.head())
print(os.getcwd())