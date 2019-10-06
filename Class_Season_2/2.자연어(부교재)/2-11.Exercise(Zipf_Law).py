# 지프의 법칙 (Zipf's Law)
# f(w) : 단어 w의 빈도
# rank(w) : 단어 w의 빈도 순위
# f(w) ~ 1/rank(w)
# log(f) = -1 * log(rank) : 기울기가 -1인 직선
import nltk
import numpy as np
from matplotlib import pyplot as plt
text = nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
fdist = nltk.FreqDist(text)
print(fdist)

x = np.arange(1, len(fdist) + 1)
y = sorted(list(fdist.values()), reverse=True)
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.xlim(1, 100)
plt.show()

plt.figure(figsize=(10, 6))
logx = np.log(x)
logy = np.log(y)
plt.plot(logx, logy)
plt.show()

print("기울기 = ", np.polyfit(logx, logy, 1)[0])

