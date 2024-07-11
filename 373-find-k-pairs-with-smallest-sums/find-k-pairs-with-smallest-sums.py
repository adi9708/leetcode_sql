class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        #Brute Force

        # Generate all pairs of combined elements and then sort the list of lists to find smallest pairs
        # TC: O(N2) -> 2 for loops
        # res = []
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         res.append([nums1[i], nums2[j]])
        # res.sort(key= lambda x: x[0] + x[1])
        # return res[:k]

        # Optimized solution using heap
        
        # Use min_heap where the min_element will be popped from top of the stack
        from heapq import heappush, heappop
        heap = []
        res = []
        visit = set()

        m = len(nums1)
        n = len(nums2)

        heap.append((nums1[0] + nums2[0], 0, 0))
        visit.add((0, 0))

        while k > 0 and heap:
            _sum, i, j = heappop(heap)
            res.append([nums1[i], nums2[j]])
            if i + 1 < m and (i + 1, j) not in visit:
                heappush(heap, (nums1[i+1] + nums2[j], i + 1, j))
                visit.add((i + 1, j))
            if j + 1 < n and (i, j + 1) not in visit:
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visit.add((i, j + 1))

            k = k - 1
        return res
        







        
        
        
        # minHeap = []
        # res = []
        
        # def push(i, j):
        #     if i < len(nums1) and j < len(nums2):
        #         heapq.heappush(minHeap, [nums1[i] + nums2[j], i, j])
        # push(0, 0)
        # # print(minHeap)
        # # print(res)
        # while minHeap and len(res) < k:
        #     num_sum, i, j = heapq.heappop(minHeap)
        #     res.append([nums1[i], nums2[j]])
        #     # print("\n res", res)
        #     push(i, j + 1)
        #     # If len of array 2 is only 1 i.e j == 0, edge case handling
        #     if j == 0:
        #         push(i + 1, 0)
        # return res
        # max_sum = float('inf')
        # res = []
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         curr_sum = nums1[i] + nums2[j]
        #         while curr_sum < max_sum:
        #             res.append([nums1[i], nums2[j]])
        #             k = k - 1

        #         # min_sum = min(min_sum, nums1[i] + nums2[j])
        #         # print(res, len(res))
        #         # print(k)
        #         if k > 0:
        #             res.append([nums1[i], nums2[j]])
        #             k = k - 1
        # return res

        

                