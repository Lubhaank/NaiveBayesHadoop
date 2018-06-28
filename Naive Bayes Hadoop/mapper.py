#!/usr/bin/env python

import re
import sys


def tokenizeDoc(cur_doc):

        return re.findall("\\w+",cur_doc)



def printLabelsWords():


        for line in sys.stdin:

                line = line.strip()

                text = re.split(r'\t+', line)
                labels = re.split(r'\,+', text[1])
                features = tokenizeDoc(text[2])

                for label in labels:



                        tempLabel = "Y=" + label

                        #prin "%s\t%s" % (tempLabel, str(1))


                        #print "%s\t%s" % ("Y=*",str(1))

                        sys.stdout.write("Y=*" + '\t' + str(1) + '\n')

                        sys.stdout.write(tempLabel + '\t' + str(1) + '\n')


                        for feature in features:

                                tempFeature = tempLabel + ",W=" + feature

                                tempFeatureAllWords = tempLabel + ",W=*"

                                #print "%s\t%s" % (tempFeature, str(1))

                                #print(tempFeature + '\t' + str(1))

                                sys.stdout.write(tempFeature + '\t' + str(1) + '\n')

                                sys.stdout.write(tempFeatureAllWords + '\t' + str(1) + '\n')

                                #print "%s\t%s" % (tempFeatureAllWords, str(1))

                                #print(tempFeatureAllWords + '\t' + str(1))



if __name__ == '__main__':
        printLabelsWords()

