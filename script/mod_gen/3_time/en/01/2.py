def twoSum(nums, target):
    # Create a dictionary to store the numbers and their indices
    my_dict = {}
    # Loop through the list of numbers
    for index, num in enumerate(nums):
        # Check if the number in the dictionary
        if num in my_dict:
            # Return the indices
            return [my_dict[num], index]
        # If the number not in the dictionary
        else:
            # Store the number and its index in the dictionary
            my_dict[target - num] = index

if __name__ == '__main__':
    twoSum()