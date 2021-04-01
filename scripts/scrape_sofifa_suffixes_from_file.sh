#!/bin/bash

echo '##### Calling: '`basename "$0"` '('$0')'

SCRIPT_PATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

### Verify the parsed variables
echo Verifying passed arguments

sofifa_base_url=$1
suffix_file_path=$2
file_name_prefix=$3
dest_dir=$4

if [[ -z ${sofifa_base_url} ]];
then
    echo "arg1 - Sofifa url is not set"
    exit 1
fi

if [[ -z ${suffix_file_path} ]];
then
    echo "arg2 - Suffix file path is not set"
    exit 1
fi

if [[ ! -f ${suffix_file_path} ]];
then
    echo "'${suffix_file_path}' is not a file." 
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

# Create a list of the suffixes
suffix_list=()
while read line; do
    echo "LINE: ${line}"
    suffix_list+=(${line})
done <"${suffix_file_path}"


for param in ${suffix_list[@]}; do
    full_url="${sofifa_base_url}${param}"
    echo "URL ${full_url}"

    file_path="${dest_dir}/${file_name_prefix}_id_${param}.html"

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

    echo "'${file_path}'        ->      '${full_url}'"     >> "${dest_dir}/SCRAPED_URLS.TXT"

    # Sleep before next try
    echo "Command: 'sleep 5'"
    sleep 5
done
