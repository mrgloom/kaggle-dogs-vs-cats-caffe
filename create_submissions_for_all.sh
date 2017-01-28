BASE_FOLDER="finetuning" #BASE_FOLDER="learning_from_scratch"
echo "Base folder "$BASE_FOLDER
for item in `ls -v $BASE_FOLDER`
do
    echo "Create submission for: "$item
    time python create_kaggle_submission_probability.py $BASE_FOLDER/$item/deploy.prototxt $BASE_FOLDER/$item/model.caffemodel $BASE_FOLDER/$item/mean.npy /home/myuser/Desktop/CatsVsDogs/kaggle_data/test
done
