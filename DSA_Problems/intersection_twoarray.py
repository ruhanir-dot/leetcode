'''
class Solution(object):
    def intersection(self, nums1, nums2):
        arr = set() 
        for i in range(len(nums1)): 
            for j in range(len(nums2)): 
                if nums1[i] == nums2[j]: 
                    arr.add(nums1[i])
        
        return list(arr)
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))