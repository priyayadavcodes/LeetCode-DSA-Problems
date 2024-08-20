class Solution:

    def hIndex(self, citations: List[int]) -> int:
    # Step 1: Sort the citations in descending order
        citations.sort(reverse=True)
        
        # Step 2: Find the h-index
        h_index = 0
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h_index = i + 1
            else:
                break
        
        return h_index

    # def hIndex(self, citations: List[int]) -> int:
    #     n = len(citations)
    #     max_sum = float("-inf")
    #     ls = []
    #     for i in range(n):
    #         num = citations[i]
    #         sum = 0
    #         if num != 0:
    #             for j in range(i,n,1):
    #                 if citations[j] >= num:
    #                     sum = sum+1
    #             if sum == num:
    #                 ls.append(num)
        

    #     val = min(ls)
    #     return val
    


        