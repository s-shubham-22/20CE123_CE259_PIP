import random as r

def shuffle_list1(li):
    r.shuffle(li)
    return li

def shuffle_list2(li):
    return r.sample(li, k=len(li))

def shuffle_list3(li):
    n = len(li)
    for _ in range(n):
        temp = r.randint(0, n-1)
        element = li.pop(temp)
        li.append(element)
    return li

def user_id_gen_by_user(length, user):
    pasList = []
    li = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    n = len(li)
    for _ in range(user):
        pas = ""
        for _ in range(length):
            pas += li[r.randint(0, n-1)]
        pasList.append(pas)
    return pasList


li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Random List 1: {shuffle_list1(li)}")
print(f"Random List 2: {shuffle_list2(li)}")
print(f"Random List 3: {shuffle_list3(li)}")

print(f"Random password Query 1:(5, 5) {user_id_gen_by_user(5, 5)}")
print(f"Random password Query 1:(16, 3) {user_id_gen_by_user(16, 3)}")
