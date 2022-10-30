import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt


st.write("""
#  Heart Diseases Analysis 
""")

# Collects user input features into dataframe

def user_input_features():
    age = st.sidebar.number_input('Age: ')

    sex  = st.sidebar.selectbox('Sex of Patient',(0,1))
    cp = st.sidebar.selectbox('Chest pain type',(0,1,2,3))
    tres = st.sidebar.number_input('Blood Pressure ')
    chol = st.sidebar.number_input('Serum cholestoral in mg/dl: ')
    fbs = st.sidebar.number_input('blood sugar before breakfast ')
    res = st.sidebar.number_input('electrocardiographic results: ')
    tha = st.sidebar.number_input('Maximum heart rate  ')
    exa = st.sidebar.selectbox('Exercise induced angina: ',(0,1))
    slope = st.sidebar.number_input('The slope of the peak exercise ST segmen: ')
    ca = st.sidebar.selectbox('number of major vessels',(0,1,2,3))
    thal = st.sidebar.selectbox('thalassemia',(0,1,2))

    data = {'age': age,
            'sex': sex, 
            'cp': cp,
            'trestbps':tres,
            'chol': chol,
            'fbs': fbs,
            'restecg': res,
            'thalach':tha,
            'exang':exa,
            'slope':slope,
            'ca':ca,
            'thal':thal
                }
    features = pd.DataFrame(data, index=[0])
    return features
input_df = user_input_features()

heart_dataset = pd.read_csv("heart.csv")

alt_handle = alt.Chart(heart_dataset).mark_circle(size=60).encode(x='sex', y='age').interactive()
st.altair_chart(alt_handle)
st.write(""" #In the above graph, it can be said that in this dataset both males and females have
 equal chances of heart disease. But one observation which is unique from this dataset is that in the 
 age group of 70-80 for females, the chances of detection of heart diseases is low. """)


alt_handle=alt.Chart(heart_dataset).mark_point().encode(x="chol", y="sex").interactive()
st.altair_chart(alt_handle)

st.write(""" #In the above visualization, we can notice that males have usually high cholestrol levels 
as compared to females.As we can see from this dataset, there are some males whose cholestrol levels 
have exceeded 400 whereas for females, the maximum is around 350. """)


alt_handle=alt.Chart(heart_dataset).mark_point().encode(x="restecg",y="slope").interactive()
st.altair_chart(alt_handle)

alt_handle=alt.Chart(heart_dataset).mark_boxplot(extent='min-max').encode(
    x='age:O',
    y='fbs:Q'
)
st.altair_chart(alt_handle)
st.write(""" #In the above visualization, the condition is that if the fasting blood sugar is equal to
or above 120mg/dl,the fbs is indicated as 1 in the graph.So here we can see that apart from the age group 
range of 55-65, mostly patients have fasting blood sugar greater than 120mg/dl which 
significantly increases their chances of heart diseases. """)


alt_handle=alt.Chart(heart_dataset).transform_density(
    'chol',
    as_=['chol', 'restecg'],
    extent=[5, 50],
    groupby=['Sex']
).mark_area(orient='horizontal').encode(
    y='chol:Q',
    color='sex:N',
    x=alt.X(
        'exang:Q',
        stack='center',
        impute=None,
        title=None,
        axis=alt.Axis(labels=False, values=[0],grid=False, ticks=True),
    ),
    column=alt.Column(
        'ex:N',
        header=alt.Header(
            titleOrient='bottom',
            labelOrient='bottom',
            labelPadding=0,
        ),
    )
).properties(
    width=100
).configure_facet(
    spacing=0
).configure_view(
    stroke=None
)
st.altair_chart(alt_handle)

alt_handle=alt.Chart(heart_dataset).mark_circle(size=60).encode(
    x='chol',
    y='thalach',
    color='sex',
    tooltip=['age', 'sex', 'chol', 'thalach']
).interactive()
st.altair_chart(alt_handle)



alt.Chart(heart_dataset).mark_bar().encode(
    x='chol:O',
    y="trestbos:Q",
    # The highlight will be set on the result of a conditional statement
    color=alt.condition(
        alt.datum.year == 1810,  # If the year is 1810 this test returns True,
        alt.value('orange'),     # which sets the bar orange.
        alt.value('steelblue')   # And if it's not true it sets the bar steelblue.
    )
).properties(width=600)

st.write(""" #In the above visualization, we can notice that the maximum heart rate achieved is inversely
proportional to the age of the patient. With increasing age, heart rate decreases. It can also be 
inferred that in terms of heart rate, there are no significant differences between men and women. """)

# st.sel
























