import re
words=open("words.txt").read().lower().split("\n")
def is_strong_password(word):

    words_password = re.findall(r'\b\w{4,}\b', re.sub(r'\d', '.', word))
    for word_pas in words_password:
        if word_pas.lower() in words:
            return False
    return True


print(is_strong_password("123123."))

