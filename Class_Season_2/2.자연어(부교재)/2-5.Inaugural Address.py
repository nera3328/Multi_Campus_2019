# Inaugural Corpus 데이터를 읽어온다
from nltk.corpus import inaugural

# Inaugural 코퍼스의 파일 ID를 조회한다.
textId = inaugural.fileids()
print(textId[:10])

# 원시 문서를 읽는다
text = inaugural.raw('1789-Washington.txt')
print(text[:500])

# 연도별로 'america'와 'citizen'이란 단어가 사용된 빈도의
# 변화를 관찰한다.
import nltk
cfd = nltk.ConditionalFreqDist(
        (target, fileid[:4])
        for fileid in inaugural.fileids()
        for w in inaugural.words(fileid)
        for target in ['america', 'citizen']
        if w.lower().startswith(target)
        )
cfd['america']
cfd['citizen']
cfd.plot()

#import matplotlib.pyplot as plt
#plt.figure(figsize=(10,6))
#
#america = sorted(dict(cfd['america']).items())
#citizen = sorted(dict(cfd['citizen']).items())
#x1, y1 = zip(*america)
#x2, y2 = zip(*citizen)
#plt.plot(x1, y1)
#plt.plot(x2, y2)
#plt.show()
