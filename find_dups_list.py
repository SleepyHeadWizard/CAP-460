list = 'a', 'a', 'b', 'c', 'd', 'f', 'f'
watcher = []
dups = []

print(list)


for i in list:
    if i not in watcher:
        watcher.append(i)
        dups.append(i)
    else:
        if i in dups:
            dups.remove(i)

print("Unique:", dups)


sample_list = ['abc', 'xyz', 'aba', '1221']

count = 0

for string in sample_list:
    if len(string) >= 2 and string[0] == string[-1]:
        count += 1

print(count)