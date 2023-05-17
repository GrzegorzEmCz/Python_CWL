from collections import Counter


def count_words(file_path, n):
    with open(file_path, 'r') as file:
        content = file.read()  # zły pomysł; proszę to zrobić z Wikipedią

    words = content.split()
    word_counts = Counter(words)

    most_common = word_counts.most_common(n)
    if n < len(word_counts):
        count_of_nth_word = most_common[-1][1]
        i = n
        while i < len(word_counts) and word_counts.most_common(i + 1)[-1][1] == count_of_nth_word:
            most_common.append(word_counts.most_common(i + 1)[-1])
            i += 1

    for word, count in most_common:
        print(word, count)


def count_ngrams(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    words = content.split()

    bigrams = [(words[i], words[i + 1]) for i in range(len(words) - 1)]
    trigrams = [(words[i], words[i + 1], words[i + 2]) for i in
                range(len(words) - 2)]  # szkoda, że w poleceniu nie było n-gramów od 2 do 10

    bigram_counts = Counter(bigrams)
    trigram_counts = Counter(trigrams)

    print("Bigrams:")
    for bigram, count in bigram_counts.items():
        print(' '.join(bigram), count)

    print("\nTrigrams:")
    for trigram, count in trigram_counts.items():
        print(' '.join(trigram), count)


count_words('potop.txt', 10)
count_ngrams('potop.txt')
