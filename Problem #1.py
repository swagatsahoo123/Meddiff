def groupByOwners(files):
    result = {}
    for file, owner in files.items():
        result[owner] = result.get(owner, []) + [file]
    return result


n = int(input())
files = dict(input().split() for _ in range(n))
print(groupByOwners(files))