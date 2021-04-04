
import json


def write_data_dict_to_json(data_dict, json_path):
    with open(json_path, 'w', encoding='utf-8') as file_ptr:
        json.dump(data_dict, file_ptr, indent=4, sort_keys=True, ensure_ascii=False)


def convert_euros(text):
    # Remove the Symbol
    new_val = text.removeprefix('€')

    # Convert Value
    multi = 1
    if new_val.endswith('M'):
        multi = 1000000
        new_val = new_val.removesuffix('M')
    elif new_val.endswith('K'):
        multi = 1000
        new_val = new_val.removesuffix('K')

    return float(new_val) * multi


def convert_cm(text):
    return int(text.removesuffix('cm'))


def convert_kg(text):
    return float(text.removesuffix('kg'))
