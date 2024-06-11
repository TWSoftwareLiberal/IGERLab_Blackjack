# project: 21點_第一階段



# 作一組52張撲克牌
# J、Q、K 皆為 10 點
# A 為 1 或 11 點
cards = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K] * 4

# 做一個 function 隨機出牌
# 出牌後將此排從排組中取出
def deal_card():
    card = random.choice(cards)
    cards.remove(card)


def game_loop():
    play_game = True
    
    while play_game == True:
        print("=======================================")
        user_input = input("重新進行遊戲？請輸入y開始、輸入n結束：")
        if user_input == "y":
            print(deal_card())
        elif user_input == "n":
            play_game = False
            print("Bye~")
        else:
            continue

# main 
if __name__ == "__main__":

    print("歡迎來到21點遊戲第一階段--洗牌")
    print(deal_card())

    game_loop()
    