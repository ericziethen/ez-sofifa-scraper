
### !!! POC !!! ###

import re

from bs4 import BeautifulSoup

from ez_sofifa_scraper.scrape_definitions import PLAYER_HTML_KEY_LOOKUP

# PLAYER_FIELDS = {
#     'pi':{ 'json_key_name': 'id' },
#     'ae':{ 'json_key_name': 'Age' },
# }



def parse_player_row(player_row):
    player_dict = {}

    # Image Sources
    image_tag = player_row.find('img', {'class': 'player-check'})
    player_dict['image_url'] = image_tag.get('data-src')
    player_dict['image_url_2x'] = image_tag.get('data-srcset').split(' ')[0]
    player_dict['image_url_3x'] = image_tag.get('data-srcset').split(' ')[2]

    # Tooltip info
    tooltip_tag = player_row.find('a', {'class': 'tooltip'})
    player_dict['detail_url'] = tooltip_tag.get('href')
    player_dict['full_name'] = tooltip_tag.get('data-tooltip')
    player_dict['short_name'] = tooltip_tag.find('div').text.strip()

    print(tooltip_tag.find('div').text)




    '''
    # Process all expected fields
    for field_name, field_data in PLAYER_FIELDS.items():
        field = player_row.find('td', {'data-col': field_name})

        player_dict[field_data['json_key_name']] = field.text
    '''
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
