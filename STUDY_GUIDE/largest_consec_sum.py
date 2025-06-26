def list_of_consec_ints(lst):
    results = []
    for start in range(len(lst)):
        seen = set()
        for end in range(start, len(lst)):
            num = lst[end]
            if num in seen:
                break
            seen.add(num)
            results.append(lst[start:end + 1])
    return results

def return_highest_sum(list_of_ints):
    return max(sum(sublist) for sublist in list_of_consec_ints(list_of_ints))

print(return_highest_sum([1,2,3,3,4]))