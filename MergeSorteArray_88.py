class Solution:
    def merge(self, nums1, m, nums2 , n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # [element for element in nums1[0:m]] + [element for element in nums2[0:n]]
        # nums1.sort()
        # print(nums1)

        lenght = m+n
        numbers_to_merge_nums1 = m
        numbers_to_merge_nums2 = n
        to_remove_n1= []
        to_remove_n2= []

        for i in range(0,len(nums1)):    
            if i >= numbers_to_merge_nums1:
                to_remove_n1.append(nums1[i])
        
        [nums1.remove(element) for element in to_remove_n1]

        for i in range(0,len(nums2)):
            if i >= numbers_to_merge_nums2:
                to_remove_n2.append(nums1[i])
        [nums2.remove(element) for element in to_remove_n2]

        [nums1.append(element) for element in nums2]

        nums1.sort()
        

        print(nums1)

instance = Solution()
instance.merge( nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)

instance2 = Solution()
instance2.merge(nums1 = [1], m = 1, nums2 = [], n = 0)

instance3 = Solution()
instance3.merge(nums1 = [0], m = 0, nums2 = [1], n = 1) 