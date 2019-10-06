# Feature structure
import nltk

# Feature structures
kim = {'CAT': 'NP', 'ORTH': 'Kim', 'REF': 'k'}
chase = {'CAT': 'V', 'ORTH': 'chased', 'REL': 'chase'}
lee = {'CAT': 'NP', 'ORTH': 'Lee', 'REF': 'l'}

sent = "Kim chased Lee"
tokens = sent.split()
def lex2fs(word):
    for fs in [kim, lee, chase]:
        if fs['ORTH'] == word:
            return fs
        
subj, verb, obj = lex2fs(tokens[0]), lex2fs(tokens[1]), lex2fs(tokens[2])
verb['AGT'] = subj['REF'] 
verb['PAT'] = obj['REF']

# 동사 chase의 논항구조
for k in ['ORTH', 'REL', 'AGT', 'PAT']:
    print("%-5s => %s" % (k, verb[k]))
    