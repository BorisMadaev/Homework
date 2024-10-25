class WordsFinder:
    file_names = []
    all_words = {}
    word = ''
    file_words = []
    find_word = {}
    count_word = {}
    schetchik = 0

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        for i in range(len(self.file_names)):
            self.file_words = []
            with open(str(self.file_names[i]), encoding='utf-8') as file:
                for line in file:
                    line = line.replace(',', ' ').replace('.', ' ').replace('=', ' ')
                    line = line.replace('!', ' ').replace('?', ' ').replace(';', ' ')
                    line = line.replace(':', ' ').replace(' - ', ' ')
                    self.file_words.extend(line.lower().split())
            self.all_words.update({str(self.file_names[i]): self.file_words})
        return self.all_words

    def find(self, word):
        self.word = word
        self.get_all_words()
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if self.word.lower() == str(words[i]):
                    self.find_word.update({name: i+1})
                    break
        return self.find_word

    def count(self, word):
        self.word = word.lower()
        self.get_all_words()
        for name, words in self.get_all_words().items():
            self.schetchik = 0
            for i in range(len(words)):
                if self.word.lower() == str(words[i]):
                    self.schetchik += 1
            self.count_word.update({name: self.schetchik})
        return self.count_word

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
