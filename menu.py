import ast
import csv
from collections import defaultdict
from scipy.spatial import distance

# Declaring the user location
aLa='40.4535915'
aLo='-80.0008071'
a = (40.4535915,-80.0008071)

columns = defaultdict(list)

with open('yelp_business1.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for (k,v) in row.items():
            columns[k].append(v)

l=[]
latlon=[]
longi=[]
ctr=0

locs=[]

la={}
lo={}


for x in columns['latitude']:
    try:
        la[x[0:2]].append(x)
    except:
        la[x[0:2]]=[x]
# print(la)
for x in columns['longitude']:
    try:
        lo[x[0:2]].append(x)
    except:
        lo[x[0:2]]=[x]
# print(lo)

tarLa=la[aLa[0:2]]
tarLo=lo[aLo[0:2]]
# print(tarLo)
# print(tarLa[0])
for x in range(len(tarLa)):
    try:
        dst = distance.euclidean(a,(float(tarLa[x]),float(tarLo[x])))
        if dst<=0.1:
            # print(x,dst)   ### Resturns the id number and the distance between the locations
            locs.append((tarLa[x],tarLo[x]))
    except:
        pass
'''### Contains all the Restaurants near a 1000m radius'''
# print(locs)
print()
LatLong={}
for x in locs:
    LatLong[x[0]]=x[1]
print(LatLong)
business_id=[]
with open('yelp_business1.csv') as f:
    for i,line in enumerate(f):
        if i==0:
            pass
        else:
            line = line.split(",")

            try:
                if LatLong[line[1]]:
                    # print(line[1],line[2])
                    # print(LatLong[line[1]],line[2])
                    # print()
                    if LatLong[line[1]]==line[2]:
                        # print(line[1],line[2])
                        print("yes")

                    # business_id.append(line[])
            except:
                # print("No such location found")
                pass
        # print(line[1],line[2])
        # if line[1] in locs[]
        # if i<=5:
        #     print(line.split(','))# if i<=5 else break)
# for x in columns['latitude']:
#     for y in columns['longitude']:
#         dst = distance.euclidean(a,(float(x),float(y)))
#         if dst<=0.3:
#             locs.append((x,y))
#
# print(locs)

# print("HI")
#
# for x in columns['categories']:
#     jj=ast.literal_eval(x)
#     if 'Restaurants' in jj:
#         l.append(jj)
#
# main=[]
#
# for x in l:
#     for y in x:
#         main.append(y)
#
# main=list(set(main))
#









# print(main)
