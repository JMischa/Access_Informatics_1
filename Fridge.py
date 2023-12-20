# Author: Mischa Jampen
class Fridge:
    
    def __init__(self):
        self.__items = []

    def store(self, item):
        self.__items.append(item)
        
    def take(self, item):
        if item not in self.__items:
            raise Warning("item is not in the fridge")
        else:
            self.__items.remove(item)
            return item
 
    def find(self, name):
        for n, date in sorted(self.__items):
            if n == name:
                return (n,date)
            return None
    
    def take_before(self, date):
        items = []
        for i in self.__items:
            if i[0] < date:
                self.__items.remove(i)
                items.append(i)
        return items
                
    def __iter__(self):
        return iter(sorted(self.__items))

    def __len__(self):
        return len(self.__items)
    


f = Fridge()
f.store((191127, "Butter"))
f.store((191117, "Milk"))
f.take((191127, "Butter")) # ok
f.take((191207, "Bread")) # fails

    
