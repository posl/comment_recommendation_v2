def unique_substrings_in_wraparound_string(s):
    if not s:
        return 0
    if len(s) == 1:
        return 1
    result = 0
    curr = 0
    count = [0] * 26
    for i in range(len(s)):
        curr = ord(s[i]) - ord('a')
        if i > 0 and ord(s[i - 1]) != (curr - 1) % 26 + ord('a'):
            count[curr] = 0
        count[curr] = max(count[curr], 1)
        result = max(result, count[curr])
    return result
print(unique_substrings_in_wraparound_string("zab"))
print(unique_substrings_in_wraparound_string("cac"))
print(unique_substrings_in_wraparound_string("a"))
print(unique_substrings_in_wraparound_string("zabzabc"))
print(unique_substrings_in_wraparound_string("zabzabzab"))
print(unique_substrings_in_wraparound_string("zabzabzaba"))
print(unique_substrings_in_wraparound_string("zabzabzabaz"))
print(unique_substrings_in_wraparound_string("zabzabzabaza"))
print(unique_substrings_in_wraparound_string("zabzabzabazab"))
print(unique_substrings_in_wraparound_string("zabzabzabazaba"))
print(unique_substrings_in_wraparound_string("zabzabzabazabaz"))
print(unique_substrings_in_wraparound_string("zabzabzabazabaza"))
print(unique_substrings_in_wraparound_string("zabzabzabazabazab"))
print(unique_substrings_in_wraparound_string("zabzabzabazabazaba"))
print(unique_substrings_in_wraparound_string("zabzabzabazabazabaz"))
print(unique_substrings_in_wraparound_string("zabzabzabazabazabaza"))
print(unique_substrings_in_wraparound_string("zabzabzabazabazabazab"))
print(unique_substrings_in_wraparound_string("zabzabzabazabazabazaba"))
print(unique_substrings_in_wraparound_string("zabzabzabazabazabazabaz"))
print(unique_substrings_in_wraparound_string("zabzabzabazabazabazabaza"))
print(unique_sub

if __name__ == '__main__':
    unique_substrings_in_wraparound_string()