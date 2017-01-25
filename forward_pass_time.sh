CAFFE_BASE_DIR="/media/myuser/120Gb/caffe-master/caffe"

BASE_FOLDER="learning_from_scratch"
echo "Base folder "$BASE_FOLDER
for item in `ls -v $BASE_FOLDER`
do
    echo "Network: "$item
    $CAFFE_BASE_DIR/build/tools/caffe time --model=$BASE_FOLDER/$item/deploy.prototxt --gpu=0
done

BASE_FOLDER="finetuning"
echo "Base folder "$BASE_FOLDER
for item in `ls -v $BASE_FOLDER`
do
    echo "Network: "$item
    $CAFFE_BASE_DIR/build/tools/caffe time --model=$BASE_FOLDER/$item/deploy.prototxt --gpu=0
done
