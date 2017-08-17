#Scrit for regex compare
import re

class Regexcomp:
        def __init__(self):
            self.pattern=""
            self.string=""
            self.result=""
        def comp(self,pattern,string):
            self.pattern = pattern
            self.string = string
            self.result = re.search(self.pattern,self.string)
            return self.result.group(0)