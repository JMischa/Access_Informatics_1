__author__ = "Mischa Jampen"
#!/usr/bin/env python3

class Inventory:
    def __init__(self, player_name = "DEFAULT", balance = 0, max_weight = 0):
        self.__player_name = player_name
        self.__balance = balance
        self.__max_weight = max_weight
        self.__content = []

    def collect(self, item):
        self.__proper_item(item)    
        if self.get_inv_weight()+ item[2] > self.__max_weight:
            raise Warning("max weight exceeded")
        else:
            self.__content.append(item)
    
    def get_player_name(self):
        return self.__player_name

    def get_inv_weight(self):
        return sum(i[2] for i in self.__content)

    def get_balance(self):
        return self.__balance

    def get_inv_value(self):
        return sum(i[1] for i in self.__content)

    def drop(self, item):
        self.__proper_item(item)
        if item in self.__content:
            self.__content.remove(item)
            return item
        else:
            raise Warning


    def sell(self, item):
        self.__proper_item(item)
        if item in self.__content:
            self.__balance += item[1]
            self.__content.remove(item)
            return item
        else:
            raise Warning

    def buy(self, item):
        self.__proper_item(item)
        if self.__balance >= item[1] and self.get_inv_weight() + item[2] <= self.__max_weight:
            self.__content.append(item)
            self.__balance -= item[1]
        else:
            raise Warning
#implement this function to check if a given object fits the described type for an item (3-tuple of string, int, int)
#raise a Warning if it doesn't
    def __proper_item(self, item):
        if not isinstance(item, tuple) or len(item) != 3 or not isinstance(item[0], str) or not isinstance(item[1], int) or not isinstance(item[2], int):
            raise TypeError

    def __iter__(self):
        return iter(sorted(self.__content, key=lambda item: item[1], reverse=True))

    def __len__(self):
        return len(self.__content)

# print_statements, do not submit the following lines.
if __name__ == "__main__":

    inv = Inventory("Great player name",  max_weight=300)
    inv.collect(("butter knife", 2, 1))
    inv.collect(("mighty sword", 500, 25))
    print(inv.drop(("butter knife", 2, 1))) # ok
    print(inv.get_inv_weight())
    #inv.drop(("yellow spork", 10_000, 1)) # fails
    #inv.sell(("butter knife", 2, 1)) # increases the balance by 2 and removes the item from the inventory
    #inv.buy(("mighty shield", 2, 10))

    #print("Items in the inventory:")
    #for item in inv:
        #print("{} with a value of {} and a weight of {}".format(item[0], item[1], item[2]))