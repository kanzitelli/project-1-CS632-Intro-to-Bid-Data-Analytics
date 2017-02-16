
# coding: utf-8

# In[36]:

get_ipython().system(u'pip install stop-words')


# In[42]:

# Project #1
# Task: to build a Basic Inverted Index

from stop_words import get_stop_words

# CONSTANTS
DOCS = ['doc1.txt', 'doc2.txt', 'doc3.txt', 'doc4.txt'] # an array with file names where paragraphs are
DOCS_TEST = ['test1.txt', 'test2.txt']
STOP_WORDS = get_stop_words('en')

def collect_all_docs(docs):
    # return - { docName: text, ... }
    docs_info = {}
    for doc_name in docs:
        with open(doc_name) as f: indata = f.read()
        name = doc_name.split('.')[0]
        docs_info[name] = indata.lower()
    return docs_info

def tokenize_text_of(docs): 
    # return - [ (term, docID), ... ]
    tokenized = []
    for key, text in docs.iteritems():
        array_of_words = text.split()
        for word in array_of_words:
            cleanWord = ""
            for char in word:
                if char in '!,.?\'":;0123456789': # we don't want whose symbols 
                    char = ""
                cleanWord += char
            if cleanWord != "" and not cleanWord in STOP_WORDS: # checks if it is in STOP_WORDS or not
                tokenized.append((cleanWord, key))
    return tokenized

def build_inverted_index_with(words):
    # return - [ ( (term, doc. freq.), [doc_name, ...] ), ... ]
    words_len = len(words)
    index_info = []
    i = 0
    while i in range(0, words_len):
        term, doc = words[i]
        doc_freq = 1
        doc_names = [doc]
        last = i + 1
        for j in range(i + 1, words_len):
            term2, doc2 = words[j]
            if term == term2:
                if not doc2 in doc_names:
                    doc_freq += 1
                    doc_names.append(doc2)
            else:
                last = j
                break
        i = last
        index_info.append( ( (term, doc_freq), doc_names ) )
    return index_info
        
docs = collect_all_docs(DOCS)
#print docs_info
#print('____________________________________')

tokenized_text = tokenize_text_of(docs)
#print tokenized_text
#print('____________________________________')

sorted_words = sorted(tokenized_text, key=lambda tup: tup[0])
#print sorted_words
#print('____________________________________')

index_info = build_inverted_index_with(sorted_words)
print 'TERM --- DOC. FREQ. --- POSTRINGS LISTS\n'
for info in index_info:
    term_doc_freq, postings_lists = info
    print '{0} - {1} - {2}'.format(term_doc_freq[0], term_doc_freq[1], postings_lists)
print('____________________________________')

#print(STOP_WORDS)


# In[ ]:



