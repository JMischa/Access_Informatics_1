

class Character:

    def __init__(self, name, lvl):
        self.__name = name
        self.__lvl = lvl
        self._health_max = 50 + (lvl -1) * 50
        self._health_cur = self._health_max
        
    def get_name(self):
        return self.__name

    def get_lvl(self):
        return self.__lvl
    
    def get_health(self):
        return (self._health_cur, self._health_max)
    
    def attack(self, other):
        damage = round(self.__lvl * 10 - other.__lvl)
        other._take_physical_damage(damage)

    def __repr__(self):
        return "{} (level {}): {} / {}".format(self.__name, self.__lvl, self._health_cur, self._health_max)
    
    def _get_caused_dmg(self, other):
        pass

    def _take_physical_dmg(self, amount):
        self._health_cur -= amount
        if self._health_cur < 0 :
            self._health_cur = 0

    def _take_magical_dmg(self, amount):
        self._health_cur -= amount
        if self._health_cur < 0:
            self._health_cur = 0
    
    def is_alive(self):
        return self._health_cur > 0


class Knight(Character):
    def __init__(self, name, lvl):
        super().__init__(name, lvl)
    
    def attack(self, other):
        damage = round((self.__lvl * 10 + self.__lvl - other.__lvl) * 0.8)
        other._take_physical_damage(damage)

    def __repr__(self):
        return super().__repr__()

class Mage(Character):
    def __init__(self, name, lvl):
        super().__init__(name, lvl)
    
    def attack(self, other):
        damage = round((self.__lvl *10 + self.__lvl - other.__lvl) * 1.25)
        other._take_magical_damage(damage)
    
    def _take_physical_dmg(self, amount):
        super()._take_physical_dmg(round(amount * 1.5))
    
    def _take_magical_dmg(self, amount):
        super()._take_magical_dmg(round(amount +1.5))
    
    def __repr__(self):
        return super().__repr__()

class Rogue(Character):
    def __init__(self, name, lvl):
        super().__init__(name, lvl)

    def attack(self, other):
        damage = round((self.__lvl * 10 + self.__lvl - other.__lvl))
        other._take_physical_damage(damage)

    def __repr__(self):
        return super().__repr__()
#!/usr/bin/env python3


# The purpose of this file is illustrating the class usages. This script
# is irrelevant for the grading and you can freely change its contents.

def attack(c1, c2):
    print("{} attacks {} ".format(c1, c2), end="")

    if not c2.is_alive():
        print("{} is beating a dead horse!".format(c1.get_name()))
        return

    life_before = c2.get_health()[0]
    c1.attack(c2)
    life_after = c2.get_health()[0]
    dmg = life_before-life_after

    print("and hits for {} damage. ".format(dmg), end="")

    if c2.is_alive():
        life = c2.get_health()
        perc = round(100 * life[0] / life[1], 1)
        print("{} still has {} ({}%) health".format(c2.get_name(), life[0], perc))
    else:
        print("{} died!".format(c2.get_name()))


# IMPORTANT: The following two lines stop the script at this point.
# This is because implementation details are missing, until you implement them.
# Delete the following two lines if you want to run the rest of the code!

k = Knight("Arthur", 12)
m = Mage("Gandalf", 12)
r = Rogue("Shades", 11)

attack(r, m)
attack(m, r)
attack(k, m)

attack(r, m)
attack(m, k)
attack(k, m) # Gandalf dies
attack(r, m)  # Shades is attacking a dead character

while r.is_alive() and k.is_alive():
    attack(r, k)
    if k.is_alive():
        attack(k, r)

winner = r.get_name() if r.is_alive() else k.get_name()
print("{} wins the battle!".format(winner)) # Arthur
