import numpy as np

import usefull_utils

#main
submissions_dir= "/home/myuser/Desktop/CatsVsDogs/kaggle_data/submissions/"
filenames= usefull_utils.GetAllFilesInDir(submissions_dir, '.csv')

predictions_arr= np.zeros((len(filenames), 12500), np.float32)

for i in range(0,len(filenames)):
    arr= np.genfromtxt(filenames[i], delimiter=',', skip_header=1)
    predictions_arr[i,:] = arr[:,1]

avr_prediction= np.mean(predictions_arr, axis=0)

text_file = open(submissions_dir+'kaggle_submit_probability_avr.csv', "w")
    
#write header
text_file.write('id,label\n')
        
for i in range(0,avr_prediction.shape[0]):
    text_file.write("%i,%.4f\n" % (i+1,avr_prediction[i])) #probability that the image is a dog [0,1]
