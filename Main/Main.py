# Philip Audet - Student ID: 001098879
import csv
import datetime


# HashTable class using chaining.
# Ref: zyBooks: Figure 7.8.2: Hash table using chaining
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
    def __init__(self, ID, address, city, state, zipcode, deadline, weight, status, departureTime, deliveryTime):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.departureTime = None
        self.deliveryTime = None

    # overwrite print(Package) otherwise it will print object reference
    # Time complexity O(1)
    def __str__(self):
        return (f"Package ID: {self.ID} \t| Address: {self.address} \t| {self.city}, {self.state}, {self.zipcode} | "
                f"Deadline: {self.deadline} | Weight: {self.weight} | Status: {self.status} | Departure"
                f" Time:  {self.departureTime} | Delivery Time:  {self.deliveryTime}")

    # Update status of each package depending on time entered by user.
    def changeStatus(self, timeDifference):

        # Change package status based on time difference
        if self.deliveryTime is None or (self.departureTime is not None and timeDifference < self.departureTime):
            self.status = "At Hub"
        elif timeDifference < self.deliveryTime:
            self.status = "Out For Delivery"
        else:
            self.status = "Delivered"

        # Package 9 address change
        if self.ID == 9:
            if timeDifference >= datetime.timedelta(hours=10, minutes=20):
                self.address = "410 S. State St"
                self.zipcode = "84111"
            else:
                self.address = "300 State St"
                self.zipcode = "84103"


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
            pDepartureTime = None
            pDeliveryTime = None

            # package object
            package = Package(pID, pAddress, pCity, pState, pZipcode, pDeadline, pWeight, pStatus, pDepartureTime,
                              pDeliveryTime)

            # Insert into the hash table
            myHash.insert(pID, package)


# Hash table instance
# Time complexity O(1)
myHash = ChainingHashTable()

# Load packages to Hash Table
# Time complexity O(1)
loadPackageData('WGUPSPackageFile.csv')

# Read Distances csv and converting to a list of lists (2d array)
# Time complexity: O(N)
filepath = 'Distances.csv'
with open(filepath, newline='') as distancesFile:
    distanceR = csv.reader(distancesFile, delimiter=',')
    distanceR = list(distanceR)

# Reading Addresses CSV
# Time complexity O(N)
filename = 'Addresses.csv'
with open(filename, newline='') as addressesFile:
    addressR = csv.reader(addressesFile, delimiter=',')
    addressR = list(addressR)


# Find address information
# Time complexity O(N)
def address_location(address):
    for row in addressR:
        if address in row[2]:
            return int(row[0])


# Find distances between two addresses
# Time complexity O(1)
def data_location(address1, address2):
    distance = distanceR[address1][address2]
    if distance == '':
        distance = distanceR[address2][address1]
    return float(distance)


# Creating Truck class and string representation
# Time complexity O(1)
class Truck:
    def __init__(self, speed, miles, address, depart_time, packages):
        self.speed = speed
        self.miles = miles
        self.address = address
        self.depart_time = depart_time
        self.time = depart_time
        self.packages = packages

    def __str__(self):
        return f"{self.speed}, {self.miles}, {self.address}, {self.depart_time}, {self.time}, {self.packages}"


# Manually loading trucks
# Time complexity O(1)
truckOne = Truck(18, 0.0, "4001 South 700 East", datetime.timedelta(hours=8),
                 [1, 13, 14, 15, 16, 19, 20, 27, 29, 30, 31, 34, 37, 40])
truckTwo = Truck(18, 0.0, "4001 South 700 East", datetime.timedelta(hours=11),
                 [2, 3, 4, 5, 9, 18, 26, 28, 32, 35, 36, 38])
truckThree = Truck(18, 0.0, "4001 South 700 East", datetime.timedelta(hours=9, minutes=5),
                   [6, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 25, 33, 39])


