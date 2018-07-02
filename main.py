import sys
from _tkinter import TclError

import WordCounter

common = ['się', 'nie', 'w', 'na', 'i', 'z', 'to', 'do',
          'a', 'że', 'co', 'po', 'ale', 'tak', 'o', 'jak',
          'jest', 'no', 'za', 'jej', 'żeby', 'już', 'coś',
          'od', 'tylko', 'czy', 'tym', 'może', 'jednak', 'tu']

input_path, output_path, special_words = WordCounter.interpret_args(sys.argv)

raw_text = WordCounter.extract_text_from_path(input_path)
all_words, words = WordCounter.extract_words(raw_text)

all_words_count, words_count = WordCounter.count_words(all_words), WordCounter.count_words(words)

words = WordCounter.count_each_word(words)
WordCounter.results_to_path(output_path, words, all_words_count, words_count, special_words)

cloud_words = {}

for word in words:
    if word not in common:
        cloud_words[word] = words[word]

try:
    WordCounter.to_cloud(cloud_words)
except TclError:
    pass
