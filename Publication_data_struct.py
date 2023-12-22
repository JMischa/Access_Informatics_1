__author__ = "Mischa Jampen"
import json
# The signatures of this class and its task methods are required for the automated grading to work.
# You must not change the names or the list of parameters.
# You may introduce grading/protected utility methods though.
class Publication:

    def __init__(self, authors, title, year):
        self.__authors = authors
        self.__authors = json.dumps(self.__authors)
        self.__title = title
        self.__year = year

    # To implement the required functionality, you will also have to implement several
    # of the special functions that typically include a double underscore.
    # We've provided a starting point for one of the operators:
    def __le__(self, other) -> bool:
        if not isinstance(other, Publication):  # complete this implementation and add all the other necessary operators!
            return NotImplemented
        return self.less(other) or self.equal(other)
        
    def __eq__(self, other) -> bool:
        if not isinstance(other, Publication):
            return NotImplemented
        return self.equal(other)

    def __gt__(self,other) -> bool:
        if not isinstance(other, Publication):
            return NotImplemented
        return not (self.less(other) or self.equal(other))

    def __lt__(self,other) -> bool:
        if not isinstance(other, Publication):
            return NotImplemented
        return self.less(other)

    def __ge__(self,other) -> bool:
        if not isinstance(other, Publication):
            return NotImplemented
        return not self.less(other)

    def __ne__(self, other) -> bool:
        if not isinstance(other, Publication):
            return NotImplemented
        return not self.equal(other)

    def __hash__(self):
        return self.calculate_hash()
    
    def calculate_hash(self) -> int:
        return hash(tuple(self.__authors) + (self.__title, str(self.__year)))
    
    def equal(self, other) -> bool:
        return self.calculate_hash() == other.calculate_hash()
    
    def less(self, other) -> bool:
        if self.get_authors() == other.get_authors():
            if self.get_title() == other.get_title():
                return self.get_year() < other.get_year()
            else:
                return self.get_title() < other.get_title()
        else:
            return self.get_authors() < other.get_authors()

    def get_authors(self):
        copy = [i for i in tuple(self.__authors)]
        return list(copy)
         
    def get_title(self):
        return self.__title
    
    def get_year(self):
        return self.__year
    
    def __str__(self):
        
        return f"Publication({self.__authors}, \"{self.__title}\", {self.__year})"
    
    def __repr__(self):
        return f"Publication({self.__authors}, \"{self.__title}\", {self.__year})"


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    references = [
        Publication(["Gamma", "Helm", "Johnson", "Vlissides"], "Design Patterns", 1994),
        Publication(["Cockburn"], "Writing Effective Use Cases", 2000),
        Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    ]

    p = Publication(["Duvall", "Matyas", "Glover"], "Continuous Integration", 2007)
    s = "Publication([\"Duvall\", \"Matyas\", \"Glover\"], \"Continuous Integration\", 2007)"
    print(p)
    print(str(p) == s)

    p1 = Publication(["A"], "B", 1234)
    p2 = Publication(["A"], "B", 1234)
    p3 = Publication(["B"], "C", 2345)
    p4 = Publication(["A", "B", "C"], "B", 1234)
    p5 = Publication(["A", "B", "C"], "B", 2345)
    print(p1 == p2)  # True
    print(p2 == p3)  # False
    print(p1 < p4)   # False 
    print(p4 < p5)   # True


    sales = {
        p1: 273,
        p2: 398,
    }
