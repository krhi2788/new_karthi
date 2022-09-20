import pandas
import streamlit
fruitlist=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe( fruitlist )
streamlit.multiselect("pcik some fruits:",list(fruitlist.index),['Avacado','Strawberries'])