# Package delivery function using nearest neighbor algorithm
# Time complexity O(N^2)
def packageDelivery(truck):
    # Generates an array which contains all the packages that need to be delivered
    undeliveredPackages = []

    # Loads each package based on ID into the above array
    for packageID in truck.packages:
        package = myHash.search(packageID)
        undeliveredPackages.append(package)

    # Loop while there are still packages in the array.
    while len(undeliveredPackages) >= 1:
        upcomingAddress = float('inf')
        upcomingPackage = None

        # Calculate the next package utilizing shortest distance
        for package in undeliveredPackages:
            distance = data_location(address_location(truck.address), address_location(package.address))
            # Packages 6 and 25 must be delivered before 10:30am and do not arrive at the depot until 9:05am, so they
            # must be prioritized on the second truck to go out.
            if package.ID in [6, 25]:
                upcomingPackage = package
                upcomingAddress = distance
                break
            if distance <= upcomingAddress:
                upcomingAddress = distance
                upcomingPackage = package

        # Add the upcoming package to the truck object
        truck.packages.append(upcomingPackage.ID)
        # Remove upcoming package from Undelivered Package array
        undeliveredPackages.remove(upcomingPackage)
        # Add the travelled distance to the truck's mileage
        truck.miles += upcomingAddress
        # Update the truck's address to current location
        truck.address = upcomingPackage.address
        # Update the time based on how far the truck travelled divided by its speed
        truck.time += datetime.timedelta(hours=upcomingAddress / truck.speed)
        # Update upcoming package departure and delivery times based on truck's departure and total time
        upcomingPackage.departureTime = truck.depart_time
        upcomingPackage.deliveryTime = truck.time


# Initiates the beginning of package delivery for first and third trucks
# Time complexity O(N^2)
packageDelivery(truckOne)
packageDelivery(truckThree)

# Truck 2 will not depart until the first or third truck returns.
truckTwo.depart_time = min(truckOne.time, truckThree.time)

# Initiates the beginning of package delivery for second trunk
# Time complexity O(N^2)
packageDelivery(truckTwo)

# User Interface which will display a menu until an option is chosen.
while True:

    print("   Menu Options:   ")
    print("*******************")
    print("1: Get total mileage")
    print("2: Get individual package status with a time")
    print("3: List all package statuses with a time")
    print("4: Exit")
    print("*******************")
    choice = input("Please enter a selection: ")

    # Display the miles driven by all the delivery trucks.
    if choice == "1":
        print("The total mileage driven by Trucks 1, 2, and 3 is: ",
              (truckOne.miles + truckTwo.miles + truckThree.miles))
        continue
    # Ask the user to input a valid time using specified format
    if choice == "2" or choice == "3":
        while True:
            try:
                inputTime = input("Enter the desired time to view the status of a package. Use the format HH:MM: ")
                (h, m) = map(int, inputTime.split(":"))
                timeDifference = datetime.timedelta(hours=h, minutes=m)
                break
            # Throw error if time format is not followed.
            except ValueError:
                print("Invalid time format. Please try again using the format HH:MM")
                continue
        # Ask the user for a specific package ID
        if choice == "2":
            packageEntry = input("Input the desired Package ID to see its status: ")
            if packageEntry.strip() == "":
                packageEntry = range(1, 41)
            else:
                try:
                    packageEntry = [int(packageEntry)]
                # Throw error if package ID is not valid
                except ValueError:
                    print("Invalid Package ID. Please try again.")
                    continue
            # Display package attributes based on time and ID selected
            for packageID in packageEntry:
                package = myHash.search(packageID)
                package.changeStatus(timeDifference)
                print(str(package))

        elif choice == "3":
            # Display all packages and their attributes based on time selected
            for packageID in range(1, 41):
                package = myHash.search(packageID)
                package.changeStatus(timeDifference)
                print(str(package))
    # Exit program
    elif choice == "4":
        break

    # Ask user to try again if invalid selection made on the main menu.
    else:
        print("Invalid selection. Please try again.")
