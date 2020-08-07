def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    cache = {}
    # the outer array
    for item in arrays:
        # the inner array with the numbers
        for num in item:
            if num in cache:
                # we increment the count?
                cache[num] = cache[num] + 1
            else:
                # put it in the cache
                cache[num] = 1
    
    # get every thing that has a count equal to the outer arrays length
    filtered = list(filter(lambda x: x[1] == len(arrays), cache.items()))
    for item in filtered:
        result.append(item[0])

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
