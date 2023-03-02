import random
import string
import argparse

def setUpWords(w, c, n, s):
    # read file length + lines
    with open("words.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]
        file_length = len(lines)

    # get correct # of words
    list = []
    for i in range(w):
        list.append(lines[random.randint(0, file_length - 1)]);

    # capitilizes the specified amount
    cap_indicies = random.sample(range(len(list)), c)
    for i in range(len(list)):
        if i in cap_indicies:
            list[i] = list[i].capitalize();

    # random nums the specified amount
    num_indicies = random.sample(range(len(list) + 1), n)
    for i in range(len(list) + 1):
        if i in num_indicies:
            if i < len(list):
                list[i] = str(random.randint(0, 9)) + list[i]
            else:
                list[len(list) - 1] += str(random.randint(0, 9))

    # random symbols the specified amount
    symbols_indicies = random.sample(range(len(list) + 1), s)
    symbols = string.punctuation
    for i in range(len(list) + 1):
        if i in symbols_indicies:
            if i < len(list):
                print(len(list))
                print(i)
                list[i] = symbols[random.randint(0, len(symbols))] + list[i]
            else:
                list[len(list) - 1] += symbols[random.randint(0, len(symbols))]

    # combine words
    combo = ""
    for i in range(len(list)):
        combo += list[i]

    # !!might allow repeat words!!
    return combo

def main():
    # combo = setUpWords(4, 2, 3, 2)
    # print(combo)
    parser = argparse.ArgumentParser(description='Create a strong password')
    parser.add_argument('-w', '-words', type=int)
    parser.add_argument('-c', '-caps', type=int)
    parser.add_argument('-n', '-numbers', type=int)
    parser.add_argument('-s', '-symbols', type=int)

    args = parser.parse_args()
    if args.w is None:
        words = 4
    else:
        words = args.w

    if args.c is None:
        cap = 0
    else:
        cap = args.c

    if args.n is None:
        num = 0
    else:
        num = args.n

    if args.s is None:
        sym = 0
    else:
        sym = args.s

    combo = setUpWords(words, cap, num, sym)
    print(combo)

if __name__ == '__main__':
    main()