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

    def insert(self, key, address, city, state, zipcode, deadline, weight, notes):  # does both insert and update
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
                kv[7] = notes
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, address, city, state, zipcode, deadline, weight, notes]
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
                return kv[1], kv[2], kv[3], kv[4], kv[5], kv[6], kv[7]  # value
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


bestMovies = [
    [1, "195 Street", "Salt Lake City", "UT", 84115, "10:30AM", 21, ""],
    [2, "CASABLANCA - 1942"],
    [3, "THE GODFATHER - 1972"],
    [4, "GONE WITH THE WIND - 1939"],
    [5, "LAWRENCE OF ARABIA - 1962"],
    [6, "THE WIZARD OF OZ - 1939"],
    [7, "THE GRADUATE - 1967"],
    [8, "ON THE WATERFRONT- 1954"],
    [9, "SCHINDLER'S LIST -1993"],
    [10, "SINGIN' IN THE RAIN - 1952"],
    [11, "STAR WARS - 1977"]
]

myHash = ChainingHashTable()

print("\nInsert:")
myHash.insert(bestMovies[0][0], bestMovies[0][1], bestMovies[0][2], bestMovies[0][3], bestMovies[0][4], bestMovies[0][5], bestMovies[0][6], bestMovies[0][7])
print(myHash.table)


print("\nSearch:")
print(myHash.search(1))

print("\nRemove:")
myHash.remove(1)
print(myHash.table)

