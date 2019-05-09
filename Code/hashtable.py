#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(l) because we loop through the buckets and all their items"""
        
        # Collect all keys in each bucket
        all_keys = []

        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(l) because we loop through the buckets and all their items"""
        
        all_values = []

        # Loop through all buckets
        for bucket in self.buckets: # b iterations
            for key, val in bucket.items():
        #Collect all values in each bucket
                all_values.append(val)
        return all_values
        
    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) because we loop through the buckets and all their items"""

        # list to store key,val entries
        all_items = [] #O(1)
        
        #loop through buckets
        for bucket in self.buckets: # b iterations => O(b * l) => O(n)
            items = bucket.items() # O(l) where l = length of list
            all_items.extend(items)
        #Collect all pairs of key-value entries in each bucket
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(b * l) --> O(n) b/c for each bucket you go to every node
        where b is # of buckets, and n is number of entries"""

        length = 0

        #Loop through all buckets
        for bucket in self.buckets: #b iterations of a loop
        #Count number of key-value entries in each bucket
            length += bucket.length() # O(l) => l = n/b
        return length # O(n)

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
           Running time: O(l) where l is the length of bucket due to find method """
        
        #Find bucket where given key belongs
        index = self._bucket_index # O(1) to calculate index
        bucket = self.buckets[index(key)] # O(1) to index array

        #Check if key-value entry exists in bucket
        key_matcher = lambda key_val: key_val[0] == key
        entry_found = bucket.find(key_matcher) # 0(l) with l = bucket.length()
        
        #check if entry was found and return results
        return entry_found is not None # O(1)
        
    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: O(l) because it depends on the length of hash table"""

        #Find bucket where given key belongs
        index = self._bucket_index # O(1) to calculate index
        bucket = self.buckets[index(key)] 

        #Check if key-value entry exists in bucket
        key_matcher = lambda key_val: key_val[0] == key
        entry_found = bucket.find(key_matcher) # 0(l) with l = bucket.length()

        #If found, return value associated with given key
        if entry_found is not None:
            return entry_found[1]
        #Otherwise, raise error to tell user get failed
        else:
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(l) because it depends on length of buckets"""

        #Find bucket where given key belongs
        index = self._bucket_index # O(1) to calculate index
        bucket = self.buckets[index(key)] # O(1) to index array

        #Check if key-value entry exists in bucket
        key_matcher = lambda key_val: key_val[0] == key
        entry_found = bucket.find(key_matcher) # 0(l) with l = bucket.length()

        #If found, update value associated with given key
        if entry_found is not None: 
            bucket.delete(entry_found) # O(l)
                
        #Otherwise, insert given key-value entry into bucket
        new_entry = (key, value) # O(1)
        bucket.append((new_entry)) # O(1)

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
           Running time: O(l) where l = buckets.length()"""

        #Find bucket where given key belongs
        index = self._bucket_index
        bucket = self.buckets[index(key)]

        #Check if key-value entry exists in bucket
        key_matcher = lambda key_val: key_val[0] == key
        entry_found = bucket.find(key_matcher)

        #If found, delete entry associated with given key
        if entry_found is not None:
            bucket.delete(entry_found)

        #Otherwise, raise error to tell user delete failed
        else:
            raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
