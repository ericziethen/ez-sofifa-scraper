"""Script to convert m3u4u channel files to a fake m3u playlist."""

import argparse
import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from ez_sofifa_scraper import scrape_data


def main():
    """Run the main function."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-hd', '--html_dir', help='The directry with the player html files.', required=True)
    parser.add_argument('-jf', '--json_file', help='The file to store the players in.', required=True)
    args = parser.parse_args()

    if (not os.path.exists(args.html_dir)) or not os.path.isdir(args.html_dir):
        raise ValueError(F'"{args.html_dir}" is not a vaid directory')

    os.makedirs(os.path.dirname(args.json_file), exist_ok=True)
    player_dict = scrape_data.parse_player_files_from_dir(args.html_dir)

    with open(args.json_file, 'w') as file_ptr:
        json.dump(player_dict, file_ptr, indent=4, sort_keys=True)

if __name__ == '__main__':
    main()
