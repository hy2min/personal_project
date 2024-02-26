import random


def updown():

    random_number = random.randint(1, 100)
    attempts = 0

    flag = 0
    while True:
        try:
            my_number = int(input('1~100 사이의 숫자를 입력하시오. : '))
            attempts += 1
        except ValueError:
            print('숫자를 입력하세요')

        if my_number > 100:
            print('범위 내의 숫자를 입력하세요.')
        elif random_number == my_number:
            print(f'정답입니다. {attempts}번 만에 맞추셨습니다.')
            while True:
                try_again = (input(f'다시 도전하시겠습니까?(Y/N) :  '))
                if try_again == 'Y':
                    updown()
                elif try_again == 'N':
                    flag = 1
                    break
                else:
                    print('Y 혹은 N를 입력해주십시오.')
        elif random_number > my_number:
            print('UP')
        elif random_number < my_number:
            print('DOWN')
        if flag == 1:
            break


updown()
