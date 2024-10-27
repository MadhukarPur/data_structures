'''
    String Matching - Brute Force Method

    Time Complexity: O(n * m)

    Limitation of the Brute Force Method:
        The brute force algorithm, as its name suggests, isn't very efficient. 
        It ends up doing a lot of extra comparisons, especially when dealing with repeated letters. 
'''

def brute_force(text, pattern):
    # initialize a list to store positions of pattern occurrences
    occurrences = []  

    for i in range(len(text) - len(pattern) + 1):

        # check if the pattern matches starting from position i
        for j in range(len(pattern)):
            
            match = text[i+j] == pattern[j]
            # mismatch found, break the loop
            if not match:
                break  
            # whole pattern is matched, record the position
            if j == len(pattern) - 1:
                occurrences.append(i)  

    return occurrences  


'''
    String Matching - Rabin-Karp Algorithm

    Time Complexity: O(n + m)

    Limitation of Rabin-Karp Algorithm
        -- the Rabin-Karp algorithm can sometimes give false matches because different substrings have the same hash value as the pattern.
        -- Even though the algorithm tries to fix this by checking the matches character by character, it's not very efficient. This is especially true 
            when there are many substrings with the same hash value as the pattern.
        -- This extra work of comparing characters adds to the algorithm's computational load, especially when dealing with large texts or patterns.
'''
def compute_hash(string, base = 256, prime = 101):
    
    hash_value = 0

    for index, char in enumerate(string):
        
        ascii_value = ord(char)
        exponent = len(string) - index - 1
        term = (ascii_value * pow(base, exponent)) % prime
        
        hash_value = (hash_value + term) % prime

    return hash_value

def rabin_karp(text, pattern, base = 256, prime = 101):

    pattern_length = len(pattern)
    text_length = len(text)

    # hash of the pattern text (substring)
    pattern_hash = compute_hash(pattern)
    
    # hash of a substring that has the same length as the pattern
    substring_hash = compute_hash(text[: pattern_length])
    
    # initialize a list to store occurrences of the pattern in text
    occurrences = []
    
    # pre-compute the highest power of base
    # this is needed to update the hash for the next substring
    highest_base_pow = pow(base, pattern_length - 1) % prime

    # loop through all possible substrings of text with pattern length
    for i in range(text_length - pattern_length + 1):
        
        # compare hash of substring and pattern
        if pattern_hash == substring_hash:
            
            # double check to confirm match
            if all(text[i + j] == pattern[j] for j in range(pattern_length)):
                occurrences.append(i)
                
        # update the hash of the next substring using the previous hash
        if i < text_length - pattern_length:
            
            # update the rolling hash for the next substring
            # remove first character's hash and add next character's hash-based
            substring_hash = (substring_hash - ord(text[i]) * highest_base_pow) * base
            substring_hash = (substring_hash + ord(text[i + pattern_length])) % prime
            
    return occurrences

'''
    String Matching - Knuth-Morris-Pratt (KMP) algorithm

    Time Complexity: O(m+n)
'''
def compute_lps_array(pattern):
    # start with F[0] = 0
    lps = [0]
    # temporary value
    c = 0
    # start from 1 because we already have F[0] = 0
    for i in range(1, len(pattern)):
        # in case of a pattern match
        if pattern[c] == pattern[i]:
            # increase substring length by 1
            c = c + 1 
        # else if pattern matches the first character
        elif pattern[i] == pattern[0]:
            c = 1
        # if the pattern doesn't match the subsequence or the first character
        else:
            # reset substring length to 0
            c = 0
            
        lps.append(c)
    return lps


def kmp(text, pattern):
    # compute the lps array for the given pattern
    lps = compute_lps_array(pattern)
    
    # initialize a list to store occurrences of the pattern in the text
    occurrences = []
    i = 0
    j = 0  # Using 'j' to track the position in the pattern
    
    # iterate over the text
    while i < len(text):
        # check for a match
        if text[i] == pattern[j]:
            i += 1
            j += 1
            # check for a complete match
            if j == len(pattern):
                occurrences.append((i - j))
                # Reset j based on the lps array
                j = lps[j - 1]
        else:
            # If there is a mismatch, adjust j based on the lps array
            if j != 0:
                j = lps[j - 1]
            else:
                # If j is already 0, move to the next character in the text
                i += 1

    # Return the list of occurrences of the pattern in the text
    return occurrences

# example usage
text = "CODEWITHCODER"
pattern = "CODE"
occurrences = rabin_karp(text, pattern)
if occurrences:
    print(f"The pattern found at indices: {occurrences}.")
else:
    print("The pattern is not present in the text.")