__author__ = 'hanwang'
import token__
guess = {}
p = {}
category = []


def classify(guess, p, category):
    cl = {}
    tok = token__.tokenize2(guess, category)
    for i in range(len(tok)):
        cl[i] = {}
        for j in tok[i].keys():
            cl[i][j] = {}
            for k in range(len(category)):
                cl[i][j][k] = 0
                for word in tok[i][j]:
                    if word in p:
                        cl[i][j][k] += p[word][k]

    result = {}
    for i in range(len(cl)):
        result[i] = {}
        for j in cl[i].keys():
            for k in cl[i][j]:
                if cl[i][j][k] == max(cl[i][j].values()):
                    result[i][j] = k

    for i in range(len(result)):
        print category[i] + ':'
        for j in result[i].keys():
            print '  ' + category[result[i][j]] + '  ' + j
    TP_ = 0 #overall TP
    FP_ = 0 #overall FP
    FN_ = 0 #overall FN
    for i in range(len(result)):
        TP = result[i].values().count(i)
        FP = len(result[i].values()) - TP
        FN = 0
        for j in range(len(result)):
            if j != i:
                FN += result[j].values().count(i)
        print category[i] + ': ' + 'TP = ' + str(TP) + ',FP = ' + str(FP) + ',FN = ' + str(FN)
        print '         Precision = ' + str(float(TP) / float(TP + FP)) + ', Recall = ' + str(float(TP) / float(TP + FN))
        print '         F1 = ' + str(float(2 * TP) / float(2 * TP + FP + FN))
        TP_ += TP
        FP_ += FP
        FN_ += FN
    print '         Microaveraged F1 = ' + str(float(2 * TP_) / float(2 * TP_ + FP_ + FN_))