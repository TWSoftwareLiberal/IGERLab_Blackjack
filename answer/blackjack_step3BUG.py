# project: 21點_第三階段
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

# 將輸入之牌組分數加總 call by reference error
def calculate_points(cards):
    total_points = 0
    for i in range(len(cards)):
        
        if cards[i] == 'A':
            total_points += 11
        elif cards[i] == 'J':
            total_points += 10
        elif cards[i] == 'Q':
            total_points += 10
        elif cards[i] == 'K':
            total_points += 10
        else:
            total_points += int(cards[i])

    # 2張牌
    if len(cards) == 2:
        return total_points

    # 大於2張
    if total_points > 21:
        if 'A' in cards:
            total_points = total_points - 10 # make 11 point become 1 point
    return total_points


#================以下新增function=================
def play_blackjack():
    # 將玩家及莊家的牌組呈現出來
    user_cards = []
    dealer_cards = []

    # 1. 發第一張排給玩家
    # 2. 發第一張排給莊家
    # 3. 發第二張排給玩家
    # 4. 發第二張排給莊家
    for _ in range(2):
        user_cards.append(deal_card() # 缺少括號
        dealer_cards.append(deal_card())

    print(f"玩家的牌：{user_cards}")
    print(f"莊家的明牌：{dealer_cards}") #邏輯錯誤 莊家明牌只能顯示一張

    # 玩家的牌面、輸入介面(決定是否追加)
    ask_for_card = ""
    while ask_for_card = "n": #邏輯錯誤， 應為 !=
        ask_for_card = input("輸入y加牌、輸入n看結果：")

    if ask_for_card == "y": #縮排錯誤，導致邏輯錯誤(頭)
        user_cards.append(deal_card())
        user_points = calculate_points(user_cards)
        if user_points > 21:
            ask_for_card = "n"
        else:
            print(f"玩家的牌：{user_cards}")
    elif ask_for_card == "n":
        user_points = calculate_points(user_cards)
    else:
        print("請重新輸入！輸入y加牌、輸入n看結果：")#縮排錯誤，導致邏輯錯誤(尾)

    # 莊家牌面加總
    dealer_points = calculate_points(dealer_cards)
    
    #莊家加牌邏輯(此處沒有設計bug)
    if user_points <= 21:
        while dealer_points <= user_points :
            if dealer_points == user_points:
                if dealer_points < 17:
                    dealer_cards.append(deal_card())
                
                dealer_points = calculate_points(dealer_cards)
            else:
                dealer_cards.append(deal_card())
                dealer_points = calculate_points(dealer_cards)


    

    # 開牌
    print(f"玩家的牌：{user_cards}，共{user_points}點")
    print(f"莊家的牌：{dealer_cards}，共{dealer_points}點")

    # 勝負邏輯
    if user_points > 21:
        print("你輸了!")
    if dealer_points > 21:
        print("你贏了!") 
    if user_points == dealer_points:
        print("平手!")
    if user_points > dealer_points:
        print("你贏了!")# elif 打成 if
    else:
        print("你輸了!")

#================以上新增function=================
def game_loop():
    play_game = True

    play_blackjack()


    while play_game == True:
        print("=======================================")
        user_input = input("重新進行遊戲？請輸入y開始、輸入n結束：")
        if user_input == "y":
            play_blackjack()
        elif user_input == "n":
            play_game = False
            print("Bye~")
        else:
            continue

        if len(cards) < 6:
            print("牌數不足,請重開遊戲")
            


# main 
if __name__ == "__main__":
    
    print("歡迎來到21點遊戲！")

    game_loop()