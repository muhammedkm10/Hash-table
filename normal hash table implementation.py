class hash_tabla:
    def __init__(self,size):
        self.size = size
        self.array = [None for i in range(self.size)]

    def hash_function(self,key):
        h = 0
        for char in key:
            h  = h+ord(char)
        return  h % self.size
    def insert(self,key,value):
        index = self.hash_function(key)
        self.array[index] = (key , value)
    def get(self,key):
        index = self.hash_function(key)
        return self.array[index]
    def delete(self,key):
        index = self.hash_function(key)
        self.array[index] = None
    def displey(self):
        for i in range(len(self.array)):
            print(self.array[i])


h1 = hash_tabla(10)
h1.insert("name","muhammed")
h1.insert("age","12")
h1.insert("address","kkm")
print('the hash table elements are:')


p = h1.get("name")
print(f"the name is {p}")

h1.delete("name")

h1.displey()