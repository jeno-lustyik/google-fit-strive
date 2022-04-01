

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




st.write(' ####  Next, we explore three different classifiers')
image6 = Image.open('image6.png')
st.image(image6)
st.write(' ####  Figure 5. A graph of the Accuracy of three classifiesrs')
st.title('')



st.write(' ## Selected Classifier : SVM')
st.title('')
st.title('')

st.title('RESULTS AND DISCUSSIONS')
st.title('')
st.text('With the tuning of hyperparameters, our model could constantly provide around 80% accuracy.')


st.title('CONCLUSION')
st.write('## In Building the ML Model, the following Conclusion are made')
st.write('### 1. The Model works best with Random Forest Classifier with accuracy up to 80 %')
st.write('### 2. Four Features are enough to achieve this high accuracy')
st.title('')
st.title('')

model_svm = joblib.load('model.pkl')

gyr = st.number_input('Enter your gyroscope parameters:')
spd = st.number_input('Enter your speed:')
vol = st.number_input('Enter the volume of your surroundings:')
acc = st.number_input('Enter your accelerator parameters:')

st.text(model_svm.predict([[gyr, spd, vol, acc]]))

image10 = Image.open('image10.png')
st.image(image10)

