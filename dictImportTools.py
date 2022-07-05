import json

class Tools():
    def importDict(string, delim="!"):
        rawString = string
        cleanString = rawString.replace(delim, "\"")
        convDict = json.loads(cleanString)
        return convDict
    def importFloatDict(string, delim="!"):
        rawString = string
        cleanString = rawString.replace(delim, "\"")
        convDict = json.loads(cleanString)
        for k,v in convDict.items():
            convDict[k] = float(v)
        return convDict