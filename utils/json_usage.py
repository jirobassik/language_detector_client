import json


def write_json(data):
    with open('summarize_view/static/summarize_view/upload/statistic.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)
