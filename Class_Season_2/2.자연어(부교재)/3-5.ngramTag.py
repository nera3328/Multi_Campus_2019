import nltk

# Brown Corpus를 이용하여 Unigram으로 POS 태깅하고, 결과를 평가한다.
# most likely tag for that particular token.
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news') 
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents) 
print(unigram_tagger.tag(brown_sents[2007]))
unigram_tagger.evaluate(brown_tagged_sents)

# 학습 데이터와 시험 데이터로 구분하고 시험 데이터의 POS tag를 평가한다.
size = int(len(brown_tagged_sents) * 0.9)
size
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
unigram_tagger = nltk.UnigramTagger(train_sents) 
unigram_tagger.evaluate(test_sents) 

# Bigram POS tagging과 시험 데이터를 이용한 평가.
bigram_tagger = nltk.BigramTagger(train_sents)
bigram_tagger.tag(brown_sents[2007])
unseen_sent = brown_sents[4203]
print(bigram_tagger.tag(unseen_sent))

# 시험 데이터로 성능을 평가한다.
# Bigram에서는 만약 NNS VBG 시퀀스가 학습 데이터에 없다면 P(VBG|NNS)=0, sparse problem,
# 그 이후의 모든 시퀀스에 악영향을 미치므로 평가 결과가 낮다.
# N-gram의 N이 클수록 accuracy는 낮지만 문맥의 coverage는 좋다 (trade-off)
bigram_tagger.evaluate(test_sents)

# Combining Tagger (Unigram + Bigram)
# 1. Try tagging the token with the bigram tagger.
# 2. If the bigram tagger is unable to find a tag for the token,
#    try the unigram tagger.
# 3. If the unigram tagger is also unable to find a tag, use 
#    a default tagger.
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff = t0)
t2 = nltk.BigramTagger(train_sents, backoff = t1)
t2.evaluate(test_sents)

# Trigram까지 확장해 본다.
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff = t0)
t2 = nltk.BigramTagger(train_sents, backoff = t1)
t3 = nltk.TrigramTagger(train_sents, backoff = t2)
t3.evaluate(test_sents)

# HMM Tagger
from nltk.tag import hmm
trainer = hmm.HiddenMarkovModelTrainer()
hmm_tagger = trainer.train_supervised(train_sents)
hmm_tagger.tag(brown_sents[2007])
hmm_tagger.evaluate(test_sents)

# Unknown word
text = "I go to school in the morning"
token = text.split()
print(unigram_tagger.tag(token))
print(bigram_tagger.tag(token))
print(nltk.pos_tag(token))

text = "I go to school in the morning"
token = text.split()
print(unigram_tagger.tag(token))
print(bigram_tagger.tag(token))
print(nltk.pos_tag(token))

# Confusion Matrix
test_tags = [tag for sent in brown.sents(categories='editorial')
                for (word, tag) in t2.tag(sent)]
gold_tags = [tag for (word, tag) in brown.tagged_words(categories='editorial')]
cm = nltk.ConfusionMatrix(gold_tags, test_tags)
print(cm.pretty_format(truncate=10, sort_by_count=True))
cm['NN', 'NN']

# 학습 결과 저장
from pickle import dump
output = open('data/t2.pkl', 'wb')
dump(t2, output, -1)
output.close()

# 학습 결과 적용
from pickle import load 
input = open('data/t2.pkl', 'rb')
tagger = load(input)
input.close()

text = "The board's action shows what free enterpris\
 is up against in our complex maze of regulatory laws."
tokens = text.split()
print(tagger.tag(tokens))









