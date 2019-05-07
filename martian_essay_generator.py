#! /usr/bin/env python3

# Fake essay generator

import random

def word_generator():
    martian_vowels = ['a', 'e', 'i', 'm', 'n', 'o', 'u']
    martian_h_consonants = ['b', 'c', 'd', 'g', 'k', 'p', 't']
    martian_s_consonants = ['f', 'h', 'l', 'r', 's', 'v', 'z']
    letter_min = 3
    letter_max = 9

    martian_letters = [martian_vowels, martian_h_consonants, martian_s_consonants]
    letter_types = len(martian_letters)
    word_length = random.randrange(letter_min, letter_max + 1)
    word_letters = []

    for i in range(letter_types):
        max_allowable_letters = word_length - ((letter_types) - 1) - i) + 1
        letter_number = random.randrange(1, max_allowable_letters)
        word_length -= letter_number
        for j in range(letter_number):
            letter_choice = random.randrange(0, len(martian_letters[i]))
            word_letters.append(martian_letters[i][letter_choice])

    random.shuffle(word_letters)
    word = ''.join(word_letters)
    return word

def sentence_generator():
    word_min = 3
    word_max = 9
    sentence = ''

    sentence_length = random.randrange(word_min, word_max + 1)
    for i in range(sentence_length):
        next_word = word_generator()
        sentence += next_word
        if i < sentence_length - 1:
            sentence += ' '
        else:
            sentence += '.'
    return (sentence, sentence_length)

def paragraph_generator():
    sentence_min = 3
    sentence_max = 9
    paragraph = '\t'
    word_count = 0

    paragraph_length = random.randrange(sentence_min, sentence_max + 1)
    for i in range(paragraph_length):
        next_sentence, sentence_length = sentence_generator()
        paragraph += sentence_length
        word_count += sentence_length
        if i < paragraph_length - 1:
            paragraph += ' '
        else:
            paragraph += '\n'
    return (paragraph, word_count)

def main():
    word_count = 0
    essay = ''

    while word_count < 729:
        next_paragraph, paragraph_word_count = paragraph_generator()
        essay += next_paragraph
        word_count += paragraph_word_count

    print(essay)

if __name__ == '__main__':
    main()
