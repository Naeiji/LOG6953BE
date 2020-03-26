import pathlib
import re

from Static import stop_words
from git import Repo
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


class Localizer:

    def __init__(self, review=None):
        self.review = review
        self.file = None
        self.splitted_file = None
        self.clean_splitted_file = list()

    def download(self):
        regex = '^(h.+//.*/.*/.*/)'

        release = 'https://github.com/litrik/be.norio.randomapp/releases'
        url = re.match(regex, release, re.IGNORECASE).group(1)[:-1] + '.git'
        Repo.clone_from(url, str(pathlib.Path().absolute()) + '/boy/')

    def read_file(self):
        with open('boy/src/be/norio/randomapp/ui/MainActivity.java', 'r') as content_file:
            self.file = content_file.read()

    def remove_comment_import(self):
        a = self.file.find('public')
        b = self.file.rfind('}')
        self.file = self.file[a:b + 1]

    def tokenize(self):
        self.splitted_file = word_tokenize(str(self.file))
        self.splitted_file = [m.group(0)
                              for word in self.splitted_file
                              for m in re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', word)]

        for item in self.splitted_file:
            item = item.lower().strip()
            if item.__contains__('.') or len(item) < 3:
                continue
            elif item not in stop_words:
                self.clean_splitted_file.append(item)

    def stemmer(self):
        ps = PorterStemmer()
        self.clean_splitted_file = [ps.stem(word) for word in self.clean_splitted_file]

    def run(self):
        self.read_file()
        self.remove_comment_import()
        self.tokenize()
        self.stemmer()
        print(self.clean_splitted_file)


obj = Localizer()
obj.run()
