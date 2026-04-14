from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = defaultdict(int)
        t_counter = defaultdict(int)

        for _ in s:
            s_counter[_] +=1

        for _ in t:
            t_counter[_] +=1   

        return s_counter == t_counter

        