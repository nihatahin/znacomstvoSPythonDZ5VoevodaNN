def task_enter():
    print(f'Task #{__name__[4:]}.')
    task_basic_func()
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task_basic_func():
    with open('t5_in.txt', 'r', encoding='utf-8') as f1:
        input_list = list(map(int, f1.read().split()))
    print(f"Input list\t\t\t\t- {input_list}")

    input_list = delete_repeat(input_list)
    print(f"Input list after repeat delete process\t- {input_list}")

    list_of_progs = prog_list(input_list)

    with open('t5_out.txt', 'w', encoding='utf-8') as f2:
        f2.write('')
    with open('t5_out.txt', 'a', encoding='utf-8') as f2:    
        for i in range(len(list_of_progs)):
            f2.write(str(list_of_progs[i]))
            f2.write('\n')
            print(f"Increasing sequence #{i + 1}\t\t\t- {list_of_progs[i]}")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def delete_repeat(lst):
    i = 0
    while i < len(lst):
        j = i + 1
        while j < len(lst): 
            if lst[i] == lst[j]:
                lst.pop(j)
            else:
                j += 1
        i += 1
    return(lst)
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def prog_list(lst):
    pr_lst = []
    length = len(lst)

    two_deg = 2
    for i in range(3, (2**length)):
        if two_deg * 2 <= i:
            two_deg *= 2
        else:
            mask = bin(i)[2:].rjust(length , '0')
            #print(mask)
            cur_lst = list_built(mask, lst)
            #print(cur_lst)
            if is_list_pos_seq(cur_lst):
                pr_lst.append(cur_lst[:])

    return pr_lst
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def list_built(msk, main_lst):
    new_lst = []
    for i in range(len(msk)):
        if msk[i] == '1':
            new_lst.append(main_lst[i])
    return new_lst
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def is_list_pos_seq(seq_lst):
    for i in range(1, len(seq_lst)):
        if seq_lst[i - 1] >= seq_lst[i]:
            return False
    else:
        return True
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
