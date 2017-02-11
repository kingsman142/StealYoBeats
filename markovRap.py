# heavily inspired by llSourcell/Rap_Lyric_Generator

import random, re

def addToDict(data, freqDict):
    words = re.sub("\n", " \n", data).lower().split(' ')
    for curr, succ in zip(words[1:], words[:-1]):
        if curr not in freqDict:
            freqDict[curr] = {succ: 1}
        else:
            if succ not in freqDict[curr]:
                freqDict[curr][succ] = 1
            else:
                freqDict[curr][succ] += 1
    probDict = {}
    for curr, currDict in freqDict.items():
        probDict[curr] = {}
        currTotal = sum(currDict.values())
        for succ in currDict:
            probDict[curr][succ] = currDict[succ] / currTotal
    return probDict

def addFromFile(fileName, freqDict):
    data = open(fileName, 'r').read()
    return addToDict(data, freqDict)

def markov_next(curr, probDict):
    if curr not in probDict:
        return random.choice(list(probDict.keys()))
    else:
        succProbs = probDict[curr]
        randProb = random.random()
        currProb = 0.0
        for succ in succProbs:
            curProb += succProbs[succ]
            if randProb <= currProb:
                return succ
        return random.choice(list(probDict.keys()))

def makeRap(curr, probDict, T=50):
    rap = [curr]
    for t in range(T):
        rap.append(markov_next(rap[-1], probDict))
    return " ".join(rap)

def genRap(tweets):
    rapFreqDict = {}
    rapProbDict = addToDict('lyrics1.txt', rapFreqDict)
    rapProbDict = addToDict('lyrics2.txt', rapFreqDict)
    rapProbDict = addToDict(tweets, rapFreqDict)
    
    startWord = random.choice(tweets)
    return makeRap(startWord, rapProbDict)
