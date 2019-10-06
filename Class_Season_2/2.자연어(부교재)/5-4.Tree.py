# Trees
import nltk

tree1 = nltk.Tree('NP', ['Alice'])
print(tree1)

tree2 = nltk.Tree('NP', ['the', 'rabbit'])
print(tree2)

tree3 = nltk.Tree('VP', ['chased', tree2])
tree4 = nltk.Tree('S', [tree1, tree3])
print(tree4)
print(tree4[0])
print(tree4[1])
tree4[1].label()
tree4.leaves()
tree4[1][1][1]
tree4.draw()

def traverse(t):
    try:
        t.label()
    except AttributeError:
        print(t, end=" ")
    else:
        # Now we know that t.node is defined
        print('(', t.label(), end=" ")
        for child in t:
            traverse(child)
        print(')', end=" ")
            
t = nltk.Tree('(S (NP Alice) (VP chased (NP the rabbit)))')
traverse(t)

"""
t = nltk.Tree('(S (NP Alice) (VP chased (NP the rabbit)))')
Traceback (most recent call last):

  File "<ipython-input-24-7e5df3bde6fa>", line 1, in <module>
    t = nltk.Tree('(S (NP Alice) (VP chased (NP the rabbit)))')

  File "C:\Users\seong\Anaconda3\lib\site-packages\nltk\tree.py", line 104, in __init__
    "%s: Expected a node value and child list " % type(self).__name__

TypeError: Tree: Expected a node value and child list 
"""