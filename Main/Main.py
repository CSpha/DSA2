import csv


# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=40):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.

    def insert(self, key, address, city, state, zipcode, deadline, weight, status):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = address
                kv[2] = city
                kv[3] = state
                kv[4] = zipcode
                kv[5] = deadline
                kv[6] = weight
                kv[7] = status
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, address, city, state, zipcode, deadline, weight, status]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.

    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[0], kv[1], kv[2], kv[3], kv[4], kv[5], kv[6], kv[7]  # value
        return None

    # Removes an item with matching key from the hash table.

    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1], kv[2], kv[3], kv[4], kv[5], kv[6], kv[7]])


class Package:
    def __init__(self, ID, address, city, state, zipcode, deadline, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status

    def __str__(self):  # overwrite print(Package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s" % (
            self.ID, self.address, self.city, self.state, self.zipcode, self.deadline, self.weight, self.status)


def loadPackageData(fileName):
    with open(fileName) as wgupsPackageFile:
        packageData = csv.reader(wgupsPackageFile, delimiter=',')

        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = package[4]
            pDeadline = package[5]
            pWeight = package[6]
            pStatus = "Loaded"

            # package object
            package = Package(pID, pAddress, pCity, pState, pZipcode, pDeadline, pWeight, pStatus)
            #print(p)

            # Insert into the hash table
            myHash.insert(pID, pAddress, pCity, pState, pZipcode, pDeadline, pWeight, pStatus)


# Hash table instance
myHash = ChainingHashTable()

# Load packages to Hash Table
loadPackageData('WGUPSPackageFile.csv')

print("WGUPSPackageFile from Hashtable:")
# Fetch data from Hash Table
for i in range(len(myHash.table)):
    print("Package: {}".format(myHash.search(i+1)))  # 1 to 40 is sent to myHash.search()

