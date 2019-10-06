# Ambiguity
import nltk

# 문법을 정의한다.
groucho_grammar = nltk.CFG.fromstring(
        """
        S -> NP VP
        PP -> P NP
        NP -> Det N | Det N PP | 'I'
        VP -> V NP | VP PP
        Det -> 'an' | 'my'
        N -> 'elephant' | 'pajamas'
        V -> 'shot'
        P -> 'in'
        """)

# 정의한 문법을 적용하여 아래 문장의 구조를 분석한다.
sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']
parser = nltk.ChartParser(groucho_grammar)
for tree in parser.parse(sent):
    print(tree)
