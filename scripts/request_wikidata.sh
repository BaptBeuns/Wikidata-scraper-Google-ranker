INPUT_NAME=$1
OUTPUT_NAME=$2

URL="https://query.wikidata.org/sparql?"

curl -s $URL$( python scripts/urlencode.py "$(cat $INPUT_NAME)" ) -H "Accept: text/csv" | sed "1d" > $2
