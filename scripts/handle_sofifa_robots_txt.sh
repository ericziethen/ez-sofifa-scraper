#!/bin/bash

echo '##### Calling: '`basename "$0"` '('$0')'

SCRIPT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

### Verify the parsed variables
dest_dir=$1

if [[ -z ${dest_dir} ]];
then
    echo "arg1 - Destination directory is not set"
    exit 1
fi

if [[ ! -d ${dest_dir} ]];
then
    echo "Directory '${dest_dir}' DOES NOT exist." 
    exit 1
fi

### Get the Robots File
robots_url=https://sofifa.com/robots.txt

echo "Command: ''"
${SCRIPT_PATH}/download_file.sh "${robots_url}" "${dest_dir}" "robots.txt"
return_code=$?
if [[ ${return_code} -ne  0 ]];
then
    echo "*** Some Issues Found downloading the file"
    exit ${return_code}
fi
