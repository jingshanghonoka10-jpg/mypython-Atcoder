#辞書作成
player = {"Taro":85,"Jiro":92,"Saburo":78}

#入力して検索
name = input()
if name in player:
    print(player[name])
else:
    print("Not found!")

# inを使ったif文の代わりになる魔法の書き方
print(player.get(name, "Not Found"))