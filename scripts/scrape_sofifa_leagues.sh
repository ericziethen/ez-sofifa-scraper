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
