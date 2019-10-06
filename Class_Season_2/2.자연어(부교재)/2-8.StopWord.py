# 불용어 : Stop Words
import nltk
from nltk.corpus import stopwords

# 영어의 Stop words를 확인한다.
stopWords = stopwords.words('english')
print(stopWords[:20])

# 영어 소설에서 Stop word를 제거한다.
text = nltk.corpus.gutenberg.words('austen-sense.txt')
removedStopWord = [w for w in text if w.lower() not in stopWords]
print(removedStopWord[:20])

# text에서 stop word를 제거한 word의 비중을 확인한다
print("비율 = ", len(removedStopWord) / len(text))


