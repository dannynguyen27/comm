#!/usr/bin/python

# Danny Nguyen - LAB 3
import random, sys
from optparse import OptionParser

class comm:
    def __init__(self, filename, filename2):
        if filename == '-':
            self.lines = sys.stdin.readlines()

        else:
            f = open(filename, 'r')
            self.lines = f.readlines()
            f.close()

        if filename2 == '-':
            self.lines2 = sys.stdin.readlines()
        else:
            f = open(filename2, 'r')
            self.lines2 = f.readlines()
            f.close()

    def compareLines(self):
        i = 0
        j = 0

        words = []
        while i < len(self.lines) and j < len(self.lines2):

            self.lines[i] = self.lines[i].strip()
            self.lines2[j] = self.lines2[j].strip()

            if self.lines[i] == self.lines2[j]:
                words.append('\t\t' + self.lines[i])
                i += 1
                j += 1
            elif self.lines[i] < self.lines2[j]:
                words.append(self.lines[i])
                i += 1
            elif self.lines[i] > self.lines2[j]:
                words.append('\t' + self.lines2[j])
                j += 1
        while i < len(self.lines):
            words.append(self.lines[i])
            i += 1
        while j < len(self.lines2):
            words.append('\t' + self.lines2[j])
            j += 1
        return words    
    
    def compareLinesU(self):
        i = 0
        j = 0

        for x in range(len(self.lines)):
            self.lines[x] = self.lines[x].strip()

        for x in range(len(self.lines2)):
            self.lines2[x] = self.lines2[x].strip()

        words = []
        while i < len(self.lines):
            hasFound = False;
            temp = 0
            for x in range(len(self.lines2)):
                # Word appears in both lists
                if self.lines[i] == self.lines2[x]:
                    words.append('\t\t' + self.lines[i])
                    self.lines2.remove(self.lines2[x])
                    hasFound = True
                    break;
            if not hasFound:
                words.append(self.lines[i])
            i += 1

        for i in self.lines2:
            words.append('\t' + i)

        return words


    def chooseline(self):
        return random.choice(self.lines)

def main():
    version_msg = "%prog 2.0"
    usage_msg = """%prog [OPTION]... FILE1 FILE2"""

    parser = OptionParser(version=version_msg,
                          usage=usage_msg)
    parser.add_option("-u", "--1u", "--12u", "--123u",
                      action="store_true", dest="u_flag",
                      help="input unsorted files")

    parser.add_option("-1",
                      action="store_true", dest="one_flag",
                      help="suppress first column")

    parser.add_option("-2",
                      action="store_true", dest="two_flag",
                      help="suppress second column")    

    parser.add_option("-3",
                      action="store_true", dest="three_flag",
                      help="suppress third column") 

    options, args = parser.parse_args(sys.argv[1:])

    if len(args) != 2:
        parser.error("wrong number of operands")

    first_file = args[0]
    second_file = args[1]

    compare = comm(first_file, second_file)

    if options.u_flag:
        words = compare.compareLinesU()
    else:
        words = compare.compareLines()

    if (options.one_flag):
        flag = True
        while (flag):
            temp = len(words)
            count = 0
            for x in range(len(words)):
                count += 1
                if len(words[x].strip()) == len(words[x]):
                    words.remove(words[x])
                    break
            if (temp == count):
                flag = False;


    if (options.two_flag):
        flag = True
        while (flag):
            temp = len(words)
            count = 0
            for x in range(len(words)):
                count += 1

                tempWord = words[x].lstrip('\t')
                if abs(len(words[x].lstrip('\t')) - len(words[x])) == 1:
                    words.remove(words[x])
                    break
                if (temp == count):
                    flag = False

    if (options.three_flag):
        flag = True
        while (flag):
            temp = len(words)
            count = 0
            if (len(words) == 0):
                break;
            for x in range(len(words)):
                count += 1
                tempWord = words[x].lstrip('\t')
                if abs(len(words[x].lstrip('\t')) - len(words[x])) == 2:
                    words.remove(words[x])
                    break
                if (temp == count):
                    flag = False

    # Removes columns 1
    if (options.one_flag):
        for x in range(len(words)):
            words[x] = words[x][1:]

    #  Removes columns 2
    if (options.two_flag):
        for x in range(len(words)):
            if '\t' in words[x]:
                words[x] = words[x][1:]

    for i in words:
        print (i)

if __name__ == "__main__":
    main()