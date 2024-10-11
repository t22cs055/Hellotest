import random

def janken():
    # じゃんけんの手を定義（0: グー, 1: チョキ, 2: パー）
    hands = ["グー", "チョキ", "パー"]
    
    # AとBの手をランダムに選択
    a_hand = random.randint(0, 2)
    b_hand = random.randint(0, 2)
    ###
    # 結果を出力
    print(f"Aの手: {hands[a_hand]} v.s. Bの手: {hands[b_hand]}", end=" → ")
    
    # 勝敗判定
    if a_hand == b_hand:
        print("引き分け")
    elif (a_hand == 0 and b_hand == 1) or (a_hand == 1 and b_hand == 2) or (a_hand == 2 and b_hand == 0):
        print("Aの勝ち")
    else:
        print("Bの勝ち")