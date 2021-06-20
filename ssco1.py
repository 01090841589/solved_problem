import sys
sys.stdin = open("ssco1.txt")
S = input()
C = input()


import re
from collections import defaultdict
email_lists = defaultdict(int)
C = "@"+C.lower()+".com"
lists = []
emails = list(map(str, S.split("; ")))
for email in emails:
    lo_email = email.lower()
    name = list(map(str, lo_email.split()))
    first = re.sub('[^0-9a-z]', '', name[0])
    last = re.sub('[^0-9a-z]', '', name[-1])
    left_side = first[:8]+"."+last[:8]
    email_lists[left_side] += 1
    if email_lists[left_side] > 1:
        lists.append("{} <{}{}{}>".format(email, left_side, email_lists[left_side], C))
    else:
        lists.append("{} <{}{}>".format(email, left_side, C))

print("; ".join(lists))

