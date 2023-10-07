import os
import random
import time

clearConsole = lambda: os.system('cls'
                                 if os.name in ('nt', 'dos') else 'clear')

ngrams = {}
sentences = [""]
previous_sentences = []
file = "text.txt"


def create_bigrams(line):
    line = line.strip().split(' ')
    line.append("EOL")
    for i in range(len(line) - 1):
        key = line[i]
        if key in ngrams:
            if line[i + 1] in ngrams[key]:
                ngrams[key][line[i + 1]] += 1
            else:
                ngrams[key][line[i + 1]] = 1
        else:
            ngrams[key] = {line[i + 1]: 1}


def read_file(file_name):
    in_file = open(file_name, "r")
    for line in in_file:
        create_bigrams(line)


def generate_sentences(key, num_sen):
    global sentences
    sentence = key
    count = 0
    while True:
        k1 = list(ngrams[key].keys())
        random.shuffle(k1)
        while len(k1) > int(num_sen):
            k1.pop()
        next_word = random.choice(k1)
        print("List of at most {} words after {}:".format(
            num_sen, sentences[len(sentences) - 1]))
        print(k1)
        while next_word == "EOL" and len(k1) > 1:
            next_word = random.choice(k1)
        print("Chose word: " + next_word)
        sentences.append(next_word)
        if next_word == "EOL":
            sentence += ""
            break
        count += 1
        sentence += " " + next_word
        key = next_word
        previous_sentences.append(sentence)
    sentences.clear()
    print("\n")
    print(sentence)


def main():
    read_file(file)
    while True:
        clearConsole()
        print("Randome Sentence Generator")
        print("Type / to quit (Forward Slash)")
        key = input("Write a random word:\n")
        clearConsole()
        print("Randome Sentence Generator")
        print("Type / to quit (Forward Slash)")
        num_sentences = input("How many words do you want to choose from?\n")
        clearConsole()
        sentences.append(key)
        if key in ngrams:
            previous_sentences.clear()
            generate_sentences(key, num_sentences)
            k = input("\nSee previous sentence?(y/n)")
            if k == "y":
                print(previous_sentences)
                input("\nType something to continue")
                sentences.clear()
            else:
                sentences.clear()
        else:
            if key == "/" or num_sentences == "/":
                break
            print("Not Found")
            time.sleep(2)
    print("Quitted")


if __name__ == "__main__":
    main()
