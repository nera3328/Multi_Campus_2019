# Regular Expression 연습
import nltk
import re

# 영어 단어 목록
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]

v = [w for w in wordlist if re.search('ed$', w)]
print(v[:20])

v = [w for w in wordlist if re.search('^..j..t..$', w)]
print(v[:20])

# 전화기 문자판 (textonyms)
v = [w for w in wordlist if re.search('^[ghi][mno][jlk][def]$', w)]
print(v[:20])

# NPS Chat corpus
chat_words = sorted(set(w for w in nltk.corpus.nps_chat.words()))
v = [w for w in chat_words if re.search('^m+i+n+e+$', w)]
print(v[:20])

v= [w for w in chat_words if re.search('^[ha]+$', w)]
print(v[:20])

# Penn Treebank corpus
wsj = set(nltk.corpus.treebank.words())
v = [w for w in wsj if re.search('^[0-9]+\.[0-9]+$', w)]
print(v[:30])

v = [w for w in wsj if re.search('^[A-Z]+\$$', w)]
print(v[:20])

v = [w for w in wsj if re.search('^[0-9]{4}$', w)]
print(v[:20])

v = [w for w in wsj if re.search('^[0-9]+-[a-z]{3,5}$', w)]
print(v[:20])

v = [w for w in wsj if re.search('^[a-z]{5,}-[a-z]{2,3}-[a-z]{,6}$', w)]
print(v[:20])

v = [w for w in wsj if re.search('(ed|ing)$', w)]
print(v[:20])

word = 'supercalifragilisticexpialidocious'
re.findall(r'[aeiou]', word)
len(re.findall(r'[aeiou]', word))

wsj = sorted(set(nltk.corpus.treebank.words()))
fd = nltk.FreqDist(vs for word in wsj 
                   for vs in re.findall(r'[aeiou]{2,}', word))
fd.most_common(12)
