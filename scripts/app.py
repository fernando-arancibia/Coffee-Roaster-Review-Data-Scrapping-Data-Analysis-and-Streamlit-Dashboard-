#%%
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Coffee Review Dashboard',
                   page_icon=':bar_chart:',
                   layout='wide'
                   )

# import csv file
df=pd.read_csv('C:/Users/far/OneDrive/Escritorio/coffee_2.csv', index_col=[0])


#######SIDEBAR#######

st.sidebar.header('Please Filter Here:')
rating = st.sidebar.multiselect(
    'Select Rating:',
    options=df['Rating'].unique()
)

st.sidebar.header('Please Filter Here:')
roast = st.sidebar.multiselect(
    'Select the Roast Grade:',
    options=df['Roast'].unique()
)


st.sidebar.header('Please Filter Here:')
roaster = st.sidebar.multiselect(
    'Select the Roaster name:',
    options=df['Roaster'].unique()
   
)


df_selection = df.query('Rating == @rating & Roast == @roast & Roaster == @roaster')

#st.dataframe(df_selection)
st.title(':bar_chart: Coffee Dashboard')
st.markdown('##')

####KPI#####

coffee_brand = (df_selection['Name'].count())
avg_rating = round(df_selection['Rating'].mean(), 1)
# roast = (df_selection['Roast'])
star_rating = ':star:' 
coffee = ':teapot:' 
#euro = ':euro:'

left_column, middle_column = st.columns(2)
with left_column:
    st.subheader('Coffee brands:')
    st.subheader(f'{coffee_brand} {coffee}')
with middle_column:
    st.subheader('Average Ratting:')
    st.subheader(f'{avg_rating} {star_rating}')
# with right_column:
#     st.subheader('Roast Grade:')
#     st.subheader(f'{roast}')

st.markdown('---')


#coffee_by_roaster = df_selection['Roaster'].value_counts().sort_values(ascending=False)

coffee_by_roaster = (df_selection.groupby(by=['Roaster']).count().sort_values(by=['Name'], ascending=True).round(decimals = 3))

fig_coffee_by_roaster= px.bar(
    coffee_by_roaster,
    x='Name',
    y= coffee_by_roaster.index,
    orientation='h',
    title='<b>Coffee Brands by Roaster Company<b>',
    color_discrete_sequence=['#0083b8'] * len(coffee_by_roaster),
    labels= {'Name': 'Coffee Brands (units)'},
    template='plotly_white',
)



price_by_coffee = (df_selection.groupby(by=['Name']).mean().sort_values(by=['euro/gr'], ascending=True))

fig_price_by_coffee= px.bar(
    price_by_coffee,
    x='euro/gr',
    y= price_by_coffee.index,
    orientation='h',
    title='<b>Price_by_Coffee<b>',
    color_discrete_sequence=['#0083b8'] * len(price_by_coffee),
    labels= {'Name': 'Coffee Name'},
    template='plotly_white',
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_coffee_by_roaster, use_container_widht=True)
right_column.plotly_chart(fig_price_by_coffee, use_container_width=True)

st.markdown('---')

st.title(':world_map: Coffee Roaster Location')
st.map(df_selection)