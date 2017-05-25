import ast
import csv
from collections import defaultdict
from scipy.spatial import distance
import time
## Generates accessible Latitudes and Longitudes
def extract_ll(la,lo,code):
    la=la[:-3]
    lo=lo[1:-3]
    if code == 1:
        return la+","+lo
    elif code == 2:
        return la+",-"+lo
    elif code == 3:
        return "-"+la+","+lo
    elif code == 4:
        return "-"+la+",-"+lo

print(chr(27) + "[2J")


"""==================================================="""
""" ENTER THE LATITUDE AND LONGITUDE & ALSO THE RADIUS"""
"""==================================================="""
### Give the users Latitude and Longitude
print("Enter the Latitude & Longitude of Users Location")
s=input()
print()
print("Enter users travel range in meters")

### Distance is in Meters
dist = int(input())
# print(chr(27) + "[2J")
#
# print("\nPlease wait while we pull out the best restaurants around you!")
# """==================================================="""
# time.sleep(2)
#
# print(chr(27) + "[2J")


dist = dist/1000
la,lo = s.split(',')
if la[-1]=='N':
    if lo[-1]=='E':
        location=extract_ll(la,lo,1)
    else:
        location=extract_ll(la,lo,2)
else:
    if lo[-1]=='E':
        location=extract_ll(la,lo,3)
    else:
        location=extract_ll(la,lo,4)

lat,lon = location.split(",")





"=============================================Code Begins========================================================"
a=(float(lat),float(lon))

aLa = str(lat)
aLo = str(lon)

columns = defaultdict(list)



### Extracting all the latitudes and longitudes in business dataset for calulating similarity
with open('yelp_business1.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for (k,v) in row.items():
            columns[k].append(v)

l=[]
latlon=[]
longi=[]
ctr=0

NearByLocations=[]

la={}
lo={}


### Indexes the Latitudes for better search and for reducing the time complexity
ind = {}
for x in range(len(columns['latitude'])):
    try:
        ind[columns['latitude'][x][0:2]].append((columns['latitude'][x],columns['longitude'][x]))
    except:
        ind[columns['latitude'][x][0:2]] = [(columns['latitude'][x],columns['longitude'][x])]




target = ind[aLa[0:2]]     ### Time complexity is reduced from n2 to n





### Finding out the Euclidean Distance between the User and the Restaurants
for x in range(len(target)):
    try:
        dst = distance.euclidean(a,(float(target[x][0]),float(target[x][1])))
        if dst<=dist:
            NearByLocations.append((target[x][0],target[x][1]))
    except:
        pass






'''### Contains all the Restaurants near an earlier defined radius'''
NearByLocations=dict(NearByLocations)






fail=0
troll=[]
business_id=[]  ## Used to store the restaurant business_id!
with open('yelp_business1.csv') as f:
    for i,line in enumerate(f):
        if i==0:
            pass
        else:
            line = line.split(",")
            try:
                if NearByLocations[line[1]]:
                    troll.append((line[4],(line[0],[line[3],line[4],line[5],line[1],line[2]])))

                    #                    business_id,Name,Rating,City,Latitude,Longitude
                    business_id.append((line[0],[line[3],line[4],line[5],line[1],line[2]]))
            except:
                fail=1



### No nearby locations!
if fail==1 and len(business_id)==0:
    if dist*1000 == 1 or dist*1000 == 0:
        print("No restaurants where you're standing, please increase the distance! :)\n")
    else:
        print("Sorry, no restaurants nearby!\n")


### Writing in a CSV file
wr = business_id
with open("UserLoc.csv","w") as f:
    print("business_id,Restaurant,Rating,City,Latitude,Longitude",file = f)
    for l in wr:
        print("%s,%s,%s,%s,%s,%s"%(l[0],l[1][0],l[1][1],l[1][2],l[1][3],l[1][4]),file=f)


business_id = dict(business_id)
finalRes = {}   ### Used to store the Final Outputs!!!





### Checking the sentiment for the restaurants!
with open('yelp_reviews.csv') as freviews:
    for i,line in enumerate(freviews):
        if i==0:
            pass
        line = line.split(",")

        if line[1] in business_id.keys():

            if int(line[7])>7.3: ## Checks if the sentiment is positive or not!
                try:
                    if float(business_id[line[1]][1])>3: ## Average rating of the restaurant!

                        finalRes[business_id[line[1]][0]]=(business_id[line[1]][2], business_id[line[1]][0], business_id[line[1]][1], business_id[line[1]][3],business_id[line[1]][4],line[1])
                except:
                    pass

# print(finalRes)
### Final outpust!!!
SortedOutputs = []
if not(fail==1 and len(business_id)==0):
    print("___________________________________________________________________________________________________________________________")
    # print("business_id".ljust(30), "Restaurant".ljust(65),"City".ljust(20), "Rating".ljust(30))
    print("Restaurant".ljust(65),"City".ljust(20), "Rating".ljust(30))

    print("___________________________________________________________________________________________________________________________")

cntr=0
for k, v in finalRes.items():
    l = v
    # print(l)
    SortedOutputs.append((l[2],[l[0],l[1],l[2],l[5]]))
SortedOutputs = sorted(SortedOutputs,reverse=True)
SortedOutputs = SortedOutputs [0:50] ## Top 50 Sorted Senti Outputs
# print(SortedOutputs)
OP = []
for i, v in SortedOutputs:
    OP.append(v)

# print(OP)
## Displaying the Sorted results with respect to Ratings!
with open("LocAndSenti.csv","w") as f:
    print("business_id,Restaurant,City,Rating",file = f)
    for l in OP:
        print("%s,%s,%s,%s"%(l[3],l[1],l[0],l[2]),file=f)

ctr=0
for l in OP:
    # print(l[3].ljust(30), l[1].ljust(65),l[0].ljust(20),l[2].ljust(30))
    print(l[1].ljust(65),l[0].ljust(20),l[2].ljust(30))
    if ctr==10:
        break
    ctr+=1


""" TESTING ZONE """
### Finds out the categories in the restaurants
# main=[]
#
# for x in columns['categories']:
#     jj=ast.literal_eval(x)
#     if 'Restaurants' in jj:
#         l.append(jj)
#
# for x in l:
#     for y in x:
#         main.append(y)
#
# main=list(set(main))
#
# print(main)
