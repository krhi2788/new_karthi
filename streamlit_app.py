import pandas
import streamlit
fruitlist=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruitlist=fruitlist.set_index('Fruit')
fruit_selected=streamlit.multiselect("pcik some fruits:",list(fruitlist.index),['Avacado','Strawberries'])
fruitshow=fruitlist.loc[fruit_selected]
streamlit.dataframe( fruit_selected )
