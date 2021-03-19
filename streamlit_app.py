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
        first = 0
        colCurrent = ''
        for col in dataframe.columns:
            if first == 0:
                print(col)
                colCurrent = col
            else:
                c = alt.Chart(dataframe).mark_bar().encode(x=colCurrent, y=col)
                st.altair_chart(c, use_container_width=True)
            first = first + 1
        # st.altair_chart(c, use_container_width=True)
        # c = alt.Chart(dataframe).mark_bar().encode(x='Sites', y=' Views')
        # st.altair_chart(c, use_container_width=True)
        # st.write(dataframe)
        # st.line_chart(dataframe)
        # st.area_chart(dataframe)
