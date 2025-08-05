from django.test import TestCase
from collections import Counter
# Create your tests here.
fulltext = "홍길동 홍길동 아자"
strlength = len(fulltext) # 글자수
words = fulltext.split() # 단어리스트
wordcnt = len(words) # 단어수
# words_dict = dict(Counter(words)) # 단어카운트
words_dic = dict()
for word in words:
    if word in words_dic.keys():
        words_dic[word] += 1
    else:
        words_dic[word] = 1

print("글자수 :",strlength)
print("단어수 :",wordcnt)
# print("단어 카운트 :",words_dict)
print("단어 카운트 :",words_dic)
print("출현 단어 :",words_dic.items())