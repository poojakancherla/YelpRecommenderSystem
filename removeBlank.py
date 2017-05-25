with open('yelp_business.csv') as f1:
    with open('yelp_business1.csv','w') as f2:
        for line in f1.readlines():
            if ''.join(line.split(',')).strip() == '':
                continue
            f2.write(line)
