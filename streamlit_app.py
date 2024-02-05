import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


"""
# My first app
Here's our first attempt at using data to create a table:
"""

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 5],
    'second column': [10, 20, 30, 50]
}))


# Title of the form
st.title('User Information Form')

# Using form and form submission button to group the inputs
with st.form(key='user_info_form'):
    name = st.text_input(label='Name')
    age = st.number_input(label='Age', min_value=0, max_value=100, step=1)
    birthday = st.date_input(label='Birthday')
    favorite_color = st.selectbox(label='Favorite Color', options=['Red', 'Green', 'Blue'])
    hobbies = st.multiselect(label='Hobbies', options=['Reading', 'Traveling', 'Cooking', 'Other'])
    
    # Form submit button
    submitted = st.form_submit_button('Submit')
    if submitted:
        st.write('Thank you for submitting the form.')
        # Process the data here (e.g., store it, send it somewhere, etc.)

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
