# Philip Audet - Student ID: 001098879
import csv
import datetime


# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    # Time complexity O(1)
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    # Time complexity O(1)
    def insert(self, key, package):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = package
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, package]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    # Time complexity O(Log N)
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    # Removes an item with matching key from the hash table.
    # Time complexity O(1)
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove(key)

# Create package class
# Time complexity O(1)
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

    # overwrite print(Package) otherwise it will print object reference
    # Time complexity O(1)
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zipcode, self.deadline, self.weight, self.status)

# Defining attributes for each column in package file, creating an object, and inserting each one into the hash table
# Time complexity O(N)
def loadPackageData(filename):
    with open(filename) as packageFile:
        packageData = csv.reader(packageFile, delimiter=',')

        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZipcode = package[4]
            pDeadline = package[5]
            pWeight = package[6]
            pStatus = "At hub"

            # package object
            package = Package(pID, pAddress, pCity, pState, pZipcode, pDeadline, pWeight, pStatus)
            # print(package)

            # Insert into the hash table
            myHash.insert(pID, package)


# Hash table instance
# Time complexity O(1)
myHash = ChainingHashTable()

# Load packages to Hash Table
# Time complexity O(1)
loadPackageData('WGUPSPackageFile.csv')

# Read Distance Table csv and converting to a list of lists (2d array)
def loadDistanceData(filepath):
    with open(filepath, newline='') as distanceFile:
        distanceFile = csv.reader(distanceFile, delimiter=',')
        data = list(distanceFile)
    return data

filepath = 'WGUPSDistanceTable.csv'
distances = loadDistanceData(filepath)

#
def data_location(array, row_index, column_index):
    if array[row_index][column_index]:
        return array[row_index][column_index]
    else:
        return array[column_index][row_index]

# Function to find the row index of a given address in the distances array
def address_location(package, distances):
    address = package.address
    for index, column in enumerate(distances):
        if address in column[0]:  # Addresses are in the first column
            return index

# Test data
package1 = myHash.search(1)
package2 = myHash.search(2)

# Find the row index of the first address
row_index = address_location(package1, distances)
# Find the column index of the second address
column_index = address_location(package2, distances)

distance = data_location(distances, row_index, column_index)
print("Distance between '{}' and '{}' = {}".format(package1.address, package2.address, distance))


class Truck:
    def __init__(self, speed, miles, address, depart_time, packages):
        self.speed = speed
        self.miles = miles
        self.address = address
        self.depart_time = depart_time
        self.time = 0
        self.packages = packages

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s" % (self.speed, self.miles, self.address, self.depart_time, self.time, self.packages)

# Manually loading trucks
# Time complexity O(1)
truckOne = Truck(18, 0.0, "4001 South 700 East", datetime.timedelta(hours = 8),[1,13,14,15,16,19,20,27,29,30,31,34,37,40])
truckTwo = Truck(18, 0.0, "4001 South 700 East", datetime.timedelta(hours = 11),[2,3,4,5,9,18,26,28,32,35,36,38])
truckThree = Truck(18, 0.0, "4001 South 700 East", datetime.timedelta(hours = 9, minutes = 5),[6,7,8,10,11,12,17,21,22,23,24,25,33,39])

