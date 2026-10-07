class Solution:
    def isValid(self, s: str) -> bool:
        r = ""
        for i in s :
            if i in { "(", ")"} :
                if i == "(" :
                    r+=i
                else : 
                    if r != "" and r[-1]== "(" : r  = r[:-1]
                    else : return False
            elif i in { "{", "}"} :
                if i == "{" :
                    r+=i
                else : 
                    if r != "" and r[-1]== "{" : r  = r[:-1]
                    else : return False
            elif i in { "[", "]"} :
                if i == "[" :
                    r+=i
                else :
                    if r != "" and r[-1]== "[" : r  = r[:-1]
                    else : return False
   
        if r != "": return False
        else : return True 