import nltk

# Brown Corpus에서 Tag의 빈도를 확인한다
from nltk.corpus import brown
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
tag_fd.most_common() 

# 명사 앞에 많이 오는 품사를 확인한다. (Bigram 이용)
word_tag_pairs = nltk.bigrams(brown_news_tagged)
bigram = [(a, b) for (a, b) in word_tag_pairs]
bigram[:10]

word_tag_pairs = nltk.bigrams(brown_news_tagged)
noun_preceders = [a[1] for (a, b) in word_tag_pairs if b[1] == 'NOUN']
fdist = nltk.FreqDist(noun_preceders)
[tag for (tag, _) in fdist.most_common()]

# 뉴스에서 가장 많이 쓰이는 동사를 확인한다
wsj = nltk.corpus.treebank.tagged_words(tagset='universal')
word_tag_fd = nltk.FreqDist(wsj)
word_tag_fd.most_common()[:10]

v = [wt[0] for (wt, _) in word_tag_fd.most_common() if wt[1] == 'VERB']
print(v[:20])

# 특정 단어에 부여된 품사 빈도를 확인한다
cfd1 = nltk.ConditionalFreqDist(wsj)
list(cfd1.items())[:10]

cfd1['yield'].most_common()
cfd1['cut'].most_common()

# 특정 품사로 상용된 단어를 확인한다.
wsj = nltk.corpus.treebank.tagged_words()
cfd2 = nltk.ConditionalFreqDist((tag, word) for (word, tag) in wsj)
print(list(cfd2['VBN'])[:20])

# VBD (현재형), VBN (과거분사형) 단어를 확인한다
v = [w for w in cfd1.conditions() 
        if 'VBD' in cfd1[w] and 'VBN' in cfd1[w]]
print(v[:20])

# 과거형 동사와 과거완료형 동사이 앞 부분 context를 확인한다
idx1 = wsj.index(('kicked', 'VBD'))
wsj[idx1]
wsj[idx1-4:idx1+1]

idx2 = wsj.index(('kicked', 'VBN'))
wsj[idx2-4:idx2+1]

# 특정 단어 뒤에 자주 쓰이는 단어를 조회한다
brown_learned_text = brown.words(categories='learned')
v = sorted(set(b for (a, b) in nltk.bigrams(brown_learned_text) if a == 'often'))
print(v[:20])

# 특정 단어 뒤에 자주 나오는 품사를 조회한다
brown_lrnd_tagged = brown.tagged_words(categories='learned', tagset='universal')
tags = [b[1] for (a, b) in nltk.bigrams(brown_lrnd_tagged) if a[0] == 'often']
fd = nltk.FreqDist(tags)
fd.tabulate()

# <Verb> to <Verb> 형태로 사용된 사례 10개를 확인한다.
from nltk.corpus import brown
def process(sentence):
    for (w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
        if (t1.startswith('V') and t2 == 'TO' and
            t3.startswith('V')):
            print(w1, w2, w3)
            return True
    return False

i = 0
for tagged_sent in brown.tagged_sents():
    r = process(tagged_sent)
    if i > 10: break
    if r: i += 1

# 3개 이상의 품사로 사용된 단어 10개를 조회한다.
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
data = nltk.ConditionalFreqDist((word.lower(), tag)
                            for (word, tag) in brown_news_tagged)
i = 0
for word in sorted(data.conditions()):
    if len(data[word]) > 2:
        tags = [tag for (tag, _) in data[word].most_common()]
        print(word, ' '.join(tags))
        i += 1
        if i >= 10: break
