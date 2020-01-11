# 3. 도시별 최근 3일 온도 입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9]
}
# 도시별 최근 3일의 온도 평균은
# for i in city.keys() :
#     print('{0}의 온도 평균은 {1}입니다.'.format(i,sum(city[i])/len(city[i])))

# 도시 중 최근 3일 중에 가장 추웠떤, 가장 더웠던 곳은
hot = ['',0]
cold = ['',0]
for city_name, temp in city.items():
    for j in range(len(temp)):
        if(temp[j]) > hot[1] :
            hot = [city_name,temp[j]]
        elif(temp[j]) < cold[1] :
            cold = [city_name,temp[j]]
print(hot,cold)