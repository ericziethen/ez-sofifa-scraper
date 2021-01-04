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

# Build up the Player Parameters

# Description taken from sofifa html directly
parameter_list=()
parameter_list+=("ac")          # Acceleration
parameter_list+=("ae")          # Age
parameter_list+=("ag")          # Agility
parameter_list+=("ar")          # Aggression
parameter_list+=("aw")          # Attacking Work Rate
parameter_list+=("ba")          # Balance
parameter_list+=("bl")          # Ball Control
parameter_list+=("bo")          # Best Overall
parameter_list+=("bp")          # Best Position
parameter_list+=("bs")          # Base Stats
parameter_list+=("cm")          # Composure
parameter_list+=("cr")          # Crossing
parameter_list+=("cu")          # Curve
parameter_list+=("def")         # DEF
parameter_list+=("dr")          # Dribbling
parameter_list+=("dri")         # DRI
parameter_list+=("dw")          # Defensive Work Rate
parameter_list+=("fi")          # Finishing
parameter_list+=("fr")          # FK Accuracy
parameter_list+=("gc")          # GK Kicking
parameter_list+=("gd")          # GK Diving
parameter_list+=("gh")          # GK Handling
parameter_list+=("gp")          # GK Positioning
parameter_list+=("gr")          # GK Reflexes
parameter_list+=("gu")          # Growth
parameter_list+=("he")          # Heading Accuracy
parameter_list+=("hi")          # Height
parameter_list+=("in")          # Interceptions
parameter_list+=("ir")          # International Reputation
parameter_list+=("jt")          # Joined
parameter_list+=("ju")          # Jumping
parameter_list+=("le")          # Loan Date End
parameter_list+=("ln")          # Long Shots
parameter_list+=("lo")          # Long Passing
parameter_list+=("ma")          # Marking
parameter_list+=("oa")          # Overall Rating
parameter_list+=("pac")         # PAC
parameter_list+=("pas")         # PAS
parameter_list+=("pe")          # Penalties
parameter_list+=("pf")          # Preferred Foot
parameter_list+=("phy")         # PHY
parameter_list+=("pi")          # ID
parameter_list+=("po")          # Positioning
parameter_list+=("pt")          # Potential
parameter_list+=("rc")          # Release Clause
parameter_list+=("re")          # Reactions
parameter_list+=("sa")          # Standing Tackle
parameter_list+=("sh")          # Short Passing
parameter_list+=("sho")         # SHO
parameter_list+=("sk")          # Skill Moves
parameter_list+=("sl")          # Sliding Tackle
parameter_list+=("so")          # Shot Power
parameter_list+=("sp")          # Sprint Speed
parameter_list+=("sr")          # Strength
parameter_list+=("st")          # Stamina
parameter_list+=("ta")          # Total Attacking
parameter_list+=("td")          # Total Defending
parameter_list+=("te")          # Total Mentality
parameter_list+=("tg")          # Total Goalkeeping
parameter_list+=("to")          # Total Movement
parameter_list+=("tp")          # Total Power
parameter_list+=("ts")          # Total Skill
parameter_list+=("tt")          # Total Stats
parameter_list+=("vi")          # Vision
parameter_list+=("vl")          # Value
parameter_list+=("vo")          # Volleys
parameter_list+=("wg")          # Wage
parameter_list+=("wi")          # Weight
parameter_list+=("wk")          # Weak Foot

base_url="https://sofifa.com/?col=pi&sort=desc"
full_url=${base_url}
param_url_pre_count="showCol%5B"
param_url_post_count="%5D="
param_count=0

for param in ${parameter_list[@]}; do
    #echo "Param Count: ${param_count} for param '${param}'"
    full_url="${full_url}&${param_url_pre_count}${param_count}${param_url_post_count}${param}"

    param_count=`expr ${param_count} + 1`  # Backticks - see http://alvinalexander.com/linux-unix/linux-shell-script-counter-math-addition-loop/
done

# Set Currency to Euro and metrics units
full_url="${full_url}&currency=EUR&units=mks"


./scripts/scrape_sofifa_url.sh "${full_url}" 60 "PLAYERS" "${dest_dir}"

# Return ok if we come that far
exit 0
