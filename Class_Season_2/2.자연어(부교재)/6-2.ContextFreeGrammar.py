# Context-free grammar
import nltk

grammar1 = nltk.CFG.fromstring(
    """
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V | V NP | V NP PP
    PP -> P NP
    Det -> "the" | "a"
    N -> "man" | "park" | "dog" | "telescope"
    V -> "saw" | "walked"
    P -> "in" | "with"
    """)

sent = "the dog saw a man in the park".split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree) 


# Recursion in Syntactic Structure
grammar2 = nltk.CFG.fromstring("""
  S  -> NP VP
  NP -> Det Nom | PropN
  Nom -> Adj Nom | N
  VP -> V Adj | V NP | V S | V NP PP
  PP -> P NP
  PropN -> 'Buster' | 'Chatterer' | 'Joe'
  Det -> 'the' | 'a'
  N -> 'bear' | 'squirrel' | 'tree' | 'fish' | 'log'
  Adj  -> 'angry' | 'frightened' |  'little' | 'tall'
  V ->  'chased'  | 'saw' | 'said' | 'thought' | 'was' | 'put'
  P -> 'on'
  """)

sent2 = "the angry bear chased the frightened little squirrel".split()
rd_parser = nltk.RecursiveDescentParser(grammar2)
for tree in rd_parser.parse(sent2):
    print(tree)
    
sent3 = "Chatterer said Buster thought the tree was tall".split()
rd_parser = nltk.RecursiveDescentParser(grammar2)
for tree in rd_parser.parse(sent3):
    print(tree)

grammar3 = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "saw" | "ate" | "walked"
  NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
  Det -> "a" | "an" | "the" | "my"
  N -> "man" | "dog" | "cat" | "telescope" | "park"
  P -> "in" | "on" | "by" | "with"
  """)

# Recursive Descent Parsing
rd_parser = nltk.RecursiveDescentParser(grammar3)
sent4 = 'Mary saw a dog'.split()
for tree in rd_parser.parse(sent4):
    print(tree)

# Shift-Reduce Parsing
sr_parser = nltk.ShiftReduceParser(grammar3)
for tree in sr_parser.parse(sent4):
    print(tree)