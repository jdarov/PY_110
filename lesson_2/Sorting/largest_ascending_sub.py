def all_substrings(string):
    all_subs = list()
    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            all_subs.append(string[i:j])
    return all_subs

def length_ascending(substring):
    return len(substring) if substring == ''.join(sorted(substring)) else 0

def largest_ascending_sub(string):
    return max(all_substrings(string), key=length_ascending)

print(largest_ascending_sub('asd') == 'as')
print(largest_ascending_sub('zyxv') == 'z')
print(largest_ascending_sub('aatttba') == 'aattt')