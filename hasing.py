# Introduction to Hashing
'''
Hashing - Hashing is the process of transforming data, such as text, numbers, and files, into a 
        unique string of characters and numbers.
        The data we are trying to convert is referred to as a key.
        The string we get after hashing is known as a hash value or hash code.

Hash Function - The function used to convert keys into hash values is called a hash function.

Application of Hashing:
    1. Searching
        Hashing is used to retrieve data efficiently. By using hashing, we can create a unique index for each value (key).
        Now, if we have to search for a value, we can use this unique index instead of the value itself. This approach results in a constant time complexity, O(1).

    2. Security
        In general, passwords should not be stored in plain text because if the database is compromised, the password will be exposed.
        Instead, passwords are hashed before being stored in a database. This way, even if the database is hacked, your password remains secure.
'''

# Hashing Techniques

'''
    Modular Hashing - This function uses modulus (remainder when divided by a number) to compute a key's hash value.
    
    Modular hashing ensures that the hash values are distributed within a fixed range
'''
class HashData:

    # initialize a list of 10 items
    def __init__(self):
        self.table = [None] * 10

    # compute hash
    def hash_function(self, key):
        return key % 10

    # insert data to hash table
    def put(self, key):

        hash_value = self.hash_function(key)
        self.table[hash_value] = key

    # retrieve key from hash table
    def retrieve(self, item):
        # Time Complexity : O(1)
        hash_value = self.hash_function(item)
        key = self.table[hash_value]

        return {"hash_value": hash_value, "key": key}
    
            
keys = [1, 300, 209, 117, 12]

hash1 = HashData()

# apply hash function to each key
for key in keys:
    hash1.put(key)

# retrieve values
print(hash1.retrieve(117))
print(hash1.retrieve(13))

# Hash Collision
'''
    Hash Collison - If two keys map to the same hash value, a collision occurs. 

    Hash Collision Resolution:
        1. Using a larger hash table
            If we use a larger hash table, we can accommodate more values without clashing.

        2. Modifying the hash function itself.
            We can modify the hash function itself to ensure that the hash values are unique.

    Load Factor :-
        -- The load factor is a measure of how full the hash table is.
        -- Load Factor (LF) = Number of items stored / Total Number of Slots 
        -- A load factor value close to 1 indicates that the hash table is nearly full. Similarly, a load factor close to 0 indicates 
        that the hash table is nearly empty.

    Rehashing :- 
            -- Rehashing means creating a new hash table with an increased size.
            -- We generally use rehashing if the load factor is greater than a certain value (let's say 0.75). 
            -- This helps to optimize the hash table's performance.
'''

class HashData:

    # initialize a list of 10 items
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size
        self.lf_threshold = 0.7

    # compute hash
    def hash_function(self, key):
        return key % self.size

    # insert data to hash table
    def put(self, key):
        # insert into table
        hash_value = self.hash_function(key)
        self.table[hash_value] = key
        
        # computer threshold during each insertion
        # current lf = occupied slot/total slots
        current_lf = sum(1 for slot in self.table if slot) / (self.size)
        # check if load factor exceeds after each insertion
        if current_lf >= self.lf_threshold:
            self.rehash()
            
    def rehash(self):
        # create a new hash table
        self.size = 2 * self.size
        new_table = [None] * self.size 
        # hash existing data into new table
        for data in self.table:
            if(data):
                hash_value = self.hash_function(data)
                new_table[hash_value] = data
        # update table
        self.table = new_table

    # display hash table
    def display(self):
        for hash_value, key in enumerate(self.table):
            print(f"{hash_value}: {key}")    

hash1 = HashData()

# keys
keys = [1, 300, 209, 17, 12, 24, 36]

# apply hash function to each key
for key in keys:
    hash1.put(key)

hash1.display()

# Hash Collision Resolution
'''
    Two of the most common strategies for collision resolution are:
        1. Separate Chaining
        2. Open Addressing
'''

#  Separate Chaining
'''
    Separate Chaining:
        The separate chaining technique resolves these collisions by utilizing linked lists.
        In this technique, each slot is a linked list. If two keys have the same hash, both will be placed into the same cell as items of a linked list.

    Time Complexity: O(ʎ)
'''

