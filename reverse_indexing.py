__author__ = "Mischa Jampen"

# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
 ] 

def reverse_index(dataset):
    
    index_dictionary = {}
    
    for i, s in enumerate(dataset):
        words = s.lower().split()
        
        for word in words:
            if word not in index_dictionary:
                index_dictionary[word] = [i]
            
            else:
                index_dictionary[word].append(i)

    return index_dictionary


# You can see the output of your function here
print(reverse_index(dataset))
