
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
