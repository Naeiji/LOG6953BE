import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize , sent_tokenize
from nltk.stem import PorterStemmer
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def stemming(sentence):
   words = word_tokenize(sentence)
   sentencestem = []
   for word in words:
       sentencestem.append(PorterStemmer().stem(word))
       sentencestem.append(" ")
   return "".join(sentencestem)


with open('reviews_preprocessed.csv','w', encoding='utf8', newline='') as Output:
    writer = csv.writer(Output)

    with open('reviews_categories.csv', 'r', encoding='utf8') as input_file:
        Reviews = csv.reader(input_file, delimiter=',')
        Doc = []
        for review in Reviews:
            Text = ''
            # getting title and body of reviews
            if review[9] == '':
                pass
            else:
                Text = review[9] + '.'
            if review[10] == '':
                pass
            else:
                Text = Text + ' ' + review[10]

            Text = Text.replace("'m", " am")
            Text = Text.replace("'s", " is")
            Text = Text.replace("'ve", " have")
            Text = Text.replace("'d", " would")
            Text = Text.replace("wo'nt", " will not")
            Text = Text.replace("can't", " can not")

            #removing stop words
            stop_words = stopwords.words('english')
            sentenceTokenized = sent_tokenize(Text)
            text = []

            for sentence in sentenceTokenized:
                wordTokenized = word_tokenize(sentence)
                noStopWord = []
                for word in wordTokenized:
                    if word.lower() not in stop_words:
                        noStopWord.append(word)
                sent = " ".join(noStopWord)
                #removing punctuations
                no_punctuations = sent.translate(str.maketrans('', '', string.punctuation))
                #Stemming
                text.append(stemming(no_punctuations))
            Text = ''.join(text)
            Doc.append(Text)

            writer.writerow(review + [Text])

        Output.close()

# Data = pd.read_csv('reviews_preprocessed.csv', header=None)
# print(Data.head())
#
# # TF-IDF , for n-gram = 1,2,3
# tf_idf = TfidfVectorizer(ngram_range=(1, 3))
# X = tf_idf.fit_transform(Data[15])
# Data[16] = X
#
# Data.to_csv('review_ready.csv')






