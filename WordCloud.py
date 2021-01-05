#!/usr/bin/env python3

# !pip install wordcloud

import wordcloud, numpy as np, io, sys, os
from matplotlib import pyplot as plt

def upload():
    path = os.path.join(os.getcwd(), 'Test.txt')
    with open(path, mode='r', encoding='cp1252') as file:
        file_contents = file.read()
        return file_contents

def dictionary_get(file_contents):			# Here is a list of punctuations and uninteresting words you can use to process your text

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    dictionary = {}
    lists = []
    lists=file_contents.lower().split()

    for words in lists:
        if words not in punctuations or words not in uninteresting_words:
            if words in dictionary:
                dictionary[words] +=1
            else:
                dictionary[words] = 1

    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(dictionary)

    return cloud.to_array()

myimage = dictionary_get(upload())						# Display your wordcloud image
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
