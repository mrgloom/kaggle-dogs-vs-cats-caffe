import os
import sys

os.environ['GLOG_minloglevel'] = '2' 
caffe_root = '/media/myuser/120Gb/caffe-master/caffe/'  # parameter
sys.path.insert(0, caffe_root + 'python')

import caffe
import numpy as np


if len(sys.argv) != 3:
    print "Usage: python convert_mean.py mean.binaryproto mean.npy"
    sys.exit()


input_mean_binaryproto= sys.argv[1]
output_mean_npy= sys.argv[2]

blob = caffe.proto.caffe_pb2.BlobProto()
data = open( input_mean_binaryproto , 'rb' ).read()
blob.ParseFromString(data)
arr = np.array( caffe.io.blobproto_to_array(blob) )
out = arr[0]
np.save( output_mean_npy , out )
