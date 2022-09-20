import pandas
import streamlit
fruitlist=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruitlist=fruitlist.set_index('Fruit')
fruit_selected=streamlit.multiselect("pick some fruits:",list(fruitlist.index))
fruitshow=fruitlist.loc[fruit_selected]
streamlit.dataframe( fruitshow)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

