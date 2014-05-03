import csv
import sys
#sys.stdout = open("all_results.json", "w")

list_file = []
with open('world-country-centroids.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONE)

    for row in reader:
    	print row
    	list_file.append(row)

print list_file[3]
'''
#for x in list_num_country:
#	print x[1]


import json
list_num_names = []
list_num_imports = [] 
dictionary_name = {}
dictionary = {} 

with open('all_country_trade_value.json', 'r+') as f:
    data = json.load(f)
    for x in data:
    	list_num_names.append(x['name'])
    	list_num_imports.append(x['imports'])




    #print list_num_names
	#print list_num_imports

	for n,i in enumerate(list_num_names):
		for x in list_num_text:
			if str(i) == str(x[0]):
#				print n
				list_num_names[n] = str(x[1])



	for n,i in enumerate(list_num_imports):
		for ni, ii in enumerate(i): 
			for x in list_num_text:
				if str(ii) == str(x[0]):
					i[ni] = str(x[1])
	

#for x in list_num_names:
#	print x 
#for x in list_num_imports:
#	print x 

dictionary = {}
for x in list_num_names:
	dictionary[x] = list_num_imports[:]

print dictionary


dictionary = dict(zip(list_num_names, list_num_imports))

#print dictionary
#print "000000000000000000000000000000000"

haha = json.dumps([{'name': k, 'imports': v} for k,v in dictionary.items()], indent=4)

print haha


97 - eu 
251 - monaco 
381 - italy 
579 - norway 
699 - india 
757

'''




