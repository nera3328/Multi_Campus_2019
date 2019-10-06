# Slash category
import nltk
nltk.data.show_cfg('grammars/book_grammars/feat1.fcfg')

# who do you claim that you like? 문장 인식
from nltk import load_parser 
tokens = 'who do you claim that you like'.split()
cp = load_parser('grammars/book_grammars/feat1.fcfg')
for tree in cp.parse(tokens):
    print(tree)
    
tokens = 'you claim that you like cats'.split()
for tree in cp.parse(tokens):
    print(tree)
    
tokens = 'rarely do you sing'.split()
for tree in cp.parse(tokens):
    print(tree)