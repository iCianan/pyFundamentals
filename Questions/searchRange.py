import math
def searchRange(nums, target):
    def findFirst(nums, start, end, target):
        answer = -1
        low = 0
        high = len(nums) -1
        mid = math.floor((low + high)/2)
        while low < high:
            if nums[mid] == target:
                answer = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            mid = math.floor((low + high) / 2)
        return answer

    def findLast(nums, start, end, target):
        answer = -1
        low = 0
        high = len(nums) -1
        mid = math.floor((low + high)/2)
        while low < high:
            if nums[mid] == target:
                answer = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            mid = math.floor((low + high) / 2)
        return answer
    left = findFirst(nums, start, end, target)
    right = findLast(nums, start, end, target)
    return [left, right]
    






def main():
    input = [5,7,7,8,8,10]
    print(searchRange(input, 8))
    
if __name__ == "__main__":
    main()