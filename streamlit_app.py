import pandas
import streamlit
fruitlist=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruitlist=fruitlist.set_index('Fruit')
streamlit.multiselect("pcik some fruits:",list(fruitlist.index))
streamlit.dataframe( fruitlist )
