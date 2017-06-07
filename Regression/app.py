from collections import Counter


def ransom_note(magazine, ransom):
    print(Counter(ransom.split(" ")))
    print(Counter(magazine.split(" ")))
    return Counter(ransom.split(" ")) - Counter(magazine.split(" ")) == {}


magazine = "give me one grand today night"
ransom = "give one grand today"
answer = ransom_note(magazine, ransom)

if answer:
    print("Yes")
else:
    print("No")
