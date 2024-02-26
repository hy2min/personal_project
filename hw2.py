import random


def rps():

    win_count = 0
    lose_count = 0
    draw_count = 0

    flag = 0
    while True:
        rock_paper_scissor = ['가위', '바위', '보']
        random_rps_code = random.choice(rock_paper_scissor)

        if flag == 1:
            print('게임을 종료합니다.')
            print(f'승 : {win_count} 패 : {lose_count} 무승부 : {draw_count}')
            break

        my_choice = str(input('가위, 바위, 보 : '))
        if my_choice not in ('가위', '바위', '보'):
            print('다시 입력해주세요')
        elif my_choice == random_rps_code:
            print('비겼습니다.')
            draw_count += 1
        # 승패의 경우
        elif my_choice == '가위':
            if random_rps_code == '바위':
                print(f'나 : {my_choice} 컴퓨터 : {random_rps_code}')
                print('졌습니다.')
                lose_count += 1
                while True:
                    re_try = str.upper(input('다시 도전하시겠습니까? [Y/N] : '))
                    if re_try == 'Y':
                        flag = 0
                        break
                    elif re_try == 'N':
                        flag = 1
                        break
                    else:
                        print('Y 혹은 N로 입력해주세요.')
            else:
                print(f'나 : {my_choice} 컴퓨터 : {random_rps_code}')
                print('이겼습니다.')
                win_count += 1
                while True:
                    re_try = str.upper(input('다시 도전하시겠습니까? [Y/N] : '))
                    if re_try == 'Y':
                        flag = 0
                        break
                    elif re_try == 'N':
                        flag = 1
                        break
                    else:
                        print('Y 혹은 N로 입력해주세요.')
        elif my_choice == '바위':
            if random_rps_code == '보':
                print(f'나 : {my_choice} 컴퓨터 : {random_rps_code}')
                print('졌습니다.')
                lose_count += 1
                while True:
                    re_try = str.upper(input('다시 도전하시겠습니까? [Y/N] : '))
                    if re_try == 'Y':
                        flag = 0
                        break
                    elif re_try == 'N':
                        flag = 1
                        break
                    else:
                        print('Y 혹은 N로 입력해주세요.')
            else:
                print(f'나 : {my_choice} 컴퓨터 : {random_rps_code}')
                print('이겼습니다.')
                win_count += 1
                while True:
                    re_try = str.upper(input('다시 도전하시겠습니까? [Y/N] : '))
                    if re_try == 'Y':
                        flag = 0
                        break
                    elif re_try == 'N':
                        flag = 1
                        break
                    else:
                        print('Y 혹은 N로 입력해주세요.')
        else:
            if random_rps_code == '가위':
                print(f'나 : {my_choice} 컴퓨터 : {random_rps_code}')
                print('졌습니다.')
                lose_count += 1
                while True:
                    re_try = str.upper(input('다시 도전하시겠습니까? [Y/N] : '))
                    if re_try == 'Y':
                        flag = 0
                        break
                    elif re_try == 'N':
                        flag = 1
                        break
                    else:
                        print('Y 혹은 N로 입력해주세요.')
            else:
                print(f'나 : {my_choice} 컴퓨터 : {random_rps_code}')
                print('이겼습니다.')
                win_count += 1
                while True:
                    re_try = str.upper(input('다시 도전하시겠습니까? [Y/N] : '))
                    if re_try == 'Y':
                        flag = 0
                        break
                    elif re_try == 'N':
                        flag = 1
                        break
                    else:
                        print('Y 혹은 N로 입력해주세요.')

        if flag == 1:
            print('게임을 종료합니다.')
            print(f'승 : {win_count} 패 : {lose_count} 무승부 : {draw_count}')
            break


rps()
