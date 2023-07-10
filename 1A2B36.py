import random
import re
import itertools


def generate_number():
    """生成一个36位不重复的随机数字"""
    digits = list(range(10)) + list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') + list('abcdefghijklmnopqrstuvwxyz')
    random.shuffle(digits)
    return ''.join(map(str, digits[:36]))


def get_feedback(guess, answer):
    """根据猜测和答案计算A和B的数量"""
    a = sum(1 for x, y in zip(guess, answer) if x == y)
    b = sum(1 for x in guess if x in answer) - a
    return a, b


def validate_input(input_str):
    """验证玩家输入的格式是否正确"""
    pattern = r'^\d{1,2}A\d{1,2}B$'
    return re.match(pattern, input_str) is not None


def computer_guess():
    """电脑猜数字的主函数"""
    print("请在心中想好一个36位不重复的数字（例如：1234ABcdEFghIJklMNopQRstUVwxYZab）")
    input("按下Enter键开始游戏...")
    print("======================================")

    # 初始化可能的数字列表
    possible_numbers = []
    digits = list(range(10)) + list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') + list('abcdefghijklmnopqrstuvwxyz')
    # 使用itertools.permutations生成所有36位不重复的数字
    for num in itertools.permutations(digits, 36):
        # 把每个数字转换成字符串并添加到列表中
        possible_numbers.append(''.join(map(str, num)))

    while True:
        if not possible_numbers:
            print("找不到合适的猜测数字，请检查输入是否正确。")
            break

        # 随机选择一个猜测
        guess = random.choice(possible_numbers)
        print("我的猜测是：", guess)

        valid_input = False
        while not valid_input:
            feedback = input("请输入A和B的数量（例如：1A2B）：")
            valid_input = validate_input(feedback)
            if not valid_input:
                print("输入格式不正确，请重新输入。")

        a = int(feedback.split('A')[0])
        b = int(feedback.split('B')[0])

        # 根据反馈更新可能的数字列表
        possible_numbers = [num for num in possible_numbers if get_feedback(guess, num) == (a, b)]

        if a == 36:
            print("我猜对了！答案是", guess)
            break

    print("======================================")
    print("游戏结束！")


# 运行电脑猜数字的游戏
computer_guess()