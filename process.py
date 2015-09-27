
# coding: utf-8

# In[1]:

import nltk

cp = nltk.load_parser('thing.fcfg')
thing = cp.parse("How much have I spent on coffee and frogs".split())
tree = list(thing)[0]
tree.label()['SEM']



# In[ ]:




# In[ ]:




# In[ ]:



