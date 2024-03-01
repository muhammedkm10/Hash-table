class hash_table:
    def __init__(self,size):
        self.size = size
        self.array = [[] for i in range(self.size)]
    def  hash_function(self,key):
        h = 0
        for i in key:
            h = h+ ord(i)
        return h % self.size

    def insert(self,key,value):
        index = self.hash_function(key)
        found = False
        for i,key_val in enumerate(self.array[index]):
            if key_val[0] == key:
                self.array[index][i] = (key,value)   #if we found the key name in the chain then updating it
                found = True
                break
        if not found:
            self.array[index].append((key,value))  #if we could Not find the key then adding a new value in the chain

    def delete(self,key):
        index = self.hash_function(key)
        for i,key_val in enumerate(self.array[index]):
            if key_val[0] == key:
                del self.array[index][i]
                return True
        else:
            return False
    def display(self):
        for i in self.array:
            print(i)

    def get(self,key):
        index = self.hash_function(key)
        for i in self.array[index]:
            if i[0] == key:
                return i[1]
        else:
            return None




l  = hash_table(10)
l.insert("name","muhammed")
l.insert("age","12")
l.insert("nema","sajal")
l.delete("name")
l.display()


p = l.get("name")
print(p)