# a class to represent a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# a class to represent a linked list
class LinkedList:
    def __init__(self):
        self.head = None
    
    # return the linked list elements
    def traverse(self):
        current = self.head

        result = ""

        while current:
            result += (f"{current.data}->")
            current = current.next
        
        result += "None"

        return result   
    
    # append an item to the linked list
    def append(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
       
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

class HashData:

    # initialize a list of 10 items
    def __init__(self):
        self.table = [None] * 10

    # compute hash
    def hash_function(self, key):
        return key % 10

    # insert data to hash table
    def put(self, key):
        # insert into table
        hash_value = self.hash_function(key)
         # if the slot is empty	
        if not self.table[hash_value]:
            # create a linked list at the slot
            self.table[hash_value] = LinkedList()
        # append item to the linked list
        self.table[hash_value].append(key)

    # display hash table
    def display(self):
        for hash_value, key in enumerate(self.table):
            # if slot is a linked list
            if key: 
                print(f"{hash_value}: {key.traverse()}")
            # if slot is empty
            else:
                print(f"{hash_value}: {key}")

    # retrieve key from hash table
    def retrieve(self, item):

        hash_value = self.hash_function(item)
        key = self.table[hash_value]
        if key:
            current = key.head
            # when value is found, stop traversal
            while current:
                if current.data == item:
                    return {"hash_value": hash_value, "key": item}
                current = current.next
        return {"hash_value": hash_value, "key": None}

hash1 = HashData()

# keys
keys = [12, 17, 15, 4, 27, 14, 37]

# apply hash function to each key
for key in keys:
    hash1.put(key)

print(hash1.retrieve(12))
print(hash1.retrieve(47))

#  Open Addressing
'''
    Open Addressing:
        Open addressing resolves collisions by finding alternative locations within the existing hash table for collided elements.

        We will explore three open addressing methods in this lesson:
            Linear Probing
            Quadratic Probing
            Double Hashing

    Linear Probing
        When a collision occurs, linear probing searches for the next available slot in the hash table, moving linearly until an empty slot is found.
        The objective is to find the closest unoccupied position for the colliding item.

        The insertion process in linear probing can be broken down into two main steps:
            -- Attempt to insert the value at its corresponding key.
            -- If the key is already occupied, probe to the next index.

        # insert data to hash table
        def put(self, key):
            i = 0
            hash_value = self.hash_function(key)
            while self.table[hash_value]:
                # move to next slot until empty space is found
                i += 1
                hash_value = (self.hash_function(key) + i) % 10
            # insert into empty slot
            self.table[hash_value] = key 

        # retrieve data from hash table
        def retrieve(self, key):
            hash_value = self.hash_function(key)
            i = 0
            # continue searching until an empty slot is found
            while self.table[hash_value]:
                # if the required key is found, return its hash value and key
                if self.table[hash_value] == key:
                    return {"hash_value": hash_value, "key": key}
                # move to next slot
                i += 1
                hash_value = (self.hash_function(key) + i) % 10
                    
            # if key not in table, return None
            return {"hash_value": hash_value, "key": None}
    
    Limitations of Linear Probing
        While linear probing offers a simple approach to handle hash collisions, it comes with the following limitations:
        1. Difficulty in deleting values
            In order to delete an item after linear probing, we need to take out all other elements and rehash them again. This is not very feasible.
            Thus, we don't implement deletion operations at all from linear probing.

        2. Primary clustering
            Every time a collision happens, the position of the item is shifted one position down. When there are a lot of collisions around a small area, 
            the position of items can shift a lot. In such cases, the hash table may no longer provide constant time search operations. This is known as 
            primary clustering.

        To address the primary clustering problem, we use quadratic probing.
'''

# Quadratic Probing
'''
    Quadratic Probing
        When collisions happen, quadratic probing searches for the next available slot by using a quadratic term, like i^2, to place items farther apart compared 
        to linear probing.
        Here, instead of probing by i, we probe by i ** 2.

    # insert data to hash table
    def put(self, key):
        i = 0
        hash_value = self.hash_function(key)
        while self.table[hash_value]:
            i += 1
            hash_value = (self.hash_function(key) + i**2) % 10 # use i ** 2
        self.table[hash_value] = key 

    # retrieve data from hash table
    def retrieve(self, key):
        hash_value = self.hash_function(key)
        i = 0
        while self.table[hash_value]:
            if self.table[hash_value] == key:
                return {"hash_value": hash_value, "key": key}
            i += 1
            hash_value = (self.hash_function(key) + i**2) % 10 # use i ** 2
        return {"hash_value": hash_value, "key": None}

    Limitations of Quadratic Probing:
        -- The deletion operation still remains complex.
        -- quadratic probing introduces the possibility of secondary clustering, where items still cluster together despite using the quadratic increment.
'''

# Double Hashing
'''
    Double Hashing
        In double hashing, two hash functions are used to determine the probing sequence.
        The primary hash function calculates the initial index, while the secondary hash function determines the step size for probing.

    Double hash function:
        H(x) = (H1(x) + i * H2(x)) % table size
'''
class HashData:

    # initialize a list of 10 items
    def __init__(self):
        self.table = [None] * 10

    # compute hash
    def hash_function(self, key, i = 0):
        return (self.primary_hash_function(key) + i * self.secondary_hash_function(key)) % 10
        
    # primary hash function
    def primary_hash_function(self, key):
        return (key) % 10
    
    # secondary hash function
    def secondary_hash_function(self, key):
        return 1 + key % 9

    # insert data to hash table
    def put(self, key):
        i = 0
        hash_value = self.hash_function(key)
        while self.table[hash_value]:
            # handle collision by probing using secondary hash functio
            i += 1
            hash_value = self.hash_function(key, i) # use double hash
        # insert into the empty slot
        self.table[hash_value] = key   
    
    # display hash table
    def display(self):
        for hash_value, key in enumerate(self.table):
            print(f"{hash_value}: {key}")    
    
    # retrieve data from hash table
    def retrieve(self, key):
        hash_value = self.hash_function(key)
        i = 0
        while self.table[hash_value]:
             # if the required key is found, return its hash value and key
            if self.table[hash_value] == key:
                return {"hash_value": hash_value, "key": key}
            # move to the next slot using secondary hash function
            i += 1
            hash_value = self.hash_function(key, i) # use double hash
        # if the key is not found in the table, return None
        return {"hash_value": hash_value, "key": None}

'''
    Hash Functions:
       1. Modulus Hash Function
            You take a value and perform the modulus operation with the table size.
                H(x) = x % n
                where, n is the table size.

       2. Mid-Square Hash Function
            The mid-square hash function involves squaring a given number, extracting a portion of the resulting square, and using that portion as the hash value.
            Typically, the extracted portion is from the middle of the square, which is why it's called the mid-square hash function. This technique aims to distribute
            hash values more uniformly and reduce clustering.

            Example,
                12: The square of 12 is 144. Choosing the middle digit, we get 4.


       3. Folding Hash Function
            The folding hash function involves dividing a given number into segments, summing these segments, and using the resulting sum as the hash value.
            This technique spreads data more uniformly across hash table slots, reducing clustering and improving data storage efficiency.

            Example,
                12: Splitting into segments: 1 and 2. Adding segments: 1 + 2 = 3.

    Custom Hash function:
        H(x) = ASCII(x[0]) - 64
'''

# Applications of Hashing
'''
    Applications of Hashing:
        1. Python Dictionaries as Hash Tables
        2. Hashing Passwords

    Python Dictionaries as Hash Tables
        In Python, dictionaries are implemented as hash tables, which is why they have an average O(1) time complexity for lookup, insertion, and deletion.

        To understand how Python dictionaries work as hash tables, let's delve into some of the fundamentals:
            1. Hash Function: Python uses a specialized hash function called SipHash starting from Python 3.3.
            2. Collisions: Python handles collisions using an open addressing scheme similar to quadratic probing.
            3. Dynamic Resizing: As more items are added to a dictionary, the underlying hash table might become densely populated, leading to more collisions. 
                To handle this, Python dictionaries are designed to resize dynamically.
            4. Key Invariance: It's important to note that dictionary keys should be immutable. This is because if a key changes its value (and thus its hash) 
                after it's been added to the dictionary, it would make the value associated with it unreachable.

    Hashing Passwords:
        When users create accounts on websites, it's important that their passwords are stored securely. This is where hashing algorithms come into play.
        
        Instead of storing the plain-text password, systems store the hash of the password to make it more secure. Some popular algorithms like MD5, SHA-1, SHA-2 
        use hash to secure your passwords.
'''