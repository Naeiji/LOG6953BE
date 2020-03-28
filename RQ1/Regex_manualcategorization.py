import csv
import re
import pandas as pd
from nltk import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from pandas import isnull
from collections import OrderedDict
import glob

def stemming(sentence):
   words = word_tokenize(sentence)
   sentence_stem = []
   for word in words:
       sentence_stem.append(PorterStemmer().stem(word))
       sentence_stem.append(" ")
   return "".join(sentence_stem)

def stemming_review(Text):
    sent_tokenized = sent_tokenize(Text)
    text = []
    for sentence in sent_tokenized:
        text.append(stemming(sentence))

    stemmed_review = ''.join(text)

    return(stemmed_review)



###keywords for each category
device_keyword = ['Chromecast', 'Mac', 'tablets', 'smartphones', 'ASA5505', 'oppo f3','HTC', 'S7', 'phone', 'device',
                  'cell phone', 'desktop', 'android device', 'note', 'PC', 'laptop', 'Samsung', 'SM-P600','Galaxy Note',
                  'Lite', 'Galaxy', 's5', 'M8', 'nexus', 'android wear', 'Lenovo', 'Yoga Tab 10']

device_stemmed_keywords = []
for key in device_keyword:
    device_stemmed_keywords.append(stemming(key))


android_version_keywords = ['android 7', 'web kit', 'Android 5.1', 'lollipop', 'kitkat' , 'Nougat']

android_stemmed_keywords = []
for key in android_version_keywords:
    android_stemmed_keywords.append(stemming(key))

hardware_keywords =['hardware keyboard', 'SD card', 'sdcard','fingerprint scanner', 'USB']

hardware_stemmed_keywords = []
for key in hardware_keywords:
    hardware_stemmed_keywords.append(stemming(key))

app_usability_keywords = ['request', 'excellent','perfect', 'Great app', 'what I wanted', 'what I needed', 'I want',
                          'functionality','Wonderful', 'Straight forward', 'easy to use', 'working', 'how to', 'Useful',
                          'option', 'enqueue', 'ability', 'features', 'unable', 'Lacks', 'trust', 'reliable', 'impressed',
                          'Simple', 'private', 'elegant', 'Magnificent', 'Good', 'fave', 'favorite', 'works well','wow',
                          'Favourite', 'better', 'useless', 'awsome','awesome', 'glad', 'Love', 'pretty', 'splendid', 'fantastic',
                          'cannot',"can't", 'brilliant', 'Sweet', 'effective', 'action', 'Does not work', 'what I would like',
                          'handy', 'Fake', "Doesn't allow to",'it does not', 'efficient','I loose pretty much everything',
                          'help', 'intuitive', 'Thanks', 'Nice', 'all I need', 'changes were lost', 'Smooth',
                          "it wouldn't let", 'Could not even open', 'Hates','Easy', 'reliably', 'stable', 'Horrible',
                          'Limiting', 'Super', 'no problem','Great', 'waste', 'like','ok','best','wonderful', 'bad']

usability_stemmed_keywords = []
for key in app_usability_keywords:
    usability_stemmed_keywords.append(stemming(key))
print(usability_stemmed_keywords)
ui_keywords = ['should stay open', 'interface', 'UI', 'tab', 'shortcut bar', 'icons', 'widget', 'notification tray',
               'screen', 'set the home page', 'button', 'menue', 'shortcut', 'navigation bar', 'theme', 'gesture',
               'manual', 'turn off', 'drag-n-drop', 'drag', 'drop', 'transparent', 'background', 'border', 'horizental',
               'vertical', 'side of the page', 'scrollable', 'scroll', 'page size' , 'fonts', 'highlight text',
               'toolbar']

ui_stemmed_keywords = []
for key in ui_keywords:
    ui_stemmed_keywords.append(stemming(key))

performance_keywords = ['fast', 'speed', 'slow', 'powerful', 'quick', 'faster', 'fastest', 'slower', 'slowest']

performance_stemmed_keywords = []
for key in performance_keywords:
   performance_stemmed_keywords.append(stemming(key))

battery_keywords = ['battery']

battery_stemmed_keywords = []
for key in battery_keywords:
    battery_stemmed_keywords.append(stemming(key))
