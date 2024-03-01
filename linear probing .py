class hash_table:
    def __init__(self,size):
        self.size  = size
        self.array = [None for i in range(self.size)]
    def hash_fuction(self,key):
        h = 0
        for i in  key:
            h = h+ord(i)
        return  h % self.size

    def insert(self,key,value):
        index  = self.hash_fuction(key)
        if self.array[index]  is None:
            self.array[index] = (key,value)
            return
        next_index = (index+1) % self.size
        while next_index != index:
                if self.array[next_index] == None:
                    self.array[next_index] = (key,value)
                    return
                else:
                    next_index = (next_index+1) % self.size
        print("the hash table is fully filled")
    def delete(self,key):
        for i in range(len(self.array)):
            if self.array[i] and self.array[i][0] == key:
                self.array[i] = None

    def display(self):
        for i in self.array:
            print(i)

    def get(self,key):
        for i in range(len(self.array)):
            if self.array[i] and self.array[i][0] == key:
                print(self.array[i])
        print("The element is not present in the hash table")

l = hash_table(10)
l.insert("name","muhammed")
l.insert("age","12")
l.insert("name","sajal")
l.delete("name")
l.get("age")
l.display()
