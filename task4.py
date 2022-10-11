from random import randrange

def task_enter():
    print(f'Task #{__name__[4:]}.')
    while True:
        int_num = input("Enter string or '/break' to change task: ")
        if int_num == '/break':
            return
        else:
            task_basic_func(int_num)
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task_basic_func(in_data):
    d_rle = transform(in_data)
    print(f"Straigt RLE transformation: {d_rle}.")
    i_rle = inverse(d_rle)
    print(f"Inverse RLE transformation: {i_rle}.")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def transform(inp):
    outp = ''
    cur_sym = inp[0]
    cnt = 1
    for i in range(1, len(inp)):
        if cur_sym != inp[i]:
            outp += str(cnt) + cur_sym
            cur_sym = inp[i]
            cnt = 1
        elif cnt >= 9:
            outp += str(cnt) + cur_sym
            cnt = 1
        else:
            cnt += 1
    outp += str(cnt) + cur_sym

    return outp
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def inverse(inp):
    outp = ''
    for i in range(0, len(inp), 2):
        outp += int(inp[i]) * inp[i + 1]
    return outp