memory_keywords = ['bulky', 'small', 'lightweight', 'light', 'real time', 'instant', 'memory']

memory_stemmed_keywords = []
for key in memory_keywords:
    memory_stemmed_keywords.append(stemming(key))

licensing_keywords=['license', 'certificate']

licensing_stemmed_keywords = []
for key in licensing_keywords:
    licensing_stemmed_keywords.append(stemming(key))

price_keywords= ['free', '$', 'dollar', 'expensive', 'pay', 'paied']

price_stemmed_keywords = []
for key in price_keywords:
    price_stemmed_keywords.append(stemming(key))

security_keywords =['secure', 'security', 'pin', 'password','lock']

security_stemmed_keywords = []
for key in security_keywords:
    security_stemmed_keywords.append(stemming(key))

privacy_keyword = ['rules', 'privacy', 'permission']

privacy_stemmed_keywords = []
for key in privacy_keyword:
    privacy_stemmed_keywords.append(stemming(key))

complaint_keywords = ['freeze', 'bug', 'issue', 'crash', 'complaint', 'annoying', 'error', 'problem', 'buggy', 'flaws',
                      'fix', 'solve','fail']

complaint_stemmed_keywords = []
for key in complaint_keywords:
    complaint_stemmed_keywords.append(stemming(key))


def LLC(text): # getting list of categories for each review:

    def category(category_keywords):
        flag = False
        for key in category_keywords:
            if key in text:
                flag = True
                break
        return flag

    LLC_list = []

    # device
    if category(device_stemmed_keywords):
        LLC_list.append("device")

    # android_version
    if category(android_stemmed_keywords):
        LLC_list.append("android version")

    # Hardware
    if category(hardware_stemmed_keywords):
        LLC_list.append("hardware")

    # app usability
    if category(usability_stemmed_keywords):
        LLC_list.append("app usability")

    # UI
    if category(ui_stemmed_keywords):
        LLC_list.append("UI")

    # performance
    if category(performance_stemmed_keywords):
        LLC_list.append('performance')

    # battery
    if category(battery_stemmed_keywords):
        LLC_list.append("battery")

    # memory
    if category(memory_stemmed_keywords):
        LLC_list.append("memory")

    # licensing
    if category(licensing_stemmed_keywords):
        LLC_list.append("licensing")

    # price
    if category(price_stemmed_keywords):
        LLC_list.append("price")

    # security
    if category(security_stemmed_keywords):
        LLC_list.append("security")

    # privacy
    if category(privacy_stemmed_keywords):
        LLC_list.append("privacy")

    # complaint
    if category(complaint_stemmed_keywords):
        LLC_list.append("complaint")

    return LLC_list

def HLC(result):
    HLC_list = []
    for i in result:
        if i == 'device' or i == 'hardware' or i == 'android version':
            HLC_list.append('compatibility')
        elif i == 'app usability' or i == 'UI':
            HLC_list.append('usage')
        elif i == 'performance' or i == 'battery' or i == 'memory':
            HLC_list.append('Resources')
        elif i == 'licensing' or i == 'price':
            HLC_list.append('pricing')
        elif i == 'privacy' or i == 'security':
            HLC_list.append('protection')
        elif i == 'complaint':
            HLC_list.append('complaint')

    HLC_list = list(OrderedDict.fromkeys(HLC_list))
    return HLC_list



with open('reviews_ with_categories.csv', 'w', encoding='utf8', newline='') as Output:
    writer = csv.writer(Output)
    # for app in app_list:

    with open(" review-all.csv", 'r', encoding='utf8') as input_file:
        Reviews = csv.reader(input_file, delimiter=',')
        count = 0
        for review in Reviews:
            print(count)
            count += 1
            Text = ''
            if review[4] == 'English':  # just working on english reviews
                # getting title and body of reviews
                if review[9] == '':
                    pass
                else:
                    Text = review[9]+ ' ' + '.'
                if review[10] == '':
                    pass
                else:
                    Text = Text + ' '+ review[10]

                print(Text)
                Doc = stemming_review(Text)
                print(Doc)

                final_LLC = LLC(Doc)
                final_HLC = HLC(final_LLC)
                print(final_LLC)
                print(final_HLC)

                writer.writerow(review + [final_LLC] + [final_HLC])

    Output.close()

