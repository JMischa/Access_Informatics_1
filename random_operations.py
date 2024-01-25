import random

values = [1,2,3,4]

draw = random.sample(range(1,51), k=len(values))

print(draw) # ex. == [39, 11, 7, 37]
