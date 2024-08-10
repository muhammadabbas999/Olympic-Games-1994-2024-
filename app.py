



import pandas as pd
import streamlit as st
import plotly.express as px
import plotly as pt
# Set page configuration
st.set_page_config(page_title="Olympic Games 1994-2024", layout="centered")

# Title of the app
st.markdown("""
    <h1 style='text-align: center; color: #FFFFFF; font-family: Arial, sans-serif; font-size: 40px;'>Olympic Games 1994-2024</h1>
    """, unsafe_allow_html=True)

# Custom CSS for sidebar and text
st.markdown("""
    <style>
    .css-1d391kg { /* Sidebar background color */
        background-color: #13465F;
    }
    .css-1d391kg .css-1to83wi { /* Sidebar header color */
        color: white;
    }
    .css-1d391kg .css-1n14jix { /* Sidebar text color */
        color: white;
    }
    .css-1d391kg .css-1d9dfdk { /* Sidebar input text color */
        color: white;
    }
    h1, h2, h3, h4, h5, h6, .css-1v3fvcr {
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for filtering
st.sidebar.header("Please Filter Here")

# Dictionary to map the selection to the corresponding dataset
datasets = {
    "Lillehammer 1994": pd.read_csv("Lillehammer 1994.csv", encoding='ISO-8859-1'),
    "Atlanta 1996": pd.read_csv("Atlanta 1996.csv", encoding='ISO-8859-1'),
    "Nagano 1998": pd.read_csv("Nagano 1998.csv", encoding='ISO-8859-1'),
    "Sydney 2000": pd.read_csv("Sydney 2000.csv", encoding='ISO-8859-1'),
    "Salt Lake City 2002": pd.read_csv("SaltLakeCity 2002.csv", encoding='ISO-8859-1'),
    "Athens 2004": pd.read_csv("Athens 2004.csv", encoding='ISO-8859-1'),
    "Torino 2006": pd.read_csv("Torino 2006.csv", encoding='ISO-8859-1'),
    "Vancouver 2010": pd.read_csv("Vancouver 2010.csv", encoding='ISO-8859-1'),
    "London 2012": pd.read_csv("London 2012.csv", encoding='ISO-8859-1'),
    "Sochi 2014": pd.read_csv("Sochi 2014.csv", encoding='ISO-8859-1'),
    "Rio 2016": pd.read_csv("Rio 2016.csv", encoding='ISO-8859-1'),
    "PyeongChang 2018": pd.read_csv("PyeongChang 2018.csv", encoding='ISO-8859-1'),
    "Tokyo 2020": pd.read_csv("Tokyo 2020.csv", encoding='ISO-8859-1'),
    "Beijing 2022": pd.read_csv("beijing 2022.csv", encoding='ISO-8859-1'),
    "Paris 2024": pd.read_csv("Paris 2024.csv", encoding='ISO-8859-1')
}

# Dropdown menu for selecting the Olympic Games dataset
selected_game = st.sidebar.selectbox("Select Olympic Games", options=list(datasets.keys()))

# Load the selected dataset
df = datasets[selected_game]

# Radio buttons for selecting the type of medal
medal_type = st.sidebar.radio("Select Medal Type", ["Gold", "Silver", "Bronze"])

# Initialize a variable to hold the filtered data
if medal_type == "Gold":
    filtered_df = df[df['Gold'] > 0]
    # Create the bar chart for Gold medals
    fig = px.bar(filtered_df, x='NOC', y='Gold', color='NOC', text='Gold',color_discrete_sequence=px.colors.qualitative.Vivid)
    fig.update_layout(
     #   title_text=f"{selected_game}: Gold Medal Count by NOC",
        #title_font=dict(size=20, family='Arial, sans-serif', color='black'),
        xaxis_title='Countries',
        xaxis_title_font=dict(size=18, family='Arial, sans-serif', color='white'),
        yaxis_title='Gold Medals',
        yaxis_title_font=dict(size=18, family='Arial, sans-serif', color='white'),
        xaxis_tickfont=dict(size=12, family='Arial, sans-serif', color='white'),
        yaxis_tickfont=dict(size=12, family='Arial, sans-serif', color='white'),
        annotations=[
            dict(
                x=0.55,
                y=1.20,
                xref='paper',
                yref='paper',
                text=f"Hosting Country: {selected_game}",
                showarrow=False,
                font=dict(size=14, family='Arial, sans-serif', color='white'),
                align='left'
            )
        ]
    )
    fig.update_traces(textfont=dict(family='Arial, sans-serif', size=12, color='black'))
    st.plotly_chart(fig)

elif medal_type == "Silver":
    filtered_df = df[df['Silver'] > 0]
    # Create the bar chart for Silver medals
    fig = px.bar(filtered_df, x='NOC', y='Silver', color='NOC', text='Silver',color_discrete_sequence=px.colors.qualitative.Bold)
    fig.update_layout(
        #title_text=f"{selected_game}: Silver Medal Count by NOC",
        #title_font=dict(size=20, family='Arial, sans-serif', color='black'),
        xaxis_title='Countries',
        xaxis_title_font=dict(size=18, family='Arial, sans-serif', color='white'),
        yaxis_title='Silver Medals',
        yaxis_title_font=dict(size=18, family='Arial, sans-serif', color='white'),
        xaxis_tickfont=dict(size=12, family='Arial, sans-serif', color='white'),
        yaxis_tickfont=dict(size=12, family='Arial, sans-serif', color='white'),
        annotations=[
            dict(
                x=0.55,
                y=1.20,
                xref='paper',
                yref='paper',
                text=f"Hosting Country: {selected_game}",
                showarrow=False,
                font=dict(size=14, family='Arial, sans-serif', color='white'),
                align='left'
            )
        ]
    )
    fig.update_traces(textfont=dict(family='Arial, sans-serif', size=12, color='black'))
    st.plotly_chart(fig)

elif medal_type == "Bronze":
    filtered_df = df[df['Bronze'] > 0]
    # Create the bar chart for Bronze medals
    fig = px.bar(filtered_df, x='NOC', y='Bronze', color='NOC', text='Bronze',color_discrete_sequence=px.colors.qualitative.Set1)
    fig.update_layout(
      #  title_text=f"{selected_game}: Bronze Medal Count by NOC",
       # title_font=dict(size=20, family='Arial, sans-serif', color='black'),
        xaxis_title='Countries',
        xaxis_title_font=dict(size=18, family='Arial, sans-serif', color='white'),
        yaxis_title='Bronze Medals',
        yaxis_title_font=dict(size=18, family='Arial, sans-serif', color='white'),
        xaxis_tickfont=dict(size=12, family='Arial, sans-serif', color='white'),
        yaxis_tickfont=dict(size=12, family='Arial, sans-serif', color='white'),
        annotations=[
            dict(
                x=0.55,
                y=1.20,
                xref='paper',
                yref='paper',
                text=f"Hosting Country: {selected_game}",
                showarrow=False,
                font=dict(size=14, family='Arial, sans-serif', color='white'),
                align='right'
            )
        ]
    )
    fig.update_traces(textfont=dict(family='Arial, sans-serif', size=12, color='black'))
    st.plotly_chart(fig)

# Display the filtered DataFrame
#st.dataframe(filtered_df)
