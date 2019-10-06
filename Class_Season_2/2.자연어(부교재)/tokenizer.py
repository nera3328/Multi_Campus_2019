# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:15:07 2019

@author: student
"""

from nltk.tokenize import LineTokenizer,SpaceTokenizer, TweetTokenizer
from nltk import word_tokenize

lTokernizer=LineTokenizer();
print('Line tokenizer 출력 : ', lTokernizer.tokenize('My name is Maximus Decimus Meridius, Commander of the Armies of the North, General of the Felix Legions, loyal servant to the true emperor, Marcus Aurelius. \nFather to a murdered son, husband to a murdered wife. \nAnd I will have my vengeance, in this life or the next.'))

rawtext="By 11 o'clock on Sunday, the doctor"
stokenizer=SpaceTokenizer()
print('SpaceTokenizer = ',stokenizer.tokenize(rawtext)) #띄어쓰기 단위
print('Word Tokenizer = ', word_tokenize(rawtext))# 문장 구두점, 띄어쓰기 단위
tTokenizer=TweetTokenizer()
print('Tweet token 출력 = ', tTokenizer.tokenize('This is a cooool #dummysiley: :-) :-p <3'))
