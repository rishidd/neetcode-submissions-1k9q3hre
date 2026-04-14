class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #make max heap based on occurence value and number
        # use heappop to pop up highest occurences until k

        freq_counter = collections.defaultdict(int)

        for n in nums:
            freq_counter[n] -= 1
        
        freq_pairing = [ (c,n) for n,c in freq_counter.items()]
        heapq.heapify(freq_pairing)
        print(freq_pairing)
        ans = []
        while len(ans) < k:
            ans.append(heapq.heappop(freq_pairing)[1])
        
        return ans