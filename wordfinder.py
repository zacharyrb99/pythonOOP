"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, path):
        file = open(path)
        self.words = self.make_list(file)
        
        print(f"{len(self.words)} words read")
        # count = 0

        # for word in file:
        #     count += 1

        # print(f"{count} words read")

    def make_list(self, file):
        self.list = []
        for line in file:
            self.list.append(line.strip())

        return self.list

    def random(self):
        return random.choice(self.words)
        # index = randint(0, len(self.list))
        # return self.list[index]

class SpecialWordFinder(WordFinder):
    def make_list(self, file):
            return[word.strip() for word in file if word.strip() and not word.startswith("#")]  