# 워드넷
from nltk.corpus import wordnet as wn

# motorcar와 동의어인 집합 (synset : synonym set)의 원소들을 조회한다
wn.synsets('motorcar')
wn.synset('car.n.01').lemma_names()

# 동의어 집합의 의미 (정의)를 조회한다.
wn.synset('car.n.01').definition()

# 예문을 확인한다.
wn.synset('car.n.01').examples()

# 동의어 집합이 여러 개인 경우
wn.synsets('car')
for synset in wn.synsets('car'):
    print("Lemma: {}".format(synset.name()))
    print("Definition: {}".format(synset.definition()))
    print("Lemma_names: {}".format(synset.lemma_names()))
    print()


# Lemma : 어휘의 원형 조회
wn.synsets('working')
wn.synset('work.v.02').lemmas()
wn.synset('work.v.02').lemma_names()
wn.synset('work.v.02').definition()
wn.lemma('work.v.02.work')
wn.lemma('work.v.02.work').synset()
wn.lemma('work.v.02.work').name()
    
#Lexical relations (어휘 관계)
#-----------------------------
# Hyponym : 하위어 (a more specific concept)
printer = wn.synset('printer.n.03')
printer
printer.hyponyms()
wn.synset('addressing_machine.n.01').lemmas()
sorted([lemma.name()
    for synset in printer.hyponyms()
    for lemma in synset.lemmas()]
    )

# Hypernym : 상위어
printer.hypernyms()
wn.synset('machine.n.01').lemmas()
sorted([lemma.name()
    for synset in printer.hypernyms()
    for lemma in synset.lemmas()]
    )

# 최상위의 상위어
printer.root_hypernyms()

# 계층 구조 확인
printer.hypernym_paths()
[synset.name() for synset in printer.hypernym_paths()[0]]

wn.synset('entity.n.01').hyponyms()
wn.synset('physical_entity.n.01').hyponyms()
wn.synset('object.n.01').hyponyms()
wn.synset('whole.n.02').hyponyms()
wn.synset('instrumentality.n.03').hyponyms()

# part_meronyms() - obtains parts,
# substance_meronyms() - obtains substances
wn.synsets('tree')
wn.synset('tree.n.01').part_meronyms()
wn.synset('tree.n.01').substance_meronyms()

# Holonym — denotes a membership to something
wn.synset('atom.n.01').part_holonyms()
wn.synset('hydrogen.n.01').substance_holonyms()

# Entailment — denotes how verbs are involved, 함의
wn.synset('eat.v.01').entailments()

# Similarity
wn.synsets('truck')
truck = wn.synset('truck.n.01')
truck

wn.synsets('limousine')
limousine = wn.synset('limousine.n.01')
limousine

# 공통 상위어
truck.lowest_common_hypernyms(limousine)

# 유사도 측정
wn.synsets('dog')
dog = wn.synset('dog.n.01')
wn.synsets('wolf')
wolf = wn.synset('wolf.n.01')
wn.synsets('cat')
cat = wn.synset('cat.n.01')
wn.synsets('human')
human = wn.synset('homo.n.02')

dog.path_similarity(cat)
dog.path_similarity(wolf)
dog.path_similarity(human)
cat.path_similarity(human)

# Path similarity 계산 원리
wn.synset('carnivore.n.01').hyponyms()
wn.synset('canine.n.02').hyponyms()
wn.synset('feline.n.01').hyponyms()

# 컨셉 계층 (Concept Hierarchy) 깊이 측정
cat = wn.synset('cat.n.01')
cat.min_depth()
cat.hypernym_paths()
wn.synset('entity.n.01').min_depth()

dog = wn.synset('dog.n.01')
dog.min_depth()
dog.hypernym_paths()
