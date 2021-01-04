#!/bin/bash

echo '##### Calling: '`basename "$0"` '('$0')'

SCRIPT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

### Verify the parsed variables
echo Verifying passed arguments

sofifa_url=$1
offset_change=$2
file_name_prefix=$3
dest_dir=$4

if [[ -z ${sofifa_url} ]];
then
    echo "arg1 - Sofifa url is not set"
    exit 1
fi

if [[ -z ${offset_change} ]];
then
    echo "arg2 - offset change is not set"
    exit 1
fi

re='^[0-9]+$'
if ! [[ ${offset_change} =~ $re ]] ; then
   echo "error: '${offset_change}' is not a number"
   exit 1
fi

if [[ -z ${file_name_prefix} ]];
then
    echo "arg3 - file name prefix is not set"
    exit 1
fi

if [[ -z ${dest_dir} ]];
then
    echo "arg4 - Destination directory is not set"
    exit 1
fi

if [[ ! -d ${dest_dir} ]];
then
    echo "Directory '${dest_dir}' DOES NOT exist." 
    exit 1
fi

### Scrape URL
sofifa_url=$1
offset_change=$2
file_name_prefix=$3
dest_dir=$4

### Get the data
offset=0
while true; do
    full_url="${sofifa_url}&offset=${offset}"
    echo "${full_url}"

    file_path="${dest_dir}/${file_name_prefix}_offset_${offset}.html"

    echo "Command: 'curl --fail -L -o "${file_path}" "${full_url}"'"
    curl --fail -L -o "${file_path}" "${full_url}"
    return_code=$?
    echo "Return Code: ${return_code}"
    if [[ ${return_code} -ne  0 ]];
    then
        echo "*** Some Issues Found downloading the file"
        echo "Scrape Error: curl returned '${return_code}' for URL '${full_url}'" >> "${dest_dir}/SCRAPE_ERROR.TXT"
        exit 1
    fi

    # Increment the Offset
    offset=`expr ${offset} + ${offset_change}`  # Backticks - see http://alvinalexander.com/linux-unix/linux-shell-script-counter-math-addition-loop/
    echo "New Offset: ${offset}"

    # Check if any more to scrape
    echo "Command: 'grep -nwl 'file_path' -e "offset=${offset}"'"
    grep -nwl "${file_path}" -e "offset=${offset}"
    return_code=$?
    echo "Return Code: ${return_code}"
    if [[ ${return_code} -ne  0 ]];
    then
        echo "Stop Scraping, last page found, no problem"
        break
    fi

    # Sleep before next try
    echo "Command: 'sleep 5'"
    sleep 5

done
