"""
 You are given a list of characters. what is the least popular character in the list? Return number of occurrences of the least popular character and the list of characters that have occurred that many times. 
"""

from collections import Counter
def least_polular(chars = ["a", "a", "b", "b", "b", "c", "d"]):
    char_counter  = Counter(chars)
    least_chars = []
    
    least_num = char_counter.most_common()[-1][1]
    
    for key, value in char_counter.items():
        if value == least_num:
            least_chars.append(key)
    return least_num, least_chars

