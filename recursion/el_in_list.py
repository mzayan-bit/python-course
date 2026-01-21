lst = [1,2,3,4,5,6,7,8,9,10]

def el_in_list(lst, idx):
    if idx == len(lst):
        return
    print(lst[idx])
    el_in_list(lst, idx + 1)

el_in_list(lst, 0)
