
### !!! POC !!! ###

import re

from bs4 import BeautifulSoup


PLAYER_FIELDS = {
    'pi': { 'json_key_name': 'id' },
    'ae': { 'json_key_name': 'Age' },
}



def parse_player_row(player_row):
    player_dict = {}

    # Process all expected fields
    for field_name, field_data in PLAYER_FIELDS.items():
        field = player_row.find('td',{'data-col':field_name})

        player_dict[field_data['json_key_name']] = field.text


    return player_dict


def parse_file(file_path):
    players_dict = {}

    with open(file_path, 'r', encoding='utf-8') as file_ptr:
        contents = file_ptr.read()
        soup = BeautifulSoup(contents, "html.parser")

        #players = soup.findAll('a', {'href': re.compile('/player/*')})
        players = soup.select('tbody tr')
        print('PLAYERS FOUND:', len(players))
        for player in players:
            player_dict = parse_player_row(player)
            if player_dict and player_dict['id'] not in players_dict:  # Ensure no duplicates
                players_dict[player_dict['id']] = player_dict

            tooltip = player.find("a",{"class":"tooltip"})
            #print(tooltip.get('data-tooltip'), ',', tooltip.text)

    print(players_dict)
    print('Total Players Parsed:', len(players_dict))


def main():
    file_path = R'D:\temp\sofifaTest\test3\sofifa_data\html\Players\PLAYERS_offset_0.html'
    parse_file(file_path)

if __name__ == '__main__':
    main()
