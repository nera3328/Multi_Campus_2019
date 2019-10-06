# Chunking
import nltk

sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), 
            ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  
            ("the", "DT"), ("cat", "NN")]

# Chunking을 위한 문법을 정의한다. Regular expression을 이용함.
grammar = "NP: {<DT>?<JJ>*<NN>}"

# 위 문법을 적용하여 chunk parser를 생성한다.
# Chunk grammer
cp = nltk.RegexpParser(grammar)

# chunk parser를 이용하여, sentence를 분석한다.
result = cp.parse(sentence)

# 결과를 출력한다.
print(result)
result.draw()

# 2 가지 Rule
grammar = """
    NP: {<DT|PP\$>?<JJ>*<NN>}   # rule 1
        {<NNP>+}                # rule 2
"""

cp = nltk.RegexpParser(grammar)
sentence = [("Rapunzel", "NNP"), ("let", "VBD"), ("down", "RP"),
            ("her", "PP$"), ("long", "JJ"), ("golden", "JJ"), ("hair", "NN")]
result = cp.parse(sentence)
print(result)
result.draw()

# If a tag pattern matches at overlapping locations, 
# the leftmost match takes precedence
nouns = [("money", "NN"), ("market", "NN"), ("fund", "NN")]
grammar = "NP: {<NN><NN>}  # Chunk two consecutive nouns"
cp = nltk.RegexpParser(grammar)
print(cp.parse(nouns))

# subtree 연습
sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), 
            ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  
            ("the", "DT"), ("cat", "NN")]

# Chunking을 위한 문법을 정의한다. Regular expression을 이용함.
grammar = "NP: {<DT>?<JJ>*<NN>}"

# 위 문법을 적용하여 chunk parser를 생성한다.
# Chunk grammer
cp = nltk.RegexpParser(grammar)

# chunk parser를 이용하여, sentence를 분석한다.
tree = cp.parse(sentence)
print(tree)

for subtree in tree.subtrees():
    print(subtree.label())

# 원하는 형태의 시퀀스를 발췌한다.
cp = nltk.RegexpParser('CHUNK: {<V.*> <TO> <V.*>}')
brown = nltk.corpus.brown
i = 0
for sent in brown.tagged_sents():
    tree = cp.parse(sent)
    for subtree in tree.subtrees():
        if subtree.label() == 'CHUNK':
            print(subtree)
            i += 1
    if i > 10: break

# Chinking
grammar = r"""
    NP:
    {<.*>+}         # Chunk everything
    }<VBD|IN>+{     # Chink sequences of VBD and IN
"""
sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),
            ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),
            ("the", "DT"), ("cat", "NN")]
cp = nltk.RegexpParser(grammar)
print(cp.parse(sentence))
