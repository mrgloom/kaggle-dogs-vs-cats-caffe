BASE_FOLDER="learning_from_scratch"
echo "Base folder "$BASE_FOLDER
for item in `ls -v $BASE_FOLDER`
do
    echo "Convert "$item
    python convert_mean.py $BASE_FOLDER/$item/mean.binaryproto $BASE_FOLDER/$item/mean.npy
done

BASE_FOLDER="finetuning"
echo "Base folder "$BASE_FOLDER
for item in `ls -v $BASE_FOLDER`
do
    echo "Convert "$item
    python convert_mean.py $BASE_FOLDER/$item/mean.binaryproto $BASE_FOLDER/$item/mean.npy
done
