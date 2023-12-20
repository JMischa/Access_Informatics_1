#!/usr/bin/env python3

class ProfanityFilter:

    def __init__(self, keywords, template):
        self.keywords = reversed(sorted([kw.lower() for kw in keywords]))
        self.template = template

    def filter(self, msg):
        msg_lower = msg.lower()
        for word in self.keywords:
            while word in msg_lower:
                idx = msg_lower.find(word)
                msg = self.replace(msg, idx, word)
                msg_lower = self.replace(msg_lower, idx, word)
        return msg

    def replace(self, s, idx, word):
        clean_word = self.escape(word)
        return s[:idx] + clean_word + s[idx+len(clean_word):]

    def escape(self, word):
        res = ""
        for idx, _ in enumerate(word):
            t_idx = idx % len(self.template)
            res += self.template[t_idx]
        return res

# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc defghi mastard jklmno"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno