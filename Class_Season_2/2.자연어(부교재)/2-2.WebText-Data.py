# Webtext 데이터를 읽어온다
from nltk.corpus import webtext

# Webtext 코퍼스의 파일 ID를 조회한다.
textId = webtext.fileids()
print(textId)

# "케리비안 해적"의 영화 대본 텍스트 문서를 조회한다.
# http://www.actorpoint.com/movie-scripts/scripts/pirates-of-the-caribbean-dead-man%27s-chest.html
text = webtext.raw('pirates.txt')
print(text[:1000])
print("문자 개수 = ", len(text))

# 문서를 word 단위로 읽어온다.
word = webtext.words('pirates.txt')
print(word)
print("word 개수 = ", len(word))

# 문서를 문장 단위로 읽어온다.
sentence = webtext.sents('pirates.txt')
for i in range(5):
    print(sentence[i])
print("문장 개수 = ", len(sentence))

# Firefox의 게시판 텍스트 문서를 조회한다.
text = webtext.raw('firefox.txt')
print(text[:1000])
print("문자 개수 = ", len(text))

# 문서를 word 단위로 읽어온다.
word = webtext.words('firefox.txt')
print(word)
print("word 개수 = ", len(word))

# 문서를 문장 단위로 읽어온다.
sentence = webtext.sents('firefox.txt')
for i in range(5):
    print(sentence[i])
print("문장 개수 = ", len(sentence))

###############################################
# NPS Chat 데이터
# http://faculty.nps.edu/cmartell/npschat.htm
from nltk.corpus import nps_chat

# Chat 코퍼스의 파일 ID를 조회한다.
textId = nps_chat.fileids()
print(textId)

# 특정 Chat session의 텍스트 문서를 조회한다.
text = nps_chat.raw('10-19-20s_706posts.xml')
print(text[:2000])
print("문자 개수 = ", len(text))

# XML의 post 데이터를 읽는다
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
for chat in chatroom[:20]:
    print(chat)
