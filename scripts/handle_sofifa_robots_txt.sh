#!/bin/bash

echo '##### Calling: '`basename "$0"` '('$0')'

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

file_path=${dest_dir}/robots.txt

echo "Command: 'curl --fail -L -o "${file_path}" "${robots_url}"'"
curl --fail -L -o "${file_path}" "${robots_url}"
return_code=$?
if [[ $return_code -ne  0 ]];
then
    echo "*** Some Issues Found downloading the file"
    exit 1
fi
