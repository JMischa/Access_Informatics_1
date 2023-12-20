#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def analyze(posts):
    res = {}
    
    for strings in posts:
        words = strings.replace(".", " ").split()
        for word in words:
            if len(word) == 1:
                continue
            elif word.startswith("#") and len(word)>= 2:
                word = word[1:]
                if word[0].isdigit():
                    continue
                if word not in res:
                    res[word] = 1
                else:
                    res[word] += 1
            elif "#" in word and len(word) >= 2:
                x = word.find("#") + 1
                word = word[x:]
                if len(word[x:]) == 0 or word[x].isdigit() :
                    continue
                elif word not in res:
                    res[word] = 1
                else:
                    res[word] += 1
            else:
                continue

    
    return res
# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
posts = [
    "hi #weekend", "#",
    "good morning #zurich #limmat",
    "spend my #weekend in #Zu.rich",
    "#zurich <3", "-#d-", "#9234ksaf"]
print(analyze(posts))


