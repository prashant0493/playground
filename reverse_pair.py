'''Reverse pair of two words. Function checks if two words are reverse pair of each other'''
def rev_pair(word1, word2):
    if word1[::-1]==word2[::]:
        return True
    else:
        return False

word1=input("Give word 1:->")
word2=input("Give me word 2:->")
print(rev_pair(word1,word2))
