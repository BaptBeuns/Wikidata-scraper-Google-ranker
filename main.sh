INPUT_NAME=$1
OUTPUT_NAME=$2

NORMAL=$(tput sgr0)
GREEN=$(tput setaf 2; tput bold)
YELLOW=$(tput setaf 3)
RED=$(tput setaf 1; tput bold)

function error() {
    echo -e "$RED$*$NORMAL"
}

function success() {
    echo -e "$GREEN$*$NORMAL"
}

function info() {
    echo -e "$YELLOW$*$NORMAL"
}

if [ -z ${INPUT_NAME} ]
    then error "Please specify the path to a SPARQL script file."
    exit 1
fi
if [ -z ${OUTPUT_NAME} ]
    then error "Please specify an output file."
    exit 1
fi
if [ ! -e .api_key ]
    then error "Please use a Knowledge Search Graph API Key as file .api_key"
    exit 1
fi

info "Reading ${INPUT_NAME} to scrap Wikidata..."
TFILE="/tmp/$(basename $0).$$.tmp"
./scripts/request_wikidata.sh $INPUT_NAME ${TFILE}
info "Wikidata data written in ${TFILE}"

info "Associating Google score..."
echo "./scripts/get_google_score.py ${TFILE} ${OUTPUT_NAME} &"
./scripts/get_google_score.py ${TFILE} ${OUTPUT_NAME}

success "Google score of each personnality has been associated in ${OUTPUT_NAME}."

info "Sorting the personalities according to their Google score..."
sort -rt, -k2 -g ${OUTPUT_NAME} -o ${OUTPUT_NAME}
success "${OUTPUT_NAME} has been sorted."
