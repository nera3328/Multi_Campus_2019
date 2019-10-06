# 사람 이름 목록을 읽어온다
import nltk

names = nltk.corpus.names
fileId = names.fileids()
print(fileId)

maleNames = names.words('male.txt')
femaleNames = names.words('female.txt')

print(maleNames[:20])
print()
print(femaleNames[:20])

# 이름의 마지막 글자의 분포를 확인한다.
# 남자 이름과, 여자 이름의 특징은?
cfd = nltk.ConditionalFreqDist(
	(fileid, name[-1])
	for fileid in names.fileids()
	for name in names.words(fileid)
	)
f = [w for w in cfd]
cfd[f[0]]
cfd[f[1]]
cfd.plot()
