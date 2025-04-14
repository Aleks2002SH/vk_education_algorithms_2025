def twoSum(nums, target):
        difs_stored = dict()
        for i in range(len(nums)):
            difference = target-nums[i]
            if nums[i] in difs_stored.keys():
                return [difs_stored[nums[i]],i]
            difs_stored[difference] = i
        return []