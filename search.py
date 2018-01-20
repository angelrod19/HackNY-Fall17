import requests

zipcode = []
address = []
boro = []
dreamset = {}
url = 'https://data.cityofnewyork.us/resource/byk8-bdfw.json'
url2 = 'http://webpage.pace.edu/ar88230p/meow.json'
dataset = requests.get(url2).json()


for e in range(213):
   zipcode.append(dataset[e]['postcode'])
   address.append(dataset[e]['facilityaddress'])
   boro.append(dataset[e]['borough'])

want = str(input('Input zip code: '))

print("Whole list of zipcodes:")
print(zipcode)


for e in range(213):
    if want in zipcode:
        found = True
        zipindex = zipcode.index(want)
    else:
        found = False

if found == False:
    print("Not found")
else:
    print("Found")


if want not in zipcode:
    print("Not in zipcode.")
else:
    print("Count is %d"  % zipcode.count(want))
    print("Index is %d" % zipindex)
    print("Address of the fire station is: %s" % address[zipindex])
    print("Borough is: %s" % boro[zipindex])
