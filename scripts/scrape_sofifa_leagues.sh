#!/bin/bash

echo '##### Calling: '`basename "$0"` '('$0')'

SCRIPT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

### Verify the parsed variables
teams_html_dir=$1
dest_dir=$2

if [[ -z ${teams_html_dir} ]];
then
    echo "arg1 - Teams HTML directory is not set"
    exit 1
fi

if [[ ! -d ${teams_html_dir} ]];
then
    echo "Directory '${teams_html_dir}' DOES NOT exist." 
    exit 1
fi

if [[ -z ${dest_dir} ]];
then
    echo "arg2 - Destination directory is not set"
    exit 1
fi

if [[ ! -d ${dest_dir} ]];
then
    echo "Directory '${dest_dir}' DOES NOT exist." 
    exit 1
fi

# Create a list of leagues
league_file_name=LEAGUE_IDS.txt
league_file_path=${teams_html_dir}/${league_file_name}
pushd "${teams_html_dir}"
echo "CURRENT PATH: $PWD"
grep -a -h -o "/teams?lg=[0-9]*" *.html | sort --unique | sed 's/\/teams?lg=//g' > "${league_file_name}"
popd

# Scrape the File suffixes
./scripts/scrape_sofifa_suffixes_from_file.sh "https://sofifa.com/teams?lg=" "${league_file_path}" "LEAGUE" "${dest_dir}"

# Return ok if we come that far
exit 0
