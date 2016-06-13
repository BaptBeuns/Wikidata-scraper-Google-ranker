INPUT_NAME=$1

while read LINE;
do
    # Gets the name of the celebrity
    PERSON=$(echo $LINE | awk -F "\"*,\"*" '{print $1}')
    SCORE_URL=$(./scripts/get_google_score.py "$PERSON")
    echo ${PERSON}", "${SCORE_URL};
done < ${INPUT_NAME}
# done < <(head -10 footballers.csv)
