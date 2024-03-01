class hash_table:
    # initing arry and make the whole element in the array as None and setting the size
    def __init__(self,size):
        self.size = size
        self.array = [None for i in range(self.size)]
    # defining hash function and converting the key into the hash using ascci method and the division method
    def hash_function(self,key):
        h = 0
        for i in key:
            h = h + ord(i)
        return h % self.size

    # add element in the hash table in specific position which depends on the key coming
    # this function will get the value  of the key that came as an argument of the functioin
    def get(self, key):
        # index = self.hash_function(key)
        # Search for the key in the hash table
        for i in range(len(self.array)):

            if self.array[i] and self.array[i][0] == key:  # Check if key is found
                print(self.array[i])  # Return the corresponding value
         # Key not found

    #     delete the element in a postion that indicated by the key coming
    def delete(self,key):
        # position = self.hash_function(key)
        for i in range(len(self.array)):

            if self.array[i] and self.array[i][0] == key:  # Check if key is found
                self.array[i] = None


#     showing the elements in the array
    def display(self):
        for i in range(len(self.array)):
            print(self.array[i])

    def add_element(self, key, value):
        position = self.hash_function(key)
        if self.array[position] != None:
            self.array[position] = (key, value)
            return
        next_index = (position + 1) % self.size
        while next_index != position:
            if self.array[next_index] is None:
                self.array[next_index] = (key,value)
                return
            next_index = (next_index+1) % self.size
        print("The hash table is empty")






my_hash_table = hash_table(10)
my_hash_table.add_element("name","muhammed")
my_hash_table.add_element("name","sajal")
my_hash_table.add_element("name","aljshdf")

my_hash_table.add_element("address","kkm")
my_hash_table.add_element("age","12")

result = my_hash_table.get("name")
if result:
    print(result)
print()
print("the hash table is ")
my_hash_table.delete("name")
my_hash_table.display()


