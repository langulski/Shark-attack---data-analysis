import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import folium
import altair as alt
import seaborn as sns

from PIL import Image

image =  Image.open('images/1.jpg')
image1 =  Image.open('images/activity.png')
image2 =  Image.open('images/fatal.png')
image3 =  Image.open('images/years.png')
image4 =  Image.open('images/areas.gif')
header = st.container()
dataset = st.container()
feature = st.container()

# def read_markdown_file(markdown_file):
#     return Path(markdown_file).read_text()

# st.markdown(map. _repr_html_(), unsafe_allow_html=True)
# # from explore_page import show_page


# show_page()

txt = st.text_area('text',"A party of surfists are planning to surf overseas. They would love to surf in other countries seas, but they are afraid of being attacked by sharks or even worse, becoming their food. ;)For this we are going to help them decide what locations they should avoid surfing at.")



with header:
    st.image(image, caption='our brave surfists')

    st.title('Welcome to shark attacks data')
    st.text('this file contains some information about the attacks and location')
    st.write(txt)



with dataset:
    st.header(' 1.0 Mapping the attacks')

    df = pd.read_csv('attacks_with_loc.csv')
    st.write(df.head(5))
    

    latitude = 0 #location.latitude
    longitude = 0 #location.longitude
    
    df[["Longitude", "Latitude"]] = df[["Longitude", "Latitude"]].apply(pd.to_numeric)
    map_Sharks = folium.Map(location=[latitude, longitude], zoom_start=4)

# # add markers to map
# def createMap():
    
    df=df.rename(columns={"Longitude":"lon","Latitude":'lat'})


    st.map(df)



    df1 = pd.read_csv('attacks_cleaned.csv')


# fatals 
    st.header(' 1.1 Fatality')
    st.image(image2, caption='w')
    st.text('Checking the data from all the attacks,\n'
     'the chart shows that about 80% of all the attacks are non lethal.')


    fatal_plot = df1['Fatal'].value_counts()
    fig1, ax1 = plt.subplots()  
    fig1 = plt.gcf()
    fig1.set_size_inches(18.5, 10.5)
    ax1.pie(fatal_plot, labels=fatal_plot.index, autopct="%1.1f%%", shadow=False, startangle=90)
    plt.legend(fatal_plot.index, loc='upper left')
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)

    country_top10= df1.query('Country in ["USA","AUSTRALIA","SOUTH AFRICA","PAPUA NEW GUINEA","BRAZIL","BAHAMAS","NEW ZEALAND","MEXICO","REUNION","PHILIPPINES"]')
    fatality_rate = country_top10.groupby('Country').Fatal.apply(lambda x: (x == 'Yes').mean()).sort_values(ascending=True).nlargest(10)

    st.header(' 1.1.2 Fatality by country:')

    st.text('Although USA has the largest amount of attacks by sharks, comparing the death rate from the other contries, it is not the deadliest. Surprisely most of the attacks in Philipnes are deadly..')
    st.dataframe(df1['Country'].value_counts(normalize=True)[:10])

    fig, ax = plt.subplots()  
    fig = plt.gcf()
    fig.set_size_inches(15, 10.5)

    fatality_rate.plot(kind='bar')  
    st.pyplot(fig)


    st.header('2.2.2 top 10 deadliest activities')

    st.text('It seens most of the deadly attacks happened in boats\n'
    'surfing does not seen as deadly as it seemed')

    activity_death_rate = country_top10.groupby('Activity').Fatal.apply(lambda x: (x == 'Yes').mean()).sort_values(ascending=True).nlargest(10)

    fig3, ax = plt.subplots()  
    fig3 = plt.gcf()
    fig3.set_size_inches(15, 10.5)

    activity_death_rate.plot(kind='bar')  

    st.pyplot(fig3)  



    st.header('2.2 Activities:')
    st.image(image1, caption='w')
    st.text('most of the attacks happened while surfing or fishing\n'
    'this is not a good sign for our surfists')
    fig5, ax = plt.subplots()  
    fig5 = plt.gcf()
    fig5.set_size_inches(10, 8.5)
    pe= sns.countplot(y="Activity", data=df1, color="c")
    st.pyplot(fig5)  

    st.dataframe(df1['Activity'].value_counts(normalize=True)[:10])

    surfing_attack_rate = country_top10.groupby('Country').Activity.apply(lambda x: (x == 'surfing').mean()).sort_values(ascending=True).nlargest(10)
    st.header('top 10 countrie where most of the attacks happened while surfing')
    fig4, ax = plt.subplots()  
    fig4 = plt.gcf()
    fig4.set_size_inches(10, 8.5)
    surfing_attack_rate.plot(kind='bar')
    st.pyplot(fig4)

    # df1=df1[df1['Year']>2000]
    # fig5, ax = plt.subplots()  
    # fig5 = plt.gcf()
    # fig5.set_size_inches(10, 8.5)
    # pe= sns.countplot(y="Year", data=df1, color="c")
    # st.pyplot(fig5)  