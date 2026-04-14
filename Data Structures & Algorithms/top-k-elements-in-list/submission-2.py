class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use freq counter to decrement for max occurence per character
        # use max heap to get highest k counts

        freq_count = collections.defaultdict(int)
        for n in nums:
            freq_count[n] -= 1
        freq_list = [(c,n) for n,c in freq_count.items()]
        heapq.heapify(freq_list)
        counter = 0
        res = []
        while counter < k:
            val = heapq.heappop(freq_list)[1]
            res.append(val)
            counter +=1
        
        return res