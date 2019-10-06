# 영어 단어 목록 (word list)을 읽어온다
import nltk

wordlist = nltk.corpus.words.words()
print("단어 개수 = ", len(wordlist))
print(wordlist[:30])
print(wordlist[-30:])

# Figure 4.3: A Word Puzzle: a grid of randomly chosen
# letters with rules for creating words out of the 
# letters; this puzzle is known as "Target."
# +---+---+---+  How many words of four letters or more
# | e | g | i |  from those shown here? Each letter may
# +---+---+---+  be used once per word. Each word must
# | v | r | v |  contain the center letter and there
# +---+---+---+  must be at least one nine-letter word.
# | o | n | l |  No plurals ending in "s"; no foreign
# +---+---+---+  words; no proper names. 21 words, good;
# 32 words, very good; 42 words, excellent.
puzzleLetters = nltk.FreqDist('egivrvonl')
obligatory = 'r'
answer = [w for w in wordlist if len(w) >= 6
              and obligatory in w
              and nltk.FreqDist(w) <= puzzleLetters]
print(answer) 
