import os
import sys
import shutil
import numpy as np

import usefull_utils

#Iterate over all data and get prediction errors

os.environ['GLOG_minloglevel'] = '2' 
caffe_root = '/media/myuser/120Gb/caffe-master/caffe/'  # parameter
sys.path.insert(0, caffe_root + 'python')
import caffe

if len(sys.argv) != 6:
    print "Usage: python get_predition_errors.py deploy.prototxt model.caffemodel mean.npy <cat_data_folder> <dog_data_folder>"
    sys.exit()
    
DEPLOY_PROTOTXT = sys.argv[1] #deploy.prototxt
CAFFE_MODEL = sys.argv[2] #model.caffemodel
MEAN_FILE = sys.argv[3] #mean.npy
MODEL_POSTFIX= CAFFE_MODEL.split(os.sep)[-2] # not safe way
CAT_DATA_FOLDER= sys.argv[4]
DOG_DATA_FOLDER= sys.argv[5]

print "MODEL_POSTFIX", MODEL_POSTFIX

caffe.set_mode_gpu()
net = caffe.Classifier(DEPLOY_PROTOTXT, CAFFE_MODEL,
                       mean=np.load(MEAN_FILE).mean(1).mean(1),
                       channel_swap=(2,1,0),
                       raw_scale=255,
                       image_dims=(256, 256))
                       
def get_errors_in_cat_prediction(cat_data_folder):
    filenames= usefull_utils.GetAllFilesInDir(cat_data_folder, '.jpg')
    
    errors_directory= "cat_prediction_errors_"+MODEL_POSTFIX
    if not os.path.exists(errors_directory):
        os.makedirs(errors_directory)
    
    for filename in filenames:
        print filename
         
        input_image = caffe.io.load_image(filename)

        prediction = net.predict([input_image])
    
        #0 is cat and 1 is dog
        if(prediction[0].argmax()==1):
            shutil.copyfile(filename, os.path.join(errors_directory, filename.split(os.sep)[-1]))
    
def get_errors_in_dog_prediction(dog_data_folder):
    filenames= usefull_utils.GetAllFilesInDir(dog_data_folder, '.jpg')
    
    errors_directory= "dog_prediction_errors_"+MODEL_POSTFIX
    if not os.path.exists(errors_directory):
        os.makedirs(errors_directory)
    
    for filename in filenames:
        print filename
         
        input_image = caffe.io.load_image(filename)

        prediction = net.predict([input_image])
    
        #0 is cat and 1 is dog
        if(prediction[0].argmax()==0):
            shutil.copyfile(filename, os.path.join(errors_directory, filename.split(os.sep)[-1]))
            
#main
get_errors_in_cat_prediction(CAT_DATA_FOLDER)
get_errors_in_dog_prediction(DOG_DATA_FOLDER)

