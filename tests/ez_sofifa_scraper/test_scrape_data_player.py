
import pytest

from bs4 import BeautifulSoup

from ez_sofifa_scraper.scrape_data import parse_player_row
from ez_sofifa_scraper.scrape_definitions import PLAYER_HTML_KEY_LOOKUP
from tests.ez_sofifa_scraper.TestFiles.player_rows import PLAYER_1_ROW_STR


HTML_KEY_TRANSLATION = [
    ('ac', 'acceleration'),
    ('ae', 'age'),
    ('ag', 'agility'),
    ('ar', 'aggression'),
    ('aw', 'attacking_work_rate'),
    ('ba', 'balance'),
    ('bl', 'ball_control'),
    ('bo', 'best_overall'),
    ('bp', 'best_position'),
    ('bs', 'base_stats'),
    ('cm', 'composure'),
    ('cr', 'crossing'),
    ('cu', 'curve'),
    ('def', 'defence'),
    ('dr', 'dribbling'),
    ('dri', 'dri'),
    ('dw', 'defensive_work_rate'),
    ('fi', 'finishing'),
    ('fr', 'free_kick_accuracy'),
    ('gc', 'goal_keeper_kicking'),
    ('gd', 'goal_keeper_diving'),
    ('gh', 'goal_keeper_handling'),
    ('gp', 'goal_keeper_positioning'),
    ('gr', 'goal_keeper_reflexes'),
    ('gu', 'growth'),
    ('he', 'heading_accuracy'),
    ('hi', 'height'),
    ('in', 'interceptions'),
    ('ir', 'international_reputation'),
    ('jt', 'joined'),
    ('ju', 'jumping'),
    ('le', 'loan_date_end'),
    ('ln', 'long_shots'),
    ('lo', 'long_passing'),
    ('ma', 'marking'),
    ('oa', 'overall_rating'),
    ('pac', 'pace'),
    ('pas', 'passing'),
    ('pe', 'penalties'),
    ('pf', 'preferred_foot'),
    ('phy', 'physical'),
    ('pi', 'id'),
    ('po', 'positioning'),
    ('pt', 'potential'),
    ('rc', 'release_clause'),
    ('re', 'reactions'),
    ('sa', 'standing_tackle'),
    ('sh', 'short_passing'),
    ('sho', 'shooting'),
    ('sk', 'skill_moves'),
    ('sl', 'sliding_tackle'),
    ('so', 'shot_power'),
    ('sp', 'sprint_speed'),
    ('sr', 'strength'),
    ('st', 'stamina'),
    ('ta', 'total_attacking'),
    ('td', 'total_defending'),
    ('te', 'total_mentality'),
    ('tg', 'total_goalkeeping'),
    ('to', 'total_movement'),
    ('tp', 'total_power'),
    ('ts', 'total_skill'),
    ('tt', 'total_stats'),
    ('vi', 'vision'),
    ('vl', 'value'),
    ('vo', 'volleys'),
    ('wg', 'wage_weekly'),
    ('wi', 'weight'),
    ('wk', 'weak_foot'),
]
@pytest.mark.parametrize('html_key, readable_key', HTML_KEY_TRANSLATION)
def test_player_attribute_key_translation(html_key, readable_key):
    assert PLAYER_HTML_KEY_LOOKUP[html_key] == readable_key


PLAYER_1_ROW_DETAILS = [
    ('image_url', 'https://cdn.sofifa.com/players/001/179/21_60.png'),
    ('image_url_2x', 'https://cdn.sofifa.com/players/001/179/21_120.png'),
    ('image_url_3x', 'https://cdn.sofifa.com/players/001/179/21_180.png'),
    ('detail_url', '/player/1179/gianluigi-buffon/210019/'),
    ('full_name', 'Gianluigi Buffon'),
    ('short_name', 'G. Buffon'),
    ('nationality', 'Italy'),
    ('positions', ['GK', 'LM', 'LW']),
    ('team', 'Juventus'),
    ('contract_from', '2019'),
    ('contract_to', '2021'),

    # Attributes
    ('acceleration', '37'),
    ('age', '42'),
    ('agility', '55'),
    ('aggression', '38'),
    ('attacking_work_rate', 'Medium'),
    ('balance', '49'),
    ('ball_control', '28'),
    ('best_overall', '82'),
    ('best_position', 'GK'),
    ('base_stats', '429'),
    ('composure', '70'),
    ('crossing', '13'),
    ('curve', '20'),
    ('defence', '33'),
    ('dribbling', '26'),
    ('dri', '78'),
    ('defensive_work_rate', 'Medium'),
    ('finishing', '15'),
    ('free_kick_accuracy', '13'),
    ('goal_keeper_kicking', '74'),
    ('goal_keeper_diving', '77'),
    ('goal_keeper_handling', '76'),
    ('goal_keeper_positioning', '91'),
    ('goal_keeper_reflexes', '78'),
    ('growth', '0'),
    ('heading_accuracy', '13'),
    ('height', '192cm'),
    ('interceptions', '28'),
    ('international_reputation', '4'),
    ('joined', 'Jul 4, 2019'),
    ('jumping', '71'),
    ('loan_date_end', 'N/A'),
    ('long_shots', '13'),
    ('long_passing', '35'),
    ('marking', '13'),
    ('overall_rating', '82'),
    ('pace', '77'),
    ('passing', '74'),
    ('penalties', '22'),
    ('preferred_foot', 'Right'),
    ('physical', '91'),
    ('id', '1179'),
    ('positioning', '12'),
    ('potential', '82'),
    ('release_clause', '€5.6M'),
    ('reactions', '80'),
    ('standing_tackle', '11'),
    ('short_passing', '37'),
    ('shooting', '76'),
    ('skill_moves', '1'),
    ('sliding_tackle', '11'),
    ('shot_power', '56'),
    ('sprint_speed', '30'),
    ('strength', '69'),
    ('stamina', '34'),
    ('total_attacking', '95'),
    ('total_defending', '35'),
    ('total_mentality', '150'),
    ('total_goalkeeping', '396'),
    ('total_movement', '251'),
    ('total_power', '243'),
    ('total_skill', '122'),
    ('total_stats', '1292'),
    ('vision', '50'),
    ('value', '€3.4M'),
    ('volleys', '17'),
    ('wage_weekly', '€41K'),
    ('weight', '92kg'),
    ('weak_foot', '2'),
]

@pytest.mark.parametrize('key, value', PLAYER_1_ROW_DETAILS)
def test_read_player_row(key, value):
    player_dict = parse_player_row(BeautifulSoup(PLAYER_1_ROW_STR, "html.parser"))

    assert key in player_dict
    assert player_dict[key] == value


'''
def test_convert_player_data():
    # TODO, convert to field convertion, e.g. type, name convertion...
    assert False


def test_read_html_file():
    # TODO - Test all fields are found for each player, just the key
    assert False


def test_read_multiple_html_files():
    # TODO - Test the right number of players are found, with each field found
    assert False
'''
