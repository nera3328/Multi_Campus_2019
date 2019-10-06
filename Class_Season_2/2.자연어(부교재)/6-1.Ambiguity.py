# Relation Extraction
# The IEER corpus is marked up for a variety of Named Entities.
# '.*\bin\b(?!\b.+ing)' : negative lookahead assertion
# in 다음에 ing로 끝나는 단어가 나오지 않으면 ok.
# to disregard strings such as "success in supervising the transition of ~"
import nltk
import re
from nltk.corpus import ieer

doc_ieer = ieer.parsed_docs('NYT_19980315')
print(doc_ieer[0].text[:20])

IN = re.compile(r'.*\bin\b(?!\b.+ing)')
for doc in doc_ieer:
    for rel in nltk.sem.extract_rels('ORG', 'LOC', doc,
                        corpus='ieer', pattern = IN):
        print(nltk.sem.rtuple(rel))
