import random
import re


def generate_number():
    """生成一个六位不重复的随机数字"""
    digits = list(range(10)) + ['A', 'B', 'C', 'D', 'E', 'F']
    random.shuffle(digits)
    return ''.join(map(str, digits[:6]))


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
    print("请在心中想好一个六位不重复的数字（例如：1234AB）")
    input("按下Enter键开始游戏...")
    print("======================================")

    # 初始化可能的数字列表
    possible_numbers = []
    digits = list(range(10)) + ['A', 'B', 'C', 'D', 'E', 'F']
    for i in range(16):
        for j in range(16):
            if i != j:
                for k in range(16):
                    if k != i and k != j:
                        for l in range(16):
                            if l != i and l != j and l != k:
                                for m in range(16):
                                    if m != i and m != j and m != k and m != l:
                                        for n in range(16):
                                            if n != i and n != j and n != k and n != l and n != m:
                                                possible_numbers.append(
                                                    [digits[i], digits[j], digits[k], digits[l], digits[m], digits[n]])

    while True:
        if not possible_numbers:
            print("找不到合适的猜测数字，请检查输入是否正确。")
            break

        # 随机选择一个猜测
        guess = random.choice(possible_numbers)
        guess_str = ''.join(map(str, guess))
        print("我的猜测是：", guess_str)

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

        if a == 6:
            print("我猜对了！答案是", guess_str)
            break

    print("======================================")
    print("游戏结束！")


# 运行电脑猜数字的游戏
computer_guess()