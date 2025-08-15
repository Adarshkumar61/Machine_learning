# Creating a Model of linear regression:
# we are using sonar csv file

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression #this is our model
from sklearn.metrics import accuracy_score

# importing data:
data = pd.read_csv('csv_files/Copy of sonar data.csv')

#splitting data for training:

x = data.drop(columns=60, axis= 1) #input
y = data[60] #output

#training data:

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.3, stratify= y, random_state= 2)

model = LinearRegression()

model.fit(x_train, y_train)

x_train_prediction = model.predict(x_train)
# accuracy = accuracy_score(x_train_prediction, y_train)

#now we will make a predictive system:

input_data = (np.random.uniform(0.001, 0.420, 60)) #(st, end(included), size)

#no changing input_data into numpy
input_data_as_numpy = np.asarray(input_data)

#reshaping numpy array:
reshaped_array = input_data_as_numpy.reshape(1, -1)
#- (1, -1) ka matlab hai ki hum array ko ek 2D array mein convert karna chahte hain, jismein:
# - Pehele dimension mein 1 sample hai
# - Dusre dimension mein utni hi features hain jitni ki zaroorat hai (is case mein, 60 features hain)
# - -1 ka matlab hai ki hum dusre dimension ki sankhya ko automatically calculate karne ke liye numpy ko bol rahe hain


prediction = model.predict(reshaped_array)
print(prediction)