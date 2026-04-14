class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s) - 1):
            curr_score, adj_score = ord(s[i]), ord(s[i + 1])
            score += abs (curr_score - adj_score)
        return score