import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('C:/Users/Dell/OneDrive/Desktop/app file/Main Deployment/lr_trained_model.sav', 'rb'))

input_data = (1,44,4,11,0,9.0,150,0,0,0,2)

# Changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# Reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
    print('Not Deprresed')
    
else:
    print('Depressed')