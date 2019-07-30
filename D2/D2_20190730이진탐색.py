T = int(input())
for test_case in range(1, T+1):
    PAB = list(map(int,input().split()))
    lA = [1, PAB[0]]
    lB = [1, PAB[0]]

    for i in range(20):
        if int((lA[0]+lA[1])/2) < PAB[1]:
            lA[0] = int((lA[0]+lA[1])/2)
        elif int((lA[0]+lA[1])/2) > PAB[1]:
            lA[1] = int((lA[0]+lA[1])/2)
        else :
            lA[0],lA[1] = PAB[1], PAB[1]
        if int((lB[0]+lB[1])/2) < PAB[2]:
            lB[0] = int((lB[0]+lB[1])/2)
        elif int((lB[0]+lB[1])/2) > PAB[2]:
            lB[1] = int((lB[0]+lB[1])/2)
        else :
            lB[0],lB[1] = PAB[2], PAB[2]
        if lA[0] == PAB[1] or lB[0] == PAB[2]:
            break
    if lA[0] == PAB[1] and lB[0] == PAB[2]:
        print('#{0} 0'.format(test_case))
    elif lA[0] == PAB[1]:
        print('#{0} A'.format(test_case))
    else:
        print('#{0} B'.format(test_case))