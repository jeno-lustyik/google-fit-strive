

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import plotly.express as px
import joblib



image1 = Image.open('image1.PNG')
st.image(image1)
st.title('')
st.title('')


st.title('OVERVIEWS OF THE PROJECT')
st.write('####  1. Aims of the Project')
st.write('####  2. Data Exploration ')
st.write('####  3. Results and Discussions   ')
st.write('####  4. Conclusions')
st.title('')
st.title('')


st.title('AIMS OF THE PROJECT')
st.write(' ####  1. Build A light ML Model (Smart Phones,    Smart Watches,	   Other light electronic  devices')
st.write(' ####  2. ML Model must be Accurate ')
st.write(' ####  3. ML Model must be Fast ')
image2 = Image.open('image2.png')
st.image(image2)
st.title('')
st.title('')

st.title('DATA EXPLORATION')


st.write(' #### First, we determined the number of riginal Data vs Data with NaN values')
image3 = Image.open('image3.png')
st.image(image3)
st.write(' ####  Figure 1. A graph showing the Original Data vs Data with NaN values')
st.title('')
st.title('')




st.write(' #### Next, we examined the missing valuues as a function of all the features')
image4 = Image.open('image4.png')
st.image(image4)
st.write(' #### Figure 2. A graph showing the Number of missing values as a function of the features')
st.title('')
st.title('')



st.write(' ## How Balanced is the Data?')
image4_1 = Image.open('image4_1.png')
st.image(image4_1)
st.write(' #### Figure 3. A graph showing How balnced the original data is compared to Data with NaN')
st.title('')
st.title('')



st.title('FEATUREES SELECTION AND JUSTIFICATION')
st.write(' ####  Then we explored the mean of the various sensors as a function of the mode of transport')
image5 = Image.open('image5.png')
st.image(image5)
st.write(' ####  Figure 4. A graph showing the mean of the various sensors as a function of the mode of transport')


st.title('Selected Feactures')
st.write('#### 1. Linear Acceleration')
st.write('#### 2. Sound')
st.write('#### 3. Gyroscope')
st.write('#### 4. Speed')
st.title('')
st.title('')




# st.write(' ####  Next, we explore three different classifiers')
# image6 = Image.open('image6.png')
# st.image(image6)
# st.write(' ####  Figure 5. A graph of the Accuracy of three classifiesrs')
# st.title('')



st.write(' ## Selected Classifier : SVM')
st.title('')
st.title('')

st.title('RESULTS AND DISCUSSIONS')
st.title('')
st.text('With the tuning of hyperparameters, our model could constantly provide around 80% accuracy.')


st.title('CONCLUSION')
st.write('## In Building the ML Model, the following conclusions were made:')
st.write('### 1. Our model works best with SVC with accuracy of ~80 %')
st.write('### 2. Four Features were enough to achieve this accuracy')
st.title('')
st.title('')

model_svm = joblib.load('model.pkl')

gyr = st.slider('Enter your gyroscope parameters:', min_value=0, max_value=12)
spd = st.slider('Enter your speed:', min_value=0, max_value=40)
vol = st.slider('Enter the volume of your surroundings:', min_value=0, max_value=90)
acc = st.slider('Enter your accelerator parameters:', min_value=0, max_value=40)

st.subheader('The result:')
if model_svm.predict([[gyr, spd, vol, acc]]) == 0:
    st.text('You are travelling by bus.')
if model_svm.predict([[gyr, spd, vol, acc]]) == 1:
    st.text('You are travelling by car.')
if model_svm.predict([[gyr, spd, vol, acc]]) == 2:
        st.text('You are walking.')
if model_svm.predict([[gyr, spd, vol, acc]]) == 3:
    st.text('You are travelling by train.')
if model_svm.predict([[gyr, spd, vol, acc]]) == 4:
    st.text('You are standing still.')

image10 = Image.open('image10.png')
st.image(image10)

