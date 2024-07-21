import random
import re
from itertools import permutations

def generate_number():
    """生成一個十位不重複的亂數字"""
    digits = list(range(10))
    random.shuffle(digits)
    return digits

def get_feedback(guess, answer):
    """根據猜測和答案計算A和B的數量"""
    a = sum(1 for x, y in zip(guess, answer) if x == y)
    b = sum(1 for x in guess if x in answer) - a
    return a, b

def validate_input(input_str):
    """驗證玩家輸入的格式是否正確"""
    pattern = r'^\d{2}A\d{2}B$'
    return re.match(pattern, input_str) is not None

def computer_guess():
    """電腦猜數位的主函數"""
    print("請在心中想好一個十位元不重複的數位（例如：0123456789）")
    input("按下Enter鍵開始遊戲...")
    print("======================================")

    # 使用 permutations 生成所有可能的十位元不重複數位
    possible_numbers = list(permutations(range(10), 10))

    while True:
        if not possible_numbers:
            print("找不到合適的猜測數字，請檢查輸入是否正確。")
            break

        # 隨機選擇一個猜測
        guess = random.choice(possible_numbers)
        print("我的猜測是：", ''.join(map(str, guess)))

        valid_input = False
        while not valid_input:
            feedback = input("請輸入A和B的數量（例如：01A02B）：")
            valid_input = validate_input(feedback)
            if not valid_input:
                print("輸入格式不正確，請重新輸入。")

        a = int(feedback[:2])
        b = int(feedback[3:5])

        # 根據回饋更新可能的數位清單
        possible_numbers = [num for num in possible_numbers if get_feedback(guess, num) == (a, b)]

        # 列印剩餘的有效組合數
        print(f"目前剩餘有效組合數：{len(possible_numbers)}")

        if a == 10:
            print("我猜對了！答案是", ''.join(map(str, guess)))
            break

    print("======================================")
    print("遊戲結束！")

# 運行電腦猜數位的遊戲
computer_guess()
