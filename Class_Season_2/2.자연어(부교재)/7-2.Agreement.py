# Agreement
import nltk

nltk.data.show_cfg('grammars/book_grammars/feat0.fcfg')

from nltk import load_parser
cp = load_parser('grammars/book_grammars/feat0.fcfg')
tokens = 'Kim likes children'.split()
for tree in cp.parse(tokens):
    print(tree)

fs1 = nltk.FeatStruct(TENSE='past', NUM='sg')
print(fs1)

fs1 = nltk.FeatStruct(PER=3, NUM='pl', GND='fem')
print(fs1['GND'])

fs1['CASE'] = 'acc'
fs2 = nltk.FeatStruct(POS='N', AGR=fs1)
print(fs2)

print(fs2['AGR'])
print(fs2['AGR']['PER'])

print(nltk.FeatStruct("[POS='N', AGR=[PER=3, NUM='pl', GND='fem']]"))
print(nltk.FeatStruct(NAME='Lee', TELNO='01 27 86 42 96', AGE=33))

# Structure sharing
print(nltk.FeatStruct(
    """
    [NAME='Lee', ADDRESS=(1)[NUMBER=74, STREET='rue Pascal'],
    SPOUSE=[NAME='Kim', ADDRESS->(1)]]
    """))

# Unification
fs1 = nltk.FeatStruct(NUMBER=74, STREET='rue Pascal')
fs2 = nltk.FeatStruct(CITY='Paris')
print(fs1.unify(fs2))

fs0 = nltk.FeatStruct(
    """
    [NAME=Lee,
    ADDRESS=[NUMBER=74, STREET='rue Pascal'],
    SPOUSE=[NAME=Kim, ADDRESS=[NUMBER=74,
                          STREET='rue Pascal']]]
    """)
print(fs0)

fs1 = nltk.FeatStruct("[SPOUSE = [ADDRESS = [CITY = Paris]]]") 
print(fs1.unify(fs0))

fs2 = nltk.FeatStruct(
    """
    [NAME=Lee, 
    ADDRESS=(1)[NUMBER=74, STREET='rue Pascal'], 
    SPOUSE=[NAME=Kim, ADDRESS->(1)]]
    """) 
print(fs1.unify(fs2))

fs1 = nltk.FeatStruct("[ADDRESS1=[NUMBER=74, STREET='rue Pascal']]")
fs2 = nltk.FeatStruct("[ADDRESS1=?x, ADDRESS2=?x]")
print(fs2)
print(fs2.unify(fs1))

