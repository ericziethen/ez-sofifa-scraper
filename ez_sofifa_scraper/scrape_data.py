
### !!! POC !!! ###

import re

from bs4 import BeautifulSoup

from ez_sofifa_scraper.scrape_definitions import PLAYER_HTML_KEY_LOOKUP, PLAYER_FIELD_TYPE_CONVERTION


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
    player_dict['nationality'] = tooltip_tag.find('img').get('title')

    # Player Positions
    positions = player_row.findAll('span', {'class': re.compile('pos pos*')})
    player_dict['positions'] = sorted(list({x.text for x in positions}))  # set because finding best position which results in duplicate

    # Team
    player_dict['team'] = player_row.find('a', {'href': re.compile('/team/*')}).text

    # Contract
    contract = player_row.find('div', {'class': 'sub'}).text.strip().split(' ~ ')
    player_dict['contract_from'] = contract[0]
    player_dict['contract_to'] = contract[1]

    # Attributes
    for attrib_name, firendly_name in PLAYER_HTML_KEY_LOOKUP.items():
        attrib_elem = player_row.find('td', {'data-col': attrib_name})

        # For some attributes only we need to ignore the nested span
        ignore_span = ['ir', 'sk', 'wk']
        if attrib_name not in ignore_span:
            sub_span_elem = attrib_elem.find('span')
            if sub_span_elem:
                attrib_elem = sub_span_elem
        # Select the text form the current level, not nested
        player_dict[firendly_name] = attrib_elem.find(text=True, recursive=False).strip()

    # Convert Types
    for convert_name, convert_func in PLAYER_FIELD_TYPE_CONVERTION.items():
        if convert_name in player_dict:
            player_dict[convert_name] = PLAYER_FIELD_TYPE_CONVERTION[convert_name](player_dict[convert_name])

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
