import json
import csv
import re
import pandas as pd


df = pd.read_csv('yelp_reviews.csv')
d = df.business_id
d1={}
print(len(d))
for x in d:
	d1[x]=0

print(len(d1))

filename = "yelp_academic_dataset_business.json"
str = 'Restaurant'
count=0
bcount = 0
nctr=0
# with open('yelp_reviews.csv') as fread:
with open('yelp_business.csv', 'w') as file:
    w = csv.writer(file)
    w.writerow([ "business_id", "latitude", "longitude", "name","avg rating","city", "state", "num_reviews","categories",   "hours"])
    with open(filename, encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)
            if data['business_id'] in d1.keys():
                # count += 1
                try:
                    list = repr(data['categories'])
                    if re.search("Restaurant", list):
                        print(data['categories'])
                        bcount += 1
                        w.writerow([data['business_id'], data['latitude'], data['longitude'], data['name'],data['stars'], data['city'], data['state'], data['review_count'],  data['categories'], data['hours']])
                        count += 1

                except:
                    nctr+=1
                    pass
            else:
                pass
        print(count,nctr)
        # print("bcount: "+ bcount);
