# import requests
# 자음모음
'''
word = input()
vowels = 0
consonants = 0
for i in range(len(word)):
    if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u':
        vowels += 1
    else:
        consonants += 1
print(vowels,consonants)
'''
# url = "https://api.bithumb.com/public/ticker/btc"
# data = requests.get(url).json()['data']
# print(data)


'''
my_str = "Life is too short, you need python"
for i in list(my_str):
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        continue
    else :
        print(i,end='')
'''
'''
phone = input()
if phone[0]+phone[1]+phone[2] != '010' or len(phone) != 11:
    print("핸드폰번호를 입력하세요")
else :
    print('*'*7 + phone[7]+ phone[8]+ phone[9]+ phone[10])
'''