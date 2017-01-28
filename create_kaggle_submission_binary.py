#https://github.com/BVLC/caffe/blob/master/python/caffe/classifier.py

#For each image in the test set predicts a probability that the image is a dog in [0,1] range (1 = dog, 0 = cat).

import numpy as np
import sys
import os

import usefull_utils

os.environ['GLOG_minloglevel'] = '2' 
caffe_root = '/media/myuser/120Gb/caffe-master/caffe/'  # parameter
sys.path.insert(0, caffe_root + 'python')
import caffe

if len(sys.argv) != 5:
    print "Usage: python create_kaggle_submission_probability.py deploy.prototxt model.caffemodel mean.npy <test_data_dir>"
    sys.exit()
    
DEPLOY_PROTOTXT= sys.argv[1] #deploy.prototxt
CAFFE_MODEL= sys.argv[2] #model.caffemodel
MEAN_FILE= sys.argv[3] #mean.npy
TEST_DATA_DIR= sys.argv[4]
MODEL_POSTFIX= CAFFE_MODEL.split(os.sep)[-2] # not safe way
BATCH_SIZE= 1 # edit it to fit your GPU memory

print "MODEL_POSTFIX", MODEL_POSTFIX

caffe.set_mode_gpu()
net = caffe.Classifier(DEPLOY_PROTOTXT, CAFFE_MODEL,
                       mean=np.load(MEAN_FILE).mean(1).mean(1),
                       channel_swap=(2,1,0),
                       raw_scale=255,
                       image_dims=(256, 256))

def predict_label(images_batch):    

    predictions = net.predict(images_batch)
    
    #0 is cat and 1 is dog
    batch_predictions= np.argmax(predictions, axis=1) #binary prediction
    
    batch_predictions= batch_predictions[..., np.newaxis]
    
    return batch_predictions
     
def write_array_kaggle_format(predictions):
    
    submission_dir= 'kaggle_data/submissions/'
    if not os.path.exists(submission_dir):
        os.makedirs(submission_dir)
        
    text_file = open(submission_dir+'kaggle_submit_binary_'+MODEL_POSTFIX+".csv", "w")
    #write header
    text_file.write('id,label\n')
        
    for i in range(0,predictions.shape[0]):
        text_file.write("%i,%i\n" % (i+1,predictions[i])) #write binary predictions

def load_batch(batch_filenames):
    images_batch=[]
    for filename in batch_filenames:
        input_image = caffe.io.load_image(filename)
        images_batch.append(input_image)
        
    return images_batch
    
def create_kaggle_submission(test_data_path):
    filenames= usefull_utils.GetAllFilesInDir(test_data_path, '.jpg')
    
    predictions= np.zeros((len(filenames), 1), dtype=np.uint8)
       
    #predict by batches
    for i in range(0,len(filenames),BATCH_SIZE):
        if(i+BATCH_SIZE < len(filenames)):
            #print i, i+BATCH_SIZE
            images_batch= load_batch(filenames[i:i+BATCH_SIZE])
            predictions[i:i+BATCH_SIZE]= predict_label(images_batch)
        else:
            bz= len(filenames)-i
            #print i, i+bz
            images_batch= load_batch(filenames[i:i+bz])
            predictions[i:i+bz]= predict_label(images_batch)
        
    write_array_kaggle_format(predictions)

#main  
create_kaggle_submission(TEST_DATA_DIR)
