import random
import re


def generate_number():
    """生成一个四位不重复的随机数字"""
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:4]


def get_feedback(guess, answer):
    """根据猜测和答案计算A和B的数量"""
    a = sum(1 for x, y in zip(guess, answer) if x == y)
    b = sum(1 for x in guess if x in answer) - a
    return a, b


def validate_input(input_str):
    """验证玩家输入的格式是否正确"""
    pattern = r'^\dA\dB$'
    return re.match(pattern, input_str) is not None


def computer_guess():
    """电脑猜数字的主函数"""
    print("请在心中想好一个四位不重复的数字（例如：1234）")
    input("按下Enter键开始游戏...")
    print("======================================")

    # 初始化可能的数字列表
    possible_numbers = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    if i != j and i != k and i != l and j != k and j != l and k != l:
                        possible_numbers.append([i, j, k, l])

    while True:
        if not possible_numbers:
            print("找不到合适的猜测数字，请检查输入是否正确。")
            break

        # 随机选择一个猜测
        guess = random.choice(possible_numbers)
        print("我的猜测是：", ''.join(map(str, guess)))

        valid_input = False
        while not valid_input:
            feedback = input("请输入A和B的数量（例如：1A2B）：")
            valid_input = validate_input(feedback)
            if not valid_input:
                print("输入格式不正确，请重新输入。")

        a = int(feedback[0])
        b = int(feedback[2])

        # 根据反馈更新可能的数字列表
        possible_numbers = [num for num in possible_numbers if get_feedback(guess, num) == (a, b)]

        if a == 4:
            print("我猜对了！答案是", ''.join(map(str, guess)))
            break

    print("======================================")
    print("游戏结束！")


# 运行电脑猜数字的游戏
computer_guess()