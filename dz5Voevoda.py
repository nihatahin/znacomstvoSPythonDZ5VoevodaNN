import task1 as t1
import task2 as t2
import task3 as t3
import task4 as t4
import task5 as t5

def taskChoice():                   
    while True:
        global taskNum
        taskNum = int(input("Enter task number: "))
        if 0 < taskNum <= maxTaskNum:
            return
        else:
            print("Invalid task number was entered. Please, try again.")
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------            
def taskFuncChoice():
    global taskNum
    match taskNum:
        case 1:
            t1.task_enter()
        case 2:
            t2.task_enter()
        case 3:
            t3.task_enter()
        case 4:
            t4.task_enter()
        case 5:
            t5.task_enter()
        case _:
            print('Invalid task number')
#####################################################################
#####################################################################
##################################################################### 
taskNum = None
maxTaskNum = 5

while True:
    taskChoice()
    print()
    taskFuncChoice()
    print()

    
    