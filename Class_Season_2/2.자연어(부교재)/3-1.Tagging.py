# POS Tagging
import nltk

# 태깅
text = "And now for something completely different"
token = nltk.word_tokenize(text)
nltk.pos_tag(token) 

text2 = "They refuse to permit us to obtain the refuse permit"
token2 = nltk.word_tokenize(text2)
nltk.pos_tag(token2) 


