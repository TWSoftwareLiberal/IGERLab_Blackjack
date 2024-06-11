# project: 21點_第二階段

import random
# 作一組52張撲克牌
# J、Q、K 皆為 10 點
# A 為 1 或 11 點
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4

# 做一個 function 隨機出牌
# 出牌後將此排從排組中取出
def deal_card():
    card = random.choice(cards)
    cards.remove(card)
    return card


#================以下新增function=================
# 將輸入之牌組分數加總
def calculate_points(cards):
    
    for i in range(len(cards)):
        total_points = 0 
        if cards[i] = 'A':
            total_points += 11
        if cards[i] = 'J':
            total_points += 10
        if cards[i] = 'Q': 
            total_points += 10
        if cards[i] = 'K': 
            total_points += 10
        else:
            total_points += cards[i] 

    # 2張牌
    if len(cards) == 2: 
        return total_points

    # 大於2張
    if total_points > 21:
        if 'A' in cards:
            total_points = total_points - 11  
    return total_points
#================以上新增function=================

def game_loop():
    play_game = True

    user_cards = []

    for _ in range(2):
        user_cards.append(deal_card())

    print(user_cards)
    user_point = calculate_points(user_cards)
    print(user_point)

    while play_game == True:
        print("=======================================")
        user_input = input("重新進行遊戲？請輸入y開始、輸入n結束：")
        if user_input == "y":
            user_cards = []
            for _ in range(2):     
                user_cards.append(deal_card())
            
            print(user_cards)
            user_point = calculate_points(user_cards)
            print(user_point)

        elif user_input == "n":
            play_game = False
            print("Bye~")
        else:
            continue

# main 
if __name__ == "__main__":
    
    print("歡迎來到21點遊戲第二階段--加總")

    game_loop()
    
