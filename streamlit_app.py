from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

with st.echo(code_location='below'):
    st.text('This is some text.')
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)
        print(dataframe[dataframe.columns[0]])
        st.write(dataframe)
        st.line_chart(dataframe)
        st.area_chart(dataframe)
