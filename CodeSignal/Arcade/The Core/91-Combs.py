def solution(comb1, comb2):
    bin_str1 = comb1.replace("*", "1").replace(".", "0")
    bin_str2 = comb2.replace("*", "1").replace(".", "0")
    offset1 = len(bin_str2)
    length_strs = len(bin_str1) + len(bin_str2)
    minimum = length_strs
    temp_min = 0
    bin1 = int(bin_str1, 2) << offset1
    bin2 = int(bin_str2, 2)
    for i in range(length_strs):
        temp_min = max(i + len(bin_str2), length_strs) - min(i, offset1)
        if not (bin1 & (bin2 << i)) and temp_min < minimum:
            minimum = temp_min
    return minimum
