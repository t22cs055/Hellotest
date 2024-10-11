import random

def janken_3_rounds(num_players=2):
    # じゃんけんの手を定義（0: グー, 1: チョキ, 2: パー）
    hands = ["グー", "チョキ", "パー"]
    
    # 各プレイヤーの勝利数を記録
    player_wins = [0] * num_players
    
    # 3回勝負
    rounds = 3
    for round_num in range(1, rounds + 1):
        print(f"=== 第{round_num}回戦 ===")
        
        # 各プレイヤーの手をランダムに選択
        player_hands = [random.randint(0, 2) for _ in range(num_players)]
        
        # プレイヤーの手を表示
        for i in range(num_players):
            print(f"プレイヤー{i + 1}の手: {hands[player_hands[i]]}")
        
        # 勝敗判定
        winners = determine_winner(player_hands)
        
        if len(winners) == num_players:
            print("引き分け！再試合です。")
        else:
            for winner in winners:
                player_wins[winner] += 1
            winner_names = "、".join([f"プレイヤー{winner + 1}" for winner in winners])
            print(f"{winner_names}がこのラウンドの勝者です。")
    
    # 最終的な勝者を決定
    max_wins = max(player_wins)
    final_winners = [i for i, wins in enumerate(player_wins) if wins == max_wins]
    
    if len(final_winners) == 1:
        print(f"\nプレイヤー{final_winners[0] + 1}が最終勝者です！")
    else:
        print("\n複数のプレイヤーが同じ勝利数で引き分けです。再戦します！")
        # 再戦（同じ勝利数のプレイヤーだけで3回勝負）
        janken_replay(final_winners, hands)

def janken_replay(players, hands):
    # 再戦用関数（再戦するプレイヤーたちだけで3回勝負）
    player_wins = [0] * len(players)
    rounds = 3
    
    for round_num in range(1, rounds + 1):
        print(f"\n=== 再戦 第{round_num}回戦 ===")
        
        # 再戦プレイヤーの手をランダムに選択
        player_hands = [random.randint(0, 2) for _ in range(len(players))]
        
        # プレイヤーの手を表示
        for i, player in enumerate(players):
            print(f"プレイヤー{player + 1}の手: {hands[player_hands[i]]}")
        
        # 勝敗判定
        winners = determine_winner(player_hands)
        
        if len(winners) == len(players):
            print("再戦も引き分け！再試合です。")
        else:
            for winner in winners:
                player_wins[winner] += 1
            winner_names = "、".join([f"プレイヤー{players[winner] + 1}" for winner in winners])
            print(f"{winner_names}がこのラウンドの勝者です。")
    
    # 再戦の最終結果
    max_wins = max(player_wins)
    final_winners = [i for i, wins in enumerate(player_wins) if wins == max_wins]
    
    if len(final_winners) == 1:
        print(f"\nプレイヤー{players[final_winners[0]] + 1}が再戦の最終勝者です！")
    else:
        print("\n再戦でも複数勝者が出ました。再々戦が必要です！")
        # 再再戦（引き分けが続く場合）
        janken_replay([players[i] for i in final_winners], hands)

def determine_winner(player_hands):
    # 勝者を決定（最も多くのプレイヤーに勝てる手を持っている人）
    winners = []
    num_players = len(player_hands)
    
    for i in range(num_players):
        is_winner = True
        for j in range(num_players):
            if i != j and not beats(player_hands[i], player_hands[j]):
                is_winner = False
                break
        if is_winner:
            winners.append(i)
    
    if len(winners) == 0:
        return list(range(num_players))  # 引き分け
    return winners

def beats(hand1, hand2):
    # hand1がhand2に勝つかどうかを判定
    return (hand1 == 0 and hand2 == 1) or (hand1 == 1 and hand2 == 2) or (hand1 == 2 and hand1 == 0)

# 実行例 (3人プレイヤーでの3回勝負)
janken_3_rounds(3)
