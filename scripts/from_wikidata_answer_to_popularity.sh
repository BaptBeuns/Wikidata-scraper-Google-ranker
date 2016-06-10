INPUT_NAME=$1

while read LINE;
do
    # Gets the name of the celebrity
    URL=$(echo $LINE | awk -F "\"*,\"*" '{print $2}')
    PERSON=$(echo $LINE | awk -F "\"*,\"*" '{print $1}')
    SCORE=$(./scripts/get_google_score.py "$PERSON")
    # echo ${PERSON}
    echo ${PERSON}", "${SCORE}", "${URL};
done < ${INPUT_NAME}
# done < <(head -10 footballers.csv)
