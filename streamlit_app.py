import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import io

warnings.filterwarnings("ignore")
st.set_option('deprecation.showPyplotGlobalUse', False)

df = pd.read_csv("usa.csv")
dfw = pd.read_csv("world.csv")

st.write(df.head(1))

#Introduction : Agile Antelopes
st.header("Agile Antelopes")

#Kai

#Ava

#Tyler

#Sienna

#On Economic Freedom Index : Kai

# Kai
# What are countries with most and least economic freedom ?

# Bar chart of index and top countries

#Does location affect the economic freedom summary index for countries ?

#Scatter Plots for index vs region

#Does economic freedom Quartile relate to region ?
#Pie Charts

#Tyler
#How do Taxes relate to Economic Freedom Summary Index ?

#Scatter Plot of Taxes vs Index (Hue Quartile)

#What is relation of taxes and Govt emloyment with Quartile.

#Bar chart of mean of taxes for each quartile.
#Bar chart of mean of Govt employment with quartile.

#Sienna

#What is the genral distribution of Economic Freedom Index?

#Histogram Plot of Economic Freedom Index

#Ava
# What are US states with most and least economic freedom ?

# Bar chart of index and top countries

# What is relation of Min Wage with Quartile?

# Bar chart of taxes for each quartile.

#Relation of Income claasification and quartile in the world ?

#Pie plot for quartiles and income class

#Conclusion : Ava
