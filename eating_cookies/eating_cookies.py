'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache = None):

    cache = [0]*(n+1)

    for i in range(0,len(cache)):
        if i < 2:
            cache[i]= 1
        elif i == 2:
            cache[i] = cache[i-2] + cache[i-1]
        else: 
            cache[i] = cache[i-3] + cache[i-2] + cache[i-1] 
    return cache[i]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
