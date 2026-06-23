class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        length = len(nums)

        if length == k:
            return nums

        groups = {}

        for i in  nums:
            if i in groups:
                groups[i] +=1
            else:
                groups[i] = 1

        buckets = [[] for _ in range(length)]

        for key in  groups.keys():
            buckets[groups[key] - 1].append(key)

        output = []
        for i in  range(1, length +1):
            index = length - i
            if buckets[index]:
                lenght_items = len(buckets[index])

                if lenght_items > k:
                    items =  buckets[index][-k:]
                    k = 0
                    output += items
                else:
                    k -= lenght_items
                    output += buckets[index]
            
            if k == 0:
                break

        return output



        

        