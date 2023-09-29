class LanguageDetectorModel:
    def __init__(self, text_language, filename, file_id, language_percent):
        self.language_percent = language_percent
        self.file_id = file_id
        self.filename = filename
        self.text_language = text_language


class StatisticModel:
    def __init__(self, alphabet_time, short_time, neuro_time, english_percent, russian_percent):
        self.russian_percent = russian_percent
        self.english_percent = english_percent
        self.alphabet_time = alphabet_time
        self.short_time = short_time
        self.neuro_time = neuro_time
