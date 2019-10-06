# Penn Treebank Corpus : Grammars
import nltk
from nltk.corpus import treebank

t = treebank.parsed_sents('wsj_0001.mrg')[0]
print(t)

print(treebank.parsed_sents())

def filter(tree):
    child_nodes = [child.label() for child in tree
                   if isinstance(child, nltk.Tree)]
    return  (tree.label() == 'VP') and ('S' in child_nodes)

i = 0
for tree in treebank.parsed_sents():
    for subtree in tree.subtrees(filter):
        print(list(subtree))
        
    i += 1
    if i > 10: break


# Treebank의 10개 문장에서 production 규칙을 얻는다.
ruleset = set(rule for tree in nltk.corpus.treebank.parsed_sents()[:10] 
           for rule in tree.productions())

rules = []
for rule in ruleset:
    rules.append(rule)
rules[:20]

# The Prepositional Phrase Attachment Corpus
from collections import defaultdict
entries = nltk.corpus.ppattach.attachments('training')
table = defaultdict(lambda: defaultdict(set))

i = 0
for entry in entries:
    key = entry.noun1 + '-' + entry.prep + '-' + entry.noun2
    table[key][entry.attachment].add(entry.verb)
    for key in sorted(table):
        if len(table[key]) > 1:
            print(key, 'N:', sorted(table[key]['N']), 'V:', sorted(table[key]['V']))
    i += 1
    if i > 10: break

entries[0]
"""
PPAttachment(sent='0', verb='join', noun1='board', prep='as', noun2='director', attachment='V')
"""

table['board-as-director']
# defaultdict(set, {'V': {'join'}})

table['board-as-director']['N']
#set()

table['board-as-director']['V']
# {'join'}

"""
If you want a grammar that precisely captures the Penn Treebank sample that 
comes with NLTK, you can do this, assuming you've downloaded the Treebank data 
for NLTK (see comment below):
    
import nltk
from nltk.corpus import treebank
from nltk.grammar import ContextFreeGrammar, Nonterminal

tbank_productions = set(production for sent in treebank.parsed_sents()
                        for production in sent.productions())
tbank_grammar = ContextFreeGrammar(Nonterminal('S'), list(tbank_productions))

This will probably not, however, give you something useful. Since NLTK only supports 
parsing with grammars with all the terminals specified, you will only be able to parse 
sentences containing words in the Treebank sample.
Also, because of the flat structure of many phrases in the Treebank, this grammar will 
generalize very poorly to sentences that weren't included in training. This is why NLP 
applications that have tried to parse the treebank have not used an approach of learning 
CFG rules from the Treebank. The closest technique to that would be the Ren Bods Data 
Oriented Parsing approach, but it is much more sophisticated.
Finally, this will be so unbelievably slow it's useless. So if you want to see this 
approach in action on the grammar from a single sentence just to prove that it works, 
try the following code (after the imports above):

mini_grammar = ContextFreeGrammar(Nonterminal('S'),
                                  treebank.parsed_sents()[0].productions())
parser = nltk.parse.EarleyChartParser(mini_grammar)
print parser.parse(treebank.sents()[0])
"""