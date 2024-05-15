class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {} # This creates 2 hashmaps
        
        for i in range(len(s)): # Using index i to loop through both strings b/c same length
            countS[s[i]] = 1 + countS.get(s[i], 0) # Counting occurance of each character in string s
            countT[t[i]] = 1 + countT.get(t[i], 0)
            # Each character would be string s or t at index i, thats the key of the hashmap
            # Then increment
            ## Key error gets thrown with countS[s[i]] = 1 + countS[s[i]] due to character does not exist in hashmap yet
            ## the get method allows us to return a default value of 0 as a fix
        for c in countS: # Now iterate through the hashmaps and make sure the counts are the same
            if countS[c] != countT.get(c, 0):
                return False
            
        return True