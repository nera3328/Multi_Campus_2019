# Chunking (2)
import nltk
from nltk.corpus import conll2000

# Chunked sentence
print(conll2000.chunked_sents('train.txt')[99])

# NP만 chunk로 표시
print(conll2000.chunked_sents('train.txt', chunk_types=['NP'])[99])

# IOB tag로 표시
conll2000.iob_sents('train.txt')[99]

# test.txt로 chunk 성능을 평가한다
test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
grammar = r"NP: {<[CDJNP].*>+}"
cp = nltk.RegexpParser(grammar)
score = cp.evaluate(test_sents)
print(score)

score.accuracy()
score.precision()
score.recall()
score.f_measure()

# Recursion in Linguistic Structure
grammar = r"""
    NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
    PP: {<IN><NP>}               # Chunk prepositions followed by NP
    VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
    CLAUSE: {<NP><VP>}           # Chunk NP, VP
    """
cp = nltk.RegexpParser(grammar)
sentence = [("Mary", "NN"), ("saw", "VBD"), ("the", "DT"), ("cat", "NN"),
            ("sit", "VB"), ("on", "IN"), ("the", "DT"), ("mat", "NN")]
print(cp.parse(sentence))

sentence = [("John", "NNP"), ("thinks", "VBZ"), ("Mary", "NN"),
            ("saw", "VBD"), ("the", "DT"), ("cat", "NN"), ("sit", "VB"),
            ("on", "IN"), ("the", "DT"), ("mat", "NN")]
print(cp.parse(sentence))

cp = nltk.RegexpParser(grammar, loop=2)
print(cp.parse(sentence))

# Named Entity Recognition (NER)
sent = nltk.corpus.treebank.tagged_sents()[22]
print(nltk.ne_chunk(sent, binary=True))
print(nltk.ne_chunk(sent))