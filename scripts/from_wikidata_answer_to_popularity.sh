INPUT_NAME=$1

while read LINE;
do
    # Gets the name of the celebrity
    URL=$(echo $LINE | awk -F "\"*,\"*" '{print $1}')
    PERSON=$(echo $LINE | awk -F "\"*,\"*" '{print $2}')
    SCORE=$(./scripts/get_google_score.py "$PERSON")
    echo "${SCORE},${URL},${PERSON}";
done < ${INPUT_NAME}
# done < <(head -10 footballers.csv)
