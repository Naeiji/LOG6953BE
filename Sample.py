import pandas as pd
import numpy as np
import glob


def is_empty(item):
    return type(item) is str


def show_sizes(r):
    apps = r.groupby('App ID')
    print(apps.size())


def Sampler():
    # loading files and indexing
    releases = pd.read_csv('files/releases.csv')
    reviews = pd.concat([pd.read_csv(reviews) for reviews in glob.glob("dataset/*/appbot-reviews.csv")])
    reviews.index = np.arange(len(reviews))

    # processing
    for index, row in reviews.iterrows():
        app_id, date, country, subject, body = row['App ID'], row['Date'], row['Country'], row['Subject'], row['Body']

        rd = releases.loc[releases['Package Name'] == app_id]['Latest Release Date'].item()

        if not is_empty(rd) or (date < rd) or (country != 'English') or not (is_empty(body) or is_empty(subject)):
            reviews.drop(index, inplace=True)

    # getting sample from an app with more than 1000 reviews
    sdf = reviews.loc[reviews['App ID'] == 'at.tomtasche.reader'].sample(n=1000)
    for index, row in sdf.iterrows():
        reviews.drop(index, inplace=True)

    # reIndexing reviews and saving in a csv file
    reviews.index = np.arange(len(reviews))
    reviews.to_csv(r'Out.csv', index=False)

    show_sizes(reviews)

Sampler()
