
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
    ('wg', 'wage'),
    ('wi', 'weight'),
    ('wk', 'weak_foot'),
]
@pytest.mark.parametrize('html_key, readable_key', HTML_KEY_TRANSLATION)
# TODO - ENABLE
def DISABLE_test_player_attribute_key_translation(html_key, readable_key):
    assert PLAYER_HTML_KEY_LOOKUP[html_key] == readable_key


PLAYER_1_ROW_DETAILS = [
    ('image_url', 'https://cdn.sofifa.com/players/001/179/21_60.png'),
    ('image_url_2x', 'https://cdn.sofifa.com/players/001/179/21_120.png'),
    ('image_url_3x', 'https://cdn.sofifa.com/players/001/179/21_180.png'),
    ('detail_url', '/player/1179/gianluigi-buffon/210019/'),
    ('full_name', 'Gianluigi Buffon'),
    ('short_name', 'G. Buffon'),
    ('nationality', 'Italy'),
    ('position', 'GK'),
    ('team', 'Juventus'),

    # Attributes
    ('acceleration', ''),
    ('age', '42'),
    ('agility', ''),
    ('aggression', ''),
    ('attacking_work_rate', ''),
    ('balance', ''),
    ('ball_control', ''),
    ('best_overall', ''),
    ('best_position', ''),
    ('base_stats', ''),
    ('composure', ''),
    ('crossing', ''),
    ('curve', ''),
    ('defence', ''),
    ('dribbling', ''),
    ('dri', ''),
    ('defensive_work_rate', ''),
    ('finishing', ''),
    ('free_kick_accuracy', ''),
    ('goal_keeper_kicking', ''),
    ('goal_keeper_diving', ''),
    ('goal_keeper_handling', ''),
    ('goal_keeper_positioning', ''),
    ('goal_keeper_reflexes', ''),
    ('growth', ''),
    ('heading_accuracy', ''),
    ('height', ''),
    ('interceptions', ''),
    ('international_reputation', ''),
    ('joined', ''),
    ('jumping', ''),
    ('loan_date_end', ''),
    ('long_shots', ''),
    ('long_passing', ''),
    ('marking', ''),
    ('overall_rating', '82'),
    ('pace', ''),
    ('passing', ''),
    ('penalties', ''),
    ('preferred_foot', ''),
    ('physical', ''),
    ('id', ''),
    ('positioning', ''),
    ('potential', ''),
    ('release_clause', ''),
    ('reactions', ''),
    ('standing_tackle', ''),
    ('short_passing', ''),
    ('shooting', ''),
    ('skill_moves', ''),
    ('sliding_tackle', ''),
    ('shot_power', ''),
    ('sprint_speed', ''),
    ('strength', ''),
    ('stamina', ''),
    ('total_attacking', ''),
    ('total_defending', ''),
    ('total_mentality', ''),
    ('total_goalkeeping', ''),
    ('total_movement', ''),
    ('total_power', ''),
    ('total_skill', ''),
    ('total_stats', ''),
    ('vision', ''),
    ('value', ''),
    ('volleys', ''),
    ('wage', ''),
    ('weight', ''),
    ('weak_foot', ''),
]

@pytest.mark.parametrize('key, value', PLAYER_1_ROW_DETAILS)
def test_read_player_row(key, value):
    player_dict = parse_player_row(BeautifulSoup(PLAYER_1_ROW_STR, "html.parser"))

    assert key in player_dict
    assert player_dict[key] == value



def test_convert_player_data():
    # TODO, convert to field convertion, e.g. type, name convertion...
    assert False


def test_read_html_file():
    # TODO - Test all fields are found for each player, just the key
    assert False


def test_read_multiple_html_files():
    # TODO - Test the right number of players are found, with each field found
    assert False
