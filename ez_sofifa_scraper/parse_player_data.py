
import os
import re

from bs4 import BeautifulSoup, SoupStrainer

from ez_sofifa_scraper.utils import convert_cm, convert_euros, convert_kg


PLAYER_HTML_KEY_LOOKUP = {
    'ac': 'acceleration',
    'ae': 'age',
    'ag': 'agility',
    'ar': 'aggression',
    'aw': 'attacking_work_rate',
    'ba': 'balance',
    'bl': 'ball_control',
    'bo': 'best_overall',
    'bp': 'best_position',
    'bs': 'base_stats',
    'cm': 'composure',
    'cr': 'crossing',
    'cu': 'curve',
    'def': 'defence',
    'dr': 'dribbling',
    'dri': 'dri',
    'dw': 'defensive_work_rate',
    'fi': 'finishing',
    'fr': 'free_kick_accuracy',
    'gc': 'goal_keeper_kicking',
    'gd': 'goal_keeper_diving',
    'gh': 'goal_keeper_handling',
    'gp': 'goal_keeper_positioning',
    'gr': 'goal_keeper_reflexes',
    'gu': 'growth',
    'he': 'heading_accuracy',
    'hi': 'height_cm',
    'in': 'interceptions',
    'ir': 'international_reputation',
    'jt': 'joined',
    'ju': 'jumping',
    'le': 'loan_date_end',
    'ln': 'long_shots',
    'lo': 'long_passing',
    'ma': 'marking',
    'oa': 'overall_rating',
    'pac': 'pace',
    'pas': 'passing',
    'pe': 'penalties',
    'pf': 'preferred_foot',
    'phy': 'physical',
    'pi': 'id',
    'po': 'positioning',
    'pt': 'potential',
    'rc': 'release_clause_euros',
    're': 'reactions',
    'sa': 'standing_tackle',
    'sh': 'short_passing',
    'sho': 'shooting',
    'sk': 'skill_moves',
    'sl': 'sliding_tackle',
    'so': 'shot_power',
    'sp': 'sprint_speed',
    'sr': 'strength',
    'st': 'stamina',
    'ta': 'total_attacking',
    'td': 'total_defending',
    'te': 'total_mentality',
    'tg': 'total_goalkeeping',
    'to': 'total_movement',
    'tp': 'total_power',
    'ts': 'total_skill',
    'tt': 'total_stats',
    'vi': 'vision',
    'vl': 'value_euros',
    'vo': 'volleys',
    'wg': 'wage_weekly_euros',
    'wi': 'weight_kg',
    'wk': 'weak_foot',
}


PLAYER_FIELD_TYPE_CONVERTION = {
    'acceleration': int,
    'age': int,
    'aggression': int,
    'agility': int,
    'balance': int,
    'ball_control': int,
    'base_stats': int,
    'best_overall': int,
    'composure': int,
    'contract_from': int,
    'contract_to': int,
    'crossing': int,
    'curve': int,
    'defence': int,
    'dri': int,
    'dribbling': int,
    'finishing': int,
    'free_kick_accuracy': int,
    'goal_keeper_diving': int,
    'goal_keeper_handling': int,
    'goal_keeper_kicking': int,
    'goal_keeper_positioning': int,
    'goal_keeper_reflexes': int,
    'growth': int,
    'heading_accuracy': int,
    'height_cm': convert_cm,
    'interceptions': int,
    'international_reputation': int,
    'jumping': int,
    'long_passing': int,
    'long_shots': int,
    'marking': int,
    'overall_rating': int,
    'pace': int,
    'passing': int,
    'penalties': int,
    'physical': int,
    'positioning': int,
    'potential': int,
    'reactions': int,
    'release_clause_euros': convert_euros,
    'shooting': int,
    'short_passing': int,
    'shot_power': int,
    'skill_moves': int,
    'sliding_tackle': int,
    'sprint_speed': int,
    'stamina': int,
    'standing_tackle': int,
    'strength': int,
    'total_attacking': int,
    'total_defending': int,
    'total_goalkeeping': int,
    'total_mentality': int,
    'total_movement': int,
    'total_power': int,
    'total_skill': int,
    'total_stats': int,
    'value_euros': convert_euros,
    'vision': int,
    'volleys': int,
    'wage_weekly_euros': convert_euros,
    'weak_foot': int,
    'weight_kg': convert_kg,
}


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
    team_text = player_row.find('a', {'href': re.compile('/team/*')})
    if team_text:
        player_dict['team'] = team_text.text
    else:
        player_dict['team'] = ''

    # Contract
    contract_text = player_row.find('div', {'class': 'sub'}).text.strip()
    if ' ~ ' in contract_text:
        contract = contract_text.split(' ~ ')
        player_dict['contract_from'] = contract[0]
        player_dict['contract_to'] = contract[1]
    else:
        player_dict['contract_from'] = 0
        player_dict['contract_to'] = 0

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
            player_dict[convert_name] = convert_func(player_dict[convert_name])

    return player_dict


def parse_player_file(file_path):
    players_dict = {}

    with open(file_path, 'rb') as file_ptr:  # By opening in bytes beautifoul soup avoids unicode errors
        contents = file_ptr.read()

        table = SoupStrainer('tbody', 'list')
        soup = BeautifulSoup(contents, "html.parser", from_encoding="utf-8", parse_only=table)

        players = soup.select('tbody tr')
        for player in players:
            player_dict = parse_player_row(player)
            if player_dict and player_dict['id'] not in players_dict:  # Ensure no duplicates
                players_dict[player_dict['id']] = player_dict

    return players_dict


def parse_player_files_from_dir(base_dir):
    players_dict = {}

    for file_name in os.listdir(base_dir):
        if file_name.lower().endswith('.html'):
            file_path = os.path.join(base_dir, file_name)
            print('Parsing file', file_path)
            players_dict |= parse_player_file(file_path)

    return players_dict
