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
st.write(
  "My name is Kai, I'm a junior and I join AI camp to take up some of my summer."
)
#Ava
st.write(
  "I'm Ava, I'm a sophomore and I joined AI camp to learn more about coding because it has always been an interesting subject to me. "
)
#Tyler
st.write(
  "Hi, I'm Tyler. I'm a rising junior and I joined AI camp to explore coding and if it could be an interesting career path."
)
#Sienna
st.write("Hi, I'm Sienna.")
#On Economic Freedom Index : Kai
st.title("Economic Freedom Index")
st.header("Introduction")
st.write(
  "The Economic Freedom Index is a measure that assesses the level of economic freedom and openness in a country. It takes into account factors such as the rule of law, property rights, government intervention, and trade freedom, providing a comparative analysis of economic environments worldwide."
)

st.subheader("Data Tables:")
st.dataframe(df)
st.dataframe(dfw)

st.markdown("<hr>", unsafe_allow_html=True)
# Kai
# What are countries with most and least economic freedom ?
st.title("Countries with Most and Least Economic Freedom")
st.header(
  "Hypothesis: What countries have the highest and lowest Economic Freedom Index?"
)
# Bar chart of index and top countries
kai = dfw.head(165)
sorted_dfw = kai.sort_values('Economic Freedom Summary Index', ascending=False)

n = 25
top_countries = sorted_dfw.head(n)

fig = px.bar(top_countries,
             x='Countries',
             y='Economic Freedom Summary Index',
             color='Economic Freedom Summary Index',
             title=f'Top {n} Countries by Index (2020)')

fig.update_yaxes(range=[7.5, 8.6])

st.plotly_chart(fig)

st.write(
  "The graph above shows the top 25 countries by the Economic Freedom Summary Index. The countries with the highest index are Hong Kong and Singapore, both small Asian nations with high economic development."
)

kai = dfw.head(165)
sorted_dfw = kai.sort_values('Economic Freedom Summary Index', ascending=False)
n = 25
bottom_countries = sorted_dfw.tail(n)

fig = px.bar(bottom_countries,
             x='Countries',
             y='Economic Freedom Summary Index',
             color='Economic Freedom Summary Index',
             title=f'Bottom {n} Countries by Index (2020)')

fig.update_yaxes(range=[3, 6])

st.plotly_chart(fig)

st.write(
  "The graph above shows the bottom 25 countries by the Economic Freedom Summary Index. The country with the lowest index is Venezuela, highly contributed to it's corruption in government and mismanagement of the country's economy."
)
#Does location affect the economic freedom summary index for countries ?
st.title("Relation Between Location and Index")
st.header(
  "Hypothesis: Does location affect the econonomic freedom index for countries?"
)
#Scatter Plots for index vs region
bar = dfw.head(165)

kai = px.scatter(bar,
                 x="Region",
                 y="Economic Freedom Summary Index",
                 color="Region",
                 title="EFSI vs Region (2020)")

st.plotly_chart(kai)

st.write(
  "The graph above shows the relation between the Economic Freedom Summary Index and the Region where a country lies. North America, Oceania, and Europe all have a relatively high index while countries in Africa and Latin America aren't as fortunate."
)
#Does economic freedom Quartile relate to region ?
st.title("Relation Between Location and Quartile")
st.header(
  "Hypothesis: Does economic freedom and a country's quartile relate to the region a country is in?"
)
#Pie Charts
kai = dfw.copy()

quartiles = kai['Quartile'].unique()  # 1,2,3,4

for quartile_val in quartiles:
  quartile_current = kai[kai['Quartile'] == quartile_val]
  quartile_counts = quartile_current.shape[0]

  region_count = quartile_current['Region'].value_counts().reset_index()
  region_count.columns = ['Region', 'Count']


  pieChart = px.pie(region_count,
                    values='Count',
                    names='Region',
                    title=f'Region Distribution in Quartile {quartile_val}')

  st.plotly_chart(pieChart)

st.write(
  "These four graphs show the Region distribution amongst the four quartiles. A majority of Quartile 1 is made up of European nations while Quartile 4 is made up of Africa, Latin America, and South Asia."
)

#Sienna

#What is the genral distribution of Economic Freedom Index?
st.title("Economic Freedom Index Distribution")
st.header(
  "Hypothesis: What is the general distribution of the Economic Freedom Index?"
)
#Histogram Plot of Economic Freedom Index
fig = px.histogram(df,
                   x="Economic Freedom Summary Index",
                   title="Histogram of Economic Freedom Summary Index")

st.plotly_chart(fig)

st.write(
  "This graph shows the distribution of the Economic Freedom Index throughout the 50 states in the US, plus Puerto Rico. This graph is heavily skewed right, with an average index of 6.15 and an outlier of 2.04 being Puerto Rico"
)
#Tyler
#How do Taxes relate to Economic Freedom Summary Index ?
st.title("How do taxes relate to the Economic Freedom Summary Index?")
st.header("Hypothesis: Do higher taxes relate to more economic freedom?")
#Scatter Plot of Taxes vs Index (Hue Quartile)
TIQ = dfw.head(165)
sorted_dfw = TIQ.sort_values("Economic Freedom Summary Index", ascending=False)

