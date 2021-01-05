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

# Build up the Team Parameters

# Description taken from sofifa html directly
parameter_list=()
parameter_list+=("at")          # Attack
parameter_list+=("bd")          # Dribbling
parameter_list+=("bp")          # Passing
parameter_list+=("bps")         # Positioning
parameter_list+=("bs")          # Speed
parameter_list+=("cc")          # Crossing
parameter_list+=("cp")          # Passing
parameter_list+=("cps")         # Positioning
parameter_list+=("cs")          # Shooting
parameter_list+=("da")          # Aggression
parameter_list+=("dd")          # Defender Line
parameter_list+=("df")          # Defence
parameter_list+=("dm")          # Pressure
parameter_list+=("dp")          # Domestic Prestige
parameter_list+=("dw")          # Team Width
parameter_list+=("ip")          # International Prestige
parameter_list+=("md")          # Midfield
parameter_list+=("oa")          # Overall
parameter_list+=("ps")          # Players
parameter_list+=("sa")          # Starting XI Average Age
parameter_list+=("ta")          # Whole Team Average Age
parameter_list+=("tb")          # Transfer Budget
parameter_list+=("ti")          # ID

base_url="https://sofifa.com/teams?currency=EUR&units=mks"
full_url=${base_url}
param_url_pre_count="showCol%5B"
param_url_post_count="%5D"
param_count=0

for param in ${parameter_list[@]}; do
    #echo "Param Count: ${param_count} for param '${param}'"
    full_url="${full_url}&${param_url_pre_count}${param_count}${param_url_post_count}=${param}"

    param_count=`expr ${param_count} + 1`  # Backticks - see http://alvinalexander.com/linux-unix/linux-shell-script-counter-math-addition-loop/
done

echo ${full_url}

./scripts/scrape_sofifa_url.sh "${full_url}" 60 "TEAMS" "${dest_dir}"

# Return ok if we come that far
exit 0
