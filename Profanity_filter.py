__author__ = "Mischa Jampen"

class ProfanityFilter:

    def __init__(self, keywords, template):
        self.keywords = [kw.lower() for kw in keywords]
        self.template = template

    def filter(self, msg):
        filtered_msg = []
        for word in msg.lower().split():
            filtered_word = word
            for kw in self.keywords:
                if word == kw:
                    num_repetition = len(kw) // len(self.template)
                    remainder = len(kw) % len(self.template)
                    filtered_word = self.template * num_repetition + self.template[:remainder]
                    break
            filtered_msg.append(filtered_word)
                
        return " ".join(filtered_msg)
# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc defghi mastard duck jklmno"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno

    