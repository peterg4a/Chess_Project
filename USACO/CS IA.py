from calendar import *

def check(time):
    #set up cal
    cal = cr_cal()
    for task in tasklist:
        x = False
        for y in range(1, 2024):
            for m in range(1, 13):
                for d in range(monthrange(y,m)[1]):
                    if task[3] == [y, m, d]:
                        x = True
                    elif task[4] == [y,m,d]:
                        x = False
                    if x:
                        cal[y][m][d].append([task[1],task[-1]])

    
    tasktime = {}
    for task in tasklist:
        tasktime[task[1]] = task[4]
    workplan = cr_cal()
    #begin simulation
    for y in range(1, 2024):
        for m in range(1, 13):
            for d in range(1, monthrange(y,m)[1]+1):
                t = time
                for task in cal[y][m][d]:
                    print(task)
                    if tasktime[task[1]] >= 0:
                        if tasktime[task[1]] > t:
                            tasktime[task[1]] -= t
                            workplan[y][m][d].append([task[1], t])
                            break

                        else:
                            t -= tasks[i][1]
                            tasktime[task[1]] = 0
                            workplan[y][m][d].append([task[1], tasktime[task[1]]])
    out = True
    times = tasktime.values()
    for i in times:
        if i > 0:
            out = False
    return [out, workplan]


def optimise():
    l = 0
    r = 86400
    while r > l+1:
        m = (l+r)//2
        ans = check(m)
        if ans[0]:
            r = m
        else:
            l = m
    workplan = ans[1]


def cr_cal():
    calendar = [['null']]
    for y in range(1, 2024):
        year = [['null']]
        for m in range(1, 13):
            month = [['null']]
            for d in range(monthrange(y,m)[1]):
                month.append([])
            year.append(month)
        calendar.append(year)
    return calendar

calendar = cr_cal()
# print(calendar[2023][4])

tasklist = []
workplan = []

while True:
    print()
    print('X'*25)
    print('1. Manage Tasks/Events')
    print('2. View All Events/Tasks')
    print('3. Calculate Workplan')
    print('4. View Workplan')
    print('5. Quit Program')
    print('X'*25)
    choice = input('Enter your choice (1-5) : ')
    if choice == '1':
        while True:
            print()
            # print(calendar[2023][4])
            # print(tasklist)
            print('*'* 25)
            print("1. Add Event")
            print("2. Delete Event")
            print('3. Add Task')
            print("4. Delete Task")
            print("5. Return to Home Page")
            print('*'* 25)
            choice = input("Enter your choice (1-5): ")
            if choice == "1":
                date = input("Enter date (yyyy mm dd) : ").split()
                date = [int(i) for i in date]
                name = input("Enter event name : ")
                description = input('Enter event description : ')
                calendar[date[0]][date[1]][date[2]].append(['Event', name, description])
                print("Event added to", date)
            elif choice == '2':
                name = input("Enter the name of the event to be deleted : ")
                date = input("Enter date of the event (yyyy mm dd) : ").split()
                date = [int(i) for i in date]
                deleted = False
                for event in calendar[date[0]][date[1]][date[2]]:
                    if event[0] == 'Event' and event[1] == name:
                        calendar[date[0]][date[1]][date[2]].remove(event)
                        deleted = True
                        break
                if deleted:
                    print('Event -', name, '- deleted')
                else:
                    print('Deletion failed')
            elif choice == "3":
                name = input('Enter task name : ')
                description = input('Enter task description : ')
                s_date = input("Enter start date of task (yyyy mm dd) : ").split()
                s_date = [int(i) for i in s_date]
                f_date = input("Enter due date of task (yyyy mm dd) : ").split()
                f_date = [int(i) for i in f_date]
                line = input('Enter an estimate of the maximum time needed to complete the task (hours minutes) : ').split()
                line = [int(i) for i in line]
                # worktime in seconds
                worktime = (line[0]*3600)+(line[1]*60)
            
                tasklist.append(['Task', name, description, s_date, f_date, worktime])
                tasklist = sorted(tasklist, key=lambda x: (x[3][0], x[3][1], x[3][2]))
                calendar[s_date[0]][s_date[1]][s_date[2]].append(['Task', name, description, 'Start Date', worktime])
                calendar[f_date[0]][f_date[1]][f_date[2]].append(['Task', name, description, 'Due Date!', worktime])
                print('Task -', name, '- added')
            elif choice == "4":
                name = input("Enter the name of the task to be deleted : ")
                deleted = 0
                for y in range(1, 2024):
                    for m in range(1, 13):
                        for d in range(1, monthrange(y,m)[1]+1):
                            for task in calendar[y][m][d]:
                                if task[0] == 'Task' and task[1] == name:
                                    print(task)
                                    calendar[y][m][d].remove(task)
                                    for t in tasklist:
                                        if t[1] == task[1]:
                                            tasklist.remove(t)
                                    deleted += 1
                                    break
                if deleted == 2:
                    print('Task -', name, '- deleted')
                else:
                    print('Deletion failed')
            elif choice == "5":
                break
            else:
                print("Invalid choice, please try again")
    elif choice == '2':
        print()
        print('-'*25)
        print('All Events/Tasks')
        for y in range(1, 2024):
            for m in range(1, 13):
                for d in range(monthrange(y,m)[1]):
                    if len(calendar[y][m][d]) > 0 and calendar[y][m][d][0] != 'null':
                        print(y, m, d)
                        for task in calendar[y][m][d]:
                            print('     ', task)
                        print()
        print('-'*25)
    elif choice == '3':
        optimise()
    elif choice == '4':
        if len(workplan) == 0:
            print('No workplan created yet')
        else:
            for y in range(1, 2024):
                for m in range(1, 13):
                    for d in range(monthrange(y,m)[1]):
                        day_plan = workplan[y][m][d]
                        if len(day_plan) > 0:
                            print('On', [y,m,d], ':')
                            for i in dayplan:
                                print('     ', i)
    elif choice == '5':
        break
    else:
        print("Invalid choice, please try again")
