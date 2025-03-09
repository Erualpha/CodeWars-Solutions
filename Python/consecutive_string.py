def longest_consec(strarr, k):
    if not strarr or k > len(strarr) or k <= 0:
        return ""

    max_length = 0
    longest_str = ""

    for i in range(len(strarr) - k + 1): 
        current_str = "".join(strarr[i:i+k])  
        if len(current_str) > max_length:  
            max_length = len(current_str)
            longest_str = current_str

    return longest_str
