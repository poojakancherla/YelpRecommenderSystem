import json
import datetime
import csv
import unicodedata


filename = "yelp_academic_dataset_user.json"

with open('users.csv', 'w') as file:

    headers = ["user_id", "year", "num_friends", "votes", "num_reviews", "avg rating"]
    w = csv.DictWriter(file, delimiter=',', lineterminator='\n', fieldnames=headers)
    with open(filename, encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            votes = data['useful'] + data['funny'] + data['cool']
            # print(len(data['friends']))

            w.writerow(headers = ["user_id", "year", "num_friends", "votes", "num_reviews", "avg rating"])
            if data['review_count'] >= 150 and votes>=700 and len(data['friends'])>150:
                w.writerow({"user_id": data['user_id'], "year": data['yelping_since'], "num_friends":len(data['friends']),
                            "votes": votes, "num_reviews": data['review_count'], "avg rating": data['average_stars']})
import subprocess

subprocess.call('yelp_reviews.py' ,shell = True)
