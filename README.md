Solutions for https://www.kaggle.com/c/dogs-vs-cats competition.

1. learning_from_scratch is folder with models that were trained in NVIDIA DIGITS with Caffe backend.
Here is table with results, but hyperparameters of neural nets can drastically affect accuracy, so if you know how to improve results let me know.

Name| Acc. test | Acc. val. | Train time | Forward pass time | On disk model size | Year | Paper
------------------ | --- | --- | --- | --- | ---
AlexNet | | | | 2012 | [link]()
SqeezeNet v1.1 | 92.46% | - | 2h | -| 2.9Mb | 2016 | [link]()
GoogLeNet | | | | 2014 | [link]()
VGG-16 | | | | 2014 | [link]()
VGG-19 | | | | 2014 | [link]()
Network-In-Network | | | | 2014 | [link]()

All network models were trained for 30 epochs, batch size, learning rate, etc. can vary.



Tested on system with following configuration:

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




