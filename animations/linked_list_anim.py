import os, time

RED='\033[91m'
GREEN='\033[92m'
YELLOW='\033[93m'
BLUE='\033[94m'
MAGENTA='\033[95m'
CYAN='\033[96m'
WHITE='\033[97m'
BOLD='\033[1m'
BLINK='\033[5m'
RESET='\033[0m'


def clear():
    os.system('cls' if os.name=='nt' else 'clear')


def pause(sec=1.2):
    time.sleep(sec)


def neon_line(w=72):
    print(CYAN + '═'*w + RESET)


def show_list(arr, title='LINKED LIST', highlight=None):
    clear()
    neon_line()
    print(MAGENTA + BOLD + title.center(72) + RESET)
    neon_line()
    if not arr:
        print('\n' + RED + BOLD + '              [ EMPTY LINKED LIST ]' + RESET + '\n')
        neon_line()
        return
    print()
    parts=[]
    for i,v in enumerate(arr):
        color = GREEN if i==highlight else YELLOW
        node = color + BOLD + f'⟪{str(v).center(5)}⟫' + RESET
        parts.append(node)
    print((' ' + CYAN + '=> ' + RESET).join(parts) + ' ' + CYAN + '=> NULL' + RESET)
    idx=' '.join(WHITE + f'{i:^7}' + RESET for i in range(len(arr)))
    print(idx)
    print('\n' + CYAN + BOLD + f'⚡ Size: {len(arr)}' + RESET)
    neon_line()


def insert_begin(arr):
    try: val=int(input('\nEnter value to insert at beginning: '))
    except: return
    for s in range(3):
        show_list(arr,'INSERT BEGINNING')
        print(BLUE + f'\nMoving {val}' + '.'*(s+1) + RESET)
        print(CYAN + '\n⚡⚡ [ ] --> HEAD' + RESET)
        pause(0.35)
    arr.insert(0,val)
    show_list(arr,'AFTER INSERT',0)
    pause(2)


def insert_end(arr):
    try: val=int(input('\nEnter value to insert at end: '))
    except: return
    for s in range(3):
        show_list(arr,'INSERT END')
        print(BLUE + f'\nMoving {val}' + '.'*(s+1) + RESET)
        print(CYAN + '\n                    --> [ ] ⚡⚡' + RESET)
        pause(0.35)
    arr.append(val)
    show_list(arr,'AFTER INSERT',len(arr)-1)
    pause(2)


def delete_value(arr):
    if not arr:
        show_list(arr,'DELETE NODE')
        pause(1.5)
        return

    show_list(arr,'DELETE NODE')
    try:
        val=int(input('\nEnter value to delete: '))
    except: return
    if val not in arr:
        show_list(arr,'DELETE NODE')
        print(RED + '\nValue not found!' + RESET)
        pause(2)
        return
    idx=arr.index(val)
    for s in range(3):
        show_list(arr,'DELETE NODE',idx)
        print(YELLOW + f'\nRemoving {val}' + '.'*(s+1) + RESET)
        print(MAGENTA + '\n<-- ⚡⚡ [ ]' + RESET)
        pause(0.35)
    arr.pop(idx)
    show_list(arr,'AFTER DELETE')
    pause(2)


def search_value(arr):
    if not arr:
        show_list(arr,'SEARCH NODE')
        pause(1.5)
        return

    show_list(arr,'SEARCH NODE')
    try:
        target=int(input('\nEnter value to search: '))
    except: return
    for i,v in enumerate(arr):
        show_list(arr,'SEARCH NODE',i)
        print(BLUE + f'\nChecking node {i}: {v}' + RESET)
        pause(0.8)
        if v==target:
            print(GREEN + BOLD + f'\nFound {target} at node {i}' + RESET)
            pause(2)
            return
    print(RED + '\nNot found!' + RESET)
    pause(2)


def display(arr):
    show_list(arr,'DISPLAY LIST')
    pause(2)


def linked_list_animation():
    arr=[10,20,30]
    while True:
        clear()
        print(CYAN + '═'*40 + RESET)
        print(MAGENTA + BOLD + BLINK + 'LINKED LIST ANIMATIONS'.center(40) + RESET)
        print(CYAN + '═'*40 + RESET)
        print(GREEN + BOLD + '⚡ 1. Insert Beginning' + RESET)
        print(YELLOW + BOLD + '⚡ 2. Insert End' + RESET)
        print(CYAN + BOLD + '⚡ 3. Delete Value' + RESET)
        print(BLUE + BOLD + '⚡ 4. Search' + RESET)
        print(MAGENTA + BOLD + '⚡ 5. Display' + RESET)
        print(RED + BOLD + '⚡ 6. Back' + RESET)
        ch=input('\nEnter choice: ')
        if ch=='1': insert_begin(arr)
        elif ch=='2': insert_end(arr)
        elif ch=='3': delete_value(arr)
        elif ch=='4': search_value(arr)
        elif ch=='5': display(arr)
        elif ch=='6': break
        else: pause(0.8)

if __name__=='__main__':
    linked_list_animation()