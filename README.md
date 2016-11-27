Solutions for https://www.kaggle.com/c/dogs-vs-cats competition.

1.learning_from_scratch is folder with models that were trained in NVIDIA DIGITS with Caffe backend.

Here is table with results, but hyperparameters of neural nets can drastically affect accuracy, so if you know how to improve results let me know.

Name| Acc. test | Acc. val. | Train time | Forward pass time | On disk model size | Year | Paper
------------------ | --- | --- | --- | --- | --- | --- | ---
AlexNet | 93.65%  | - | **35m** | - | 227.5Mb | 2012 | [link](papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)
SqeezeNet v1.1 | 92.46% | - | ~2h | -| **2.9Mb** | 2016 | [link](arxiv.org/pdf/1602.07360v3.pdf)
GoogLeNet | 94.62% | - | 50m | - | 41.3Mb | 2014 | [link](www.cs.unc.edu/~wliu/papers/GoogLeNet.pdf)
VGG-16 | 96.51% | - | 5h20m | - | 537.1Mb | 2014 | [link](arxiv.org/pdf/1409.1556.pdf)
VGG-19 | **97.42%** | - | 25h50m | - | 558.3Mb | 2014 | [link](arxiv.org/pdf/1409.1556.pdf)
Network-In-Network | 93.22% | - | ~2h |-| 26.3Mb | 2014 | [link](arxiv.org/pdf/1312.4400v3.pdf)

  All network models were trained for 30 epochs, but batch size, learning rate, etc. can vary. Also note for example for VGG-19 model sufficient accuracy(~97%) achived after 6 epochs, so in real life you need to train network shorter\longer than 30 epochs. 
  Test accuracy measured on train-test split 80%-20%, maybe to achive better acuracy we can train on all available data.
  Validation accuracy measured on Kaggle leaderboard.

More models to test:
~~~
1. Train ResNet from scratch.
https://github.com/beniz/deepdetect/tree/master/templates/caffe
https://github.com/jay-mahadeokar/pynetbuilder/tree/master/models/imagenet
https://github.com/ducha-aiki/caffenet-benchmark

resnet
try this
https://github.com/lfrdm/Masterarbeit/blob/master/train_val-residual-small.prototxt
from thread
https://github.com/KaimingHe/deep-residual-networks/issues/6
~~~

2.finetuning is folder with models that were finetuned from models trained on ImageNet.

Name| Acc. test | Acc. val. | Train time | Forward pass time | On disk model size | Year | Paper
------------------ | --- | --- | --- | --- | --- | --- | ---
AlexNet | 97.98%  | - | **35m** | - | 227.5Mb | 2012 | [link](papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)
SqeezeNet v1.1 | - | - | ~2h | -| **2.9Mb** | 2016 | [link](arxiv.org/pdf/1602.07360v3.pdf)
GoogLeNet | - | - | 50m | - | 41.3Mb | 2014 | [link](www.cs.unc.edu/~wliu/papers/GoogLeNet.pdf)
VGG-16 | 99.40% | - | 5h20m | - | 537.1Mb | 2014 | [link](arxiv.org/pdf/1409.1556.pdf)
VGG-19 | - | - | 25h50m | - | 558.3Mb | 2014 | [link](arxiv.org/pdf/1409.1556.pdf)
Network-In-Network | - | - | ~2h |-| 26.3Mb | 2014 | [link](arxiv.org/pdf/1312.4400v3.pdf)

TODO:
data augmentation:
~~~
1. Create python layer
http://www.andrewjanowczyk.com/real-time-data-augmentation-using-nvidia-digits-python-layer/
Try to make it like in torch wrapper 
https://github.com/NVIDIA/DIGITS/issues/1034
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



