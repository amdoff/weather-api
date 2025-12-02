class Mylist(list):
    def remove(self, value):
        while value in self:
         super().remove(value)
lst = Mylist ([1, 2, 3, 1, 2, 2, 21, 1, 2, 2, 3, 2, 1])
lst.remove(2)
print(lst)        
