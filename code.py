import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

df = pd.read_csv("github_dataset.csv")

st.title("GitHub stars v.s. contributors v.s. forks")
st.markdown("This interactive dashboard shows the relationship between stars_count, contributors, and forks_count. We can see the trend that more contributors, more fork counts. Moreover, when there are many fork counts and contributors in one project, the stars are usually high.")


col3, col4, col5 = st.columns(3)
with col3:
    chart = alt.Chart(df).mark_circle().encode(
        x='stars_count',
        y='forks_count',
        tooltip=['repositories', 'stars_count', 'forks_count']
    ).interactive()
    st.altair_chart(chart, use_container_width=True)

with col4:
    chart = alt.Chart(df).mark_circle().encode(
        x='contributors',
        y='stars_count',
        tooltip=['repositories', 'contributors', 'stars_count']
    ).interactive()
    st.altair_chart(chart, use_container_width=True)
with col5:
    chart = alt.Chart(df).mark_circle().encode(
        x='contributors',
        y='forks_count',
        tooltip=['repositories', 'contributors', 'forks_count']
    ).interactive()
    st.altair_chart(chart, use_container_width=True)

chart = alt.Chart(df).mark_circle().encode(
    x='contributors',
    y='forks_count',
    size='stars_count',
    color='stars_count',
    tooltip=['repositories', 'stars_count', 'forks_count', 'contributors']
).properties(
    width=600,
    height=400
)
st.altair_chart(chart, use_container_width=True)