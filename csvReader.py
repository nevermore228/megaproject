import csv

results = []
application_id = []
ssl_server_name = []
with open('test.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ssl_server_name.append(row['ssl_server_name'])
        application_id.append(row['application_id'])
    #print(ssl_server_name)
