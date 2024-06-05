import calendar

def get_date():
    year = int(input('Enter year: '))
    month = int(input('Enter month: '))
    day = int(input('Enter day: '))
    return (year, month, day)

def add_task(calendar_dict):
    date = get_date()
    task = input('Enter task: ')
    if date not in calendar_dict:
        calendar_dict[date] = []
    calendar_dict[date].append(task)

def print_calendar(calendar_dict):
    year = int(input('Enter year: '))
    month = int(input('Enter month: '))
    cal = calendar.monthcalendar(year, month)
    for week in cal:
        for day in week:
            if day == 0:
                print('  ', end='')
            else:
                date = (year, month, day)
                if date in calendar_dict:
                    tasks = calendar_dict[date]
                    print(f'{day:2}*', end='')
                    for task in tasks:
                        print(f'    {task}')
                else:
                    print(f'{day:2} ', end='')
        print()

def main():
    calendar_dict = {}
    while True:
        print('1. Add task')
        print('2. Print calendar')
        print('3. Exit')
        choice = input('Enter choice: ')
        if choice == '1':
            add_task(calendar_dict)
        elif choice == '2':
            print_calendar(calendar_dict)
        elif choice == '3':
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()
