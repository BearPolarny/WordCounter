import operator
import re

import matplotlib.pyplot as plt
from wordcloud import WordCloud


def interpret_args(args):
    """
    :param args: *args
    :return: input_path, output_path, list of special words
    """

    if len(args) == 1:
        path = 'test.txt'
    else:
        if args[1] == 'def':
            path = 'test.txt'
        else:
            path = args[1]

    if len(args) < 3:
        results_path = 'results.txt'
    else:
        if args[2] == 'def':
            results_path = 'results.txt'
        else:
            results_path = args[2]

    special_words = args[3:]
    return path, results_path, special_words


def extract_text_from_path(path):
    """
    :param path: Path to file from which you want to extract words
    :return: String of text from file
    """

    text = 'pusty'

    if path[-3:] == 'txt':
        file = open(path, mode='r', encoding='UTF-8')
        file.seek(0, 0)
        text = file.read()
    elif path[-3:] == 'pdf':
        raise NameError('PDF files are not implemented')

    return text


def special_to_string(words, special_words):
    """
    :param words: List of all words in text
    :param special_words: List of special words
    :return: String with all special words and their occurences
    """

    special_words_str = ''

    for word in special_words:
        if word in words:
            special_words_str += 'Word ' + word + ' occured: ' + str(words[word]) + 'time(s)\n'
        else:
            special_words_str += 'Word ' + word + ' doesn\'t occur in text\n'

    return special_words_str


def results_to_path(path, words, all_words_number=-1, filtered_words_number=-1, special_words=None, to_sort=True,
                    descending=True):
    """
    :param path: Output path
    :param words: Words and their occurences
    :param all_words_number:
    :param filtered_words_number:
    :param special_words: List of special words
    :param to_sort: If True output will be sorted
    :param descending: If True output will be sorted descending
                        If False ascending
    :return:
    """

    if special_words is not None:
        specials = special_to_string(words, special_words)
    else:
        specials = '\n'

    if to_sort:
        words = sort_words(words, descending)

    results = open(path, mode='w', encoding='UTF-8')
    print('All words (with alphanumeric): ' + str(all_words_number) +
          '\nAll words (without alphanumeric): ' + str(filtered_words_number) +
          '\nUnique words: ' + str(len(words)) +
          '\nAverage word appearence: ' + str(round(filtered_words_number / len(words), 2)) +
          '\n\n' + specials, file=results, end='\n\n\n')

    for word, value in words:
        print(word + ' ' + str(value), file=results)
    pass


def extract_words(text):
    """
    :param text: Text from witch you want to extract words
    :return: List of all alphanumeric words, List of words without numbers
    """

    text = text.lower()
    list_of_words_not_filtered = re.sub('[^\w]', " ", text).split()
    list_of_words = []

    for word in list_of_words_not_filtered:
        if word.isalpha():
            list_of_words.append(word)

    return list_of_words_not_filtered, list_of_words


def count_each_word(words):
    """
    :param words: List of words
    :return: Dictionary (word: count)
    """
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


def count_words(words):
    return len(words)


def sort_words(words, descending=True):
    words = sorted(words.items(), key=operator.itemgetter(1))

    if descending:
        return words[::-1]
    else:
        return words


def to_cloud(words):
    wordcloud = WordCloud(font_path='assets/DroidSansMono.ttf',
                          relative_scaling=1).generate_from_frequencies(words)
    plt.imshow(wordcloud)
    plt.waitforbuttonpress(0)
