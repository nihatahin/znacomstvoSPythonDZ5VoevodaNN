import random

def task_enter():
    print(f'Task #{__name__[4:]}.')
    while True:
        print("Enter '/two' to start game of two players.")
        print("Enter '/one' to start game with bot.")
        stro = input("Enter '/break' to change task: ")
        if stro == '/break':
            return
        elif stro == '/two':
            task_two_players()
        elif stro == '/one':
            task_one_player()
        else:
            print("Invalid cmd. Try again.")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task_two_players():
    heap = 2021
    turn = False
    max_per_go = 28
    while True:
        if heap <= 0:
            print(f"{plyer_name_t2(not turn)} wins. {plyer_name_t2(turn)} must give all his candies to thre champion!")
            return
        else:
            cur_go = int(input(f"We have a small heap that consists of {heap} of candies. Your choice is limited with {max_per_go} candies. {plyer_name_t2(turn)}, how many candies would you like to take: "))
            if cur_go < 1:
                print("Invalid number! Try again.")
                continue
            elif cur_go > max_per_go:
                print("You took too much. Invalid! Unacceptable! Try again.")
                continue
            else:
                heap -= cur_go
                if max_per_go > heap:
                    max_per_go = heap
            turn = not turn
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def plyer_name_t2(t):
    if t:
        return 'Second player'
    else:
        return 'First player'
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def task_one_player():
    y_turn = bool(random.getrandbits(1))
    print(f"You are the {plyer_name_t2(y_turn).lower()}.")
    max_per_go = 28
    heap = 2021
    turn = False
    while True:
        if heap <= 0:
            print(f"{plyer_name_t2(not turn)} wins. {plyer_name_t2(turn)} must give all his candies to thre champion!")
            return
        else:
            if turn == y_turn:
                cur_go = int(input(f"We have a small heap that consists of {heap} of candies. Your choice is limited with {max_per_go} candies. {plyer_name_t2(turn)}, how many candies would you like to take: "))
            else:
                cur_go = bot_thoughts(heap, max_per_go)
                print(f"We have a small heap that consists of {heap} of candies. Your choice is limited with {max_per_go} candies. {plyer_name_t2(turn)}, how many candies would you like to take: {cur_go}")
            if cur_go < 1:
                print("Invalid number! Try again.")
                continue
            elif cur_go > max_per_go:
                print("You took too much. Invalid! Unacceptable! Try again.")
                continue
            else:
                heap -= cur_go
                if max_per_go > heap:
                    max_per_go = heap
            turn = not turn
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def bot_thoughts(h, max_p_g):
    if h <= max_p_g:
        c_go = max_p_g
    elif h == max_p_g + 1:
        c_go = 1
    else:
        if condition_one(h, max_p_g):
            c_go = (h - max_p_g - 1) % max_p_g        
        elif condition_two(h, max_p_g):
            c_go = max_p_g
        else:
            c_go = (h - 2 * max_p_g - 2) % max_p_g
            if c_go == 0:
                c_go = max_p_g
    return c_go
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def condition_one(hp, max_pg):
    return (((hp - max_pg - 1) // max_pg) % 2 == 0) and ((hp - max_pg - 1) % max_pg > 0)
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
def condition_two(hp, max_pg):
    return (((hp - max_pg - 1) // max_pg) % 2 > 0) and ((hp - max_pg - 1) % max_pg == 0)
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------