# SQL 문장 생성
import nltk

from nltk import load_parser
nltk.data.show_cfg('grammars/book_grammars/sql0.fcfg')

# sql0.fcfg에 정의된 문법을 이용하여 아래 query 문장을 SQL 문장으로 번환한다.
cp = load_parser('grammars/book_grammars/sql0.fcfg')
query = 'What cities are located in China'.split()

for tree in cp.parse(query):
    print(tree)

trees = list(cp.parse(query))
trees
print(trees[0])
trees[0].label()
trees[0].label()['SEM']

answer = trees[0].label()['SEM']
answer = [s for s in answer if s]
q = ' '.join(answer)
print(q)

# 변환된 SQL 문장 (q)을 이용하여 city.db에서 실제 query를 수행한다.
from nltk.sem import chat80
rows = chat80.sql_query('corpora/city_database/city.db', q)
for r in rows: print(r[0], end=" ")                        