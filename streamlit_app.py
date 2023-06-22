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
st.dataframe(df)
st.dataframe(dfw)
# Kai
# What are countries with most and least economic freedom ?
st.title("Countries with Most and Least Economic Freedom")
st.header("Hypothesis: What countries have the highest and lowest Economic Freedom Index?")
# Bar chart of index and top countries
kai = dfw.head(165)
sorted_dfw = kai.sort_values('Economic Freedom Summary Index', ascending=False)

n = 25
top_countries = sorted_dfw.head(n)

fig = px.bar(top_countries, x='Countries', y='Economic Freedom Summary Index', color='Economic Freedom Summary Index', title=f'Top {n} Countries by Index (2020)')

fig.update_yaxes(range=[7.5, 8.6])

st.plotly_chart(fig)
#Does location affect the economic freedom summary index for countries ?

#Scatter Plots for index vs region

#Does economic freedom Quartile relate to region ?
#Pie Charts

#Tyler
#How do Taxes relate to Economic Freedom Summary Index ?
st.title("How do taxes relate to the Economic Freedom Summary Index?")
st.header("Hypothesis: Do higher taxes relate to more economic freedom?")
#Scatter Plot of Taxes vs Index (Hue Quartile)
TIQ = dfw.head(165)
sorted_dfw = TIQ.sort_values("Economic Freedom Summary Index", ascending=False)

n=
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

st.plotly_chart(px.bar(top_states, x= 'State/Province', y='Economic Freedom Summary Index', color="Economic Freedom Summary Index"
             title=f'Bottom {n} States by Index'))




# Bar chart of index and top countries

st.header("Hypothesis: Which Countries Have The Highest Economic Freedom?")

data1 = wdf.head(165)

sorted_df = data1.sort_values('Economic Freedom Summary Index', ascending=False)

n = 10
top_country = sorted_df.head(n)

fig = st.plotly_chart(px.bar(top_country, x= 'Countries', y='Economic Freedom Summary Index', color='Economic Freedom Summary Index',
             title=f'Top {n} Countries by Index'))

fig.update_yaxes(range=[6.5,9])

fig.show()

# What is relation of Min Wage with Quartile?

# Bar chart of taxes for each quartile.

#Relation of Income claasification and quartile in the world ?

#Pie plot for quartiles and income class

#Conclusion : Ava
