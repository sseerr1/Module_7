class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation_ = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                content = file.read().lower()
                words = content.replace('.', ' ').replace(',', ' ') \
                    .replace('=', ' ').replace('!', ' ').replace('?', ' '). \
                    replace(';', ' ').replace(':', ' ').replace(' - ', ' ').split()
        all_words.update({self.file_names: words})
        return all_words

    def find(self, word):
        result = {}
        words = self.get_all_words()[self.file_names]
        for i in range(len(words)):
            if word.lower() == words[i]:
                result.update({self.file_names: i + 1})
                return result

    def count(self, word):
        result = {}
        words = self.get_all_words()[self.file_names]
        result.update({self.file_names: words.count(word.lower())})
        return result


################################################################
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