n = 100
top_tcountries = sorted_dfw.head(n)

st.plotly_chart(
  px.scatter(top_countries,
             x="Economic Freedom Summary Index",
             y="1D  Top marginal tax rate",
             hue="Quartile").update_layout(
               title='Scatter Plot',
               xaxis_title='Economic Freedom Summary Index',
               yaxis_title='1D Top marginal tax rate'))
st.write(
  "The chart shoes that the taxes do not directly correlate to a level of economic freedom. This means that there is more that effects the EFSI than just taxation."
)
#What is relation of taxes and Govt emloyment with Quartile.

#Bar chart of mean of taxes for each quartile.
#Bar chart of mean of Govt employment with quartile.
st.header("Hypothesis: Do taxes and govt. employment affect the quantile?")

TbQ = df.head()
sorted_df = TbQ.sort_values("Economic Freedom Summary Index", ascending=False)

n = 50
taxable_quantiles = sorted.df.head(n)

st.plotly_chart(
  px.bar(taxable_quantiles,
         x="Quantile",
         y="Taxes",
         hue="Economic Freedom Summary Index",
         title="Tax impact on quantiles of states"))

GovtQ = df.head()
sorted_df = GovtQ.sort_values("Economic Freedom Summary Index",
                              ascending=False)

n = 50
govt_employ = sorted.df.head(n)

st.plotly_chart(
  px.bar(govt_employ,
         x="Quantile",
         y="Government Employment",
         hue="Economic Freedom Summary Index",
         title="Government employ. effect on quantile of states"))
st.write(
  "As we can see in these two charts, the taxes and government employment do factor into the effective quantile a state is in. The charts show that the taxation has a larger impact on quantile than employment."
)

#Ava
# What are US states with most and least economic freedom ?
st.title("US States with Most and Least Economic Fredom")
st.header("Hypothesis: Which States Have The Most Economic Freedom?")
data1 = df.head(165)

sorted_df = data1.sort_values('Economic Freedom Summary Index',
                              ascending=False)

n = 10
top_states = sorted_df.head(n)

st.plotly_chart(
  px.bar(top_states,
         x='State/Province',
         y='Economic Freedom Summary Index',
         color='Economic Freedom Summary Index',
         title=f'Top {n} States by Index'))

st.write(
  "We can see from the bar graph that the states with the highest economic freedom are Florida, New Hampshire, and South Dakota"
)

st.header("Hypothesis: Which States Have The Least Economic Freedom?")

data1 = df.head(165)

sorted_df = data1.sort_values('Economic Freedom Summary Index', ascending=True)

n = 10
top_states = sorted_df.head(n)

st.plotly_chart(
  px.bar(top_states,
         x='State/Province',
         y='Economic Freedom Summary Index',
         color='Economic Freedom Summary Index',
         title=f'Bottom {n} States by Index'))

# Bar chart of index and top countries

st.header("Hypothesis: Which Countries Have The Highest Economic Freedom?")

data1 = dfw.head(165)

sorted_df = data1.sort_values('Economic Freedom Summary Index',
                              ascending=False)

n = 10
top_country = sorted_df.head(n)

st.plotly_chart(
  px.bar(top_country,
         x='Countries',
         y='Economic Freedom Summary Index',
         color='Economic Freedom Summary Index',
         title=f'Top {n} Countries by Index'))

# What is relation of Min Wage with Quartile?

st.header(
  "Hypothesis: What Is The Relation of Minimum Wage With Quartile in the US?")

mean_summary_index = df.groupby(
  'Quantile')['Minimum Wage Legislation'].mean().reset_index()

st.plotly_chart(
  px.bar(mean_summary_index,
         x='Quantile',
         y='Minimum Wage Legislation',
         color='Quantile',
         title='Minimum Wage Legislation by Quartile (1970 - 2020)'))

st.write(
  "Here we can see that Quartile 1 has the highest Minimum Wage Legislation.")
# Bar chart of taxes for each quartile.

st.heading("Hypothesis: Which Quartile in the US Has The Highest Taxes?")

mean_summary_index = df.groupby('Quantile')['Taxes'].mean().reset_index()

st.plotly_chart(
  px.bar(mean_summary_index,
         x='Quantile',
         y='Taxes',
         color='Quantile',
         title='Taxes by Quartile (1970 - 2020)'))

st.write("Quartile 1 has the highest taxes")

#Relation of Income claasification and quartile in the world ?
st.header("Hypothesis: How Does Income Classification Vary Between Quartiles?")

world1 = dfw

quartiles = world1["Quartile"].unique()  # 1,2,3,4

for quartile in quartiles:
  quartile_current = world1[world1['Quartile'] == quartile]

  quartile_counts = quartile_current.shape[0]

  income_count = quartile_current[
    'World Bank Current Income Classification, 1990-present '].value_counts(
    ).reset_index()
  income_count.columns = [
    'World Bank Current Income Classification, 1990-present', 'Count'
  ]

  #so it is not a float
  quartile = int(quartile)

  st.plotly_chart(
    px.pie(income_count,
           values='Count',
           names='World Bank Current Income Classification, 1990-present',
           title=f'Income Classification in Quantile {quartile}'))

#Conclusion : Ava
