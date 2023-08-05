class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_1 = {}
        map_2 = {}

        if len(s) != len(t):
            return False 

        for ele in s:
            map_1[ele] = map_1.get(ele,0) + 1
        
        for ele in t:
            map_2[ele] = map_2.get(ele,0) + 1

        if map_1 == map_2:
            return True
        else:
            return False

     
