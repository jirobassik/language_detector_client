def write_txt(data):
    with open('summarize_view/static/summarize_view/upload/summarize.txt', 'w', encoding='utf-8') as outfile:
        outfile.write(
            f'Реферирование по ключевым словам: {data["key_words"]}\n'
            f'Классическое реферирование: {data["sum_text"]}\n'
            f'Реферирование с машинным обучением: {data["sum_text_standart"]}')
