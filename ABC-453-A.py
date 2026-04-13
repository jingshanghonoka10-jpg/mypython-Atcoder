#自作コード：問題が理解できなかった？解けなかった
#お試しコードにはなかったけどoobooみたいな例だったとき先頭のooのみ消すところ、これでは後ろのも消してしまう
N = int(input())
S = input()
Ans = []
if S[0] == "o":

    for i in range(N):
        if S[i] != "o":
            Ans += S[i]

    print("".join(Ans))

else:
    print(S)


#geminiより解答
N = int(input())
S = input()

# 'o'以外の文字が初めて現れる位置（インデックス）を探す
start = N  # もし文字が全部 'o' だった時のために、初期値を文字数(N)にしておく

for i in range(N):
    if S[i] != 'o':
        start = i # 'o' 以外が見つかったら、その場所を記録
        break     # 見つかったらそれ以降は探さなくていいのでループを抜ける

# 見つかった位置から最後までを「スライス」で切り出して出力
# （全部 'o' だった場合は S[N:] となり、問題の指示通り空文字列が出力されます）
print(S[start:])