
import pytest

from ez_sofifa_scraper.scrape_data import parse_player_row
from ez_sofifa_scraper.scrape_definitions import PLAYER_HTML_KEY_LOOKUP
from tests.ez_sofifa_scraper.TestFiles.player_rows import PLAYER_1_ROW


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
def test_player_attribute_key_translation(html_key, readable_key):
    assert PLAYER_HTML_KEY_LOOKUP[html_key] == readable_key

'''
!!! USE PARAMETRIZE TO EASIER SEE WHICH ONES ARE FAILING
def test_read_player_row():
    dict = parse_player_row(PLAYER_1_ROW)

    # <td class="col-avatar">
    assert dict['image_url'] == 'https://cdn.sofifa.com/players/001/179/21_60.png'
    assert dict['image_url_2x'] == 'https://cdn.sofifa.com/players/001/179/21_120.png'
    assert dict['image_url_3x'] == 'https://cdn.sofifa.com/players/001/179/21_180.png'

    # <td class="col-name">
    assert dict['detail_url'] == '/player/1179/gianluigi-buffon/210019/'
    assert dict['full_name'] == 'Gianluigi Buffon'
    assert dict['short_name'] == 'G. Buffon'
    assert dict['nationality'] == 'Italy'
    assert dict['position'] == 'GK'

    # Attributes
    assert dict['age'] == '42'
    assert dict['overall_rating'] == '82'
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''
    assert dict[''] == ''




def test_convert_player_data():
    assert False


def test_read_html_file():
    assert False


def test_read_multiple_html_files():
    assert False
'''