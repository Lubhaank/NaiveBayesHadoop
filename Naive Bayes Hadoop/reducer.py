#!/usr/bin/env python

import re
import sys


def reduceMap():

        curWord = ""

        curCount = 0

        word = ""

        for line in sys.stdin:

                line = line.strip()
                line = line.replace('\n','')
                text = re.split(r'\t+', line)
                word = text[0]
                count = int(text[1])

                if( curWord == word and curWord != ""):

                        curCount += count
                else:

                        if( curWord == ""):

                                curWord = word
                                curCount = count
                                continue

                        else:
                                sys.stdout.write(curWord + '\t' + str(curCount) + '\n')
                                #print "%s\t%s" % (curWord, str(curCount))
                                #print(curWord + '\t' + str(curCount))
                                curWord = word
                                curCount = count


        sys.stdout.write(curWord + '\t' + str(curCount) + '\n')
        #print "%s\t%s" % (curWord, str(curCount))
        #print(curWord + '\t' + str(curCount))


if __name__ == '__main__':
        reduceMap()
