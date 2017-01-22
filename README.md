`WORK IN PROGRESS`

Solutions for https://www.kaggle.com/c/dogs-vs-cats and https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition competition.

Here is table with results, but hyperparameters of neural nets can drastically affect accuracy, so if you know how to improve results let me know.

Name| Acc. test | finetuned Acc. test. | Train time | Forward pass time | On disk model size | Year | Paper
------------------ | --- | --- | --- | --- | --- | --- | ---
AlexNet | 93.65%  | 97.98% | **35m** | - | 227.5Mb | 2012 | [link](http://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)
SqeezeNet v1.1 | 92.46% | 98.87% | ~2h | -| **2.9Mb** | 2016 | [link](http://arxiv.org/pdf/1602.07360v3.pdf)
GoogLeNet | 94.62% | **99.58%** | 50m | - | 41.3Mb | 2014 | [link](http://www.cs.unc.edu/~wliu/papers/GoogLeNet.pdf)
VGG-16 | 96.51% | 99.40% | 5h20m | - | 537.1Mb | 2014 | [link](http://arxiv.org/pdf/1409.1556.pdf)
VGG-19 | **97.42%** | 99.48% | 25h50m | - | 558.3Mb | 2014 | [link](http://arxiv.org/pdf/1409.1556.pdf)
Network-In-Network | 93.65% | 98.49% | ~2h |-| 26.3Mb | 2014 | [link](http://arxiv.org/pdf/1312.4400v3.pdf)

Test accuracy measured on train-test split 80%-20%, maybe to achive better acuracy we can train on all available data.

1.learning_from_scratch is folder with models that were trained in NVIDIA DIGITS with Caffe backend.

2.finetuning is folder with models that were finetuned from models trained on ImageNet.

TODO:
data augmentation:
~~~
1. Create python layer
http://www.andrewjanowczyk.com/real-time-data-augmentation-using-nvidia-digits-python-layer/
Try to make it like in torch wrapper 
https://github.com/NVIDIA/DIGITS/issues/1034
2. Example for batch processing
https://github.com/choosehappy/public/blob/master/DL%20tutorial%20Code/common/step5_create_output_images_kfold.py
~~~

Tested on system with following configuration:
~~~~
Ubuntu version:

`lsb_release -a`

Ubuntu 14.04.4 LTS

`uname -a`

Linux myuser-computer 3.19.0-61-generic #69~14.04.1-Ubuntu SMP Thu Jun 9 09:09:13 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux

gcc version:

`gcc --version`

gcc (Ubuntu 4.8.4-2ubuntu1~14.04.3) 4.8.4

DIGITS version:

`./digits-devserver --version`

4.1-dev

Caffe version:

`git status`

branch caffe-0.15

`git log -n 1`

commit e638c0b1cb19afff50d830ce87cc1898f18568fd
Author: Sergei Nikolaev <snikolaev@nvidia.com>
Date:   Wed Aug 31 14:32:28 2016 -0700
Mark 0.15.13

CPU:

`cat /proc/cpuinfo | grep "model name"`

Intel(R) Core(TM)2 Duo CPU     E8500  @ 3.16GHz

GPU:

`nvidia-smi`

+-----------------------------------------------------------------------------+
| NVIDIA-SMI 367.44                 Driver Version: 367.44                    |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  GeForce GTX 1070    On   | 0000:01:00.0      On |                  N/A |
| 27%   38C    P8    10W / 151W |    150MiB /  8108MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
~~~



