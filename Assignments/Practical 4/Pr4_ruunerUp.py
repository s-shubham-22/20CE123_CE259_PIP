n = int(input())
ranks = [int(item) for item in input().split(" ")]
ranks_dict = list(dict.fromkeys(ranks))
ranks_dict.sort()

print(ranks_dict[-2])