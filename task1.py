def task_enter():
    print(f'Task #{__name__[4:]}.')
    while True:
        d = input("Enter string for 'abc' list deleting or '/break' to change task: ")
        if d == '/break':
            return
        else:
            task_basic_func(d.split())
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task_basic_func(in_data):
    frag = 'abc'
    print(in_data)
    print(list(filter(lambda s: not(frag in s), in_data)))
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------