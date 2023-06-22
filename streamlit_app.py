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


#Introduction : Agile Antelopes
st.title("Agile Antelopes")

#Kai
st.write("My name is Kai")
#Ava
st.write("I'm Ava, ")
#Tyler
st.write("Hi, I'm Tyler.")
#Sienna
st.write("sienna")
#On Economic Freedom Index : Kai
st.title("Economic Freedom Index")
st.header("Introduction")
st.write("The Economic Freedom Index is a measure that assesses the level of economic freedom and openness in a country. It takes into account factors such as the rule of law, property rights, government intervention, and trade freedom, providing a comparative analysis of economic environments worldwide.")

st.subheader("Data Tables:")
df.head(5)
dfw.head(5)
# Kai
# What are countries with most and least economic freedom ?

# Bar chart of index and top countries

#Does location affect the economic freedom summary index for countries ?

#Scatter Plots for index vs region

#Does economic freedom Quartile relate to region ?
#Pie Charts

#Tyler
#How do Taxes relate to Economic Freedom Summary Index ?
st.title("How do taxes relate to the Economic Freedom Summary Index?")
st.header("Hypothesis: Do higher taxes relate to more economic freedom?")
#Scatter Plot of Taxes vs Index (Hue Quartile)

#What is relation of taxes and Govt emloyment with Quartile.

#Bar chart of mean of taxes for each quartile.
#Bar chart of mean of Govt employment with quartile.

#Sienna

#What is the genral distribution of Economic Freedom Index?

#Histogram Plot of Economic Freedom Index

#Ava
# What are US states with most and least economic freedom ?
st.title("US States with Most and Least Economic Fredom")
st.header("Hypothesis: Which States Have The Most Economic Freedom?")
data1 = df.head(165)

sorted_df = data1.sort_values('Economic Freedom Summary Index', ascending=False)

n = 10
top_states = sorted_df.head(n)

fig = st.plotly_chart(px.bar(top_states, x= 'State/Province', y='Economic Freedom Summary Index', color='Economic Freedom Summary Index',
             title=f'Top {n} States by Index'))

fig.update_yaxes(range=[6,8])

fig.show()

st.header("Hypothesis: Which States Have The Least Economic Freedom?")

data1 = df.head(165)

sorted_df = data1.sort_values('Economic Freedom Summary Index', ascending=True)

n = 10
top_states = sorted_df.head(n)

fig = st.plotly_chart(px.bar(top_states, x= 'State/Province', y='Economic Freedom Summary Index', color='Economic Freedom Summary Index',
             title=f'Bottom {n} States by Index'))

fig.update_yaxes(range=[2,6])

fig.show()

# Bar chart of index and top countries

# What is relation of Min Wage with Quartile?

# Bar chart of taxes for each quartile.

#Relation of Income claasification and quartile in the world ?

#Pie plot for quartiles and income class

#Conclusion : Ava
