class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                txt = file.read().lower()
                for symbols in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    txt = txt.replace(symbols, '')
                    all_words[name] = txt.split()
        return all_words

    def find(self, word):
        _dict = {}
        for file_name, words in self.get_all_words().items():
            if word.lower() in words:
                _dict[file_name] = words.index(word.lower()) + 1
        return _dict

    def count(self, word):
        _dict = {}
        for name, words in self.get_all_words().items():
            _dict[name] = words.count(word.lower())
        return _dict


finder2 = WordsFinder('test_file.txt', 'test.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
