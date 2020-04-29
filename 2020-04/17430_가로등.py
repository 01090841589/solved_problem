import sys

sys.stdin = open("가로등.txt")


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    road = [[0]*N for _ in range(N)]
    for i in range(N):
        a, b = map(int, input().split())





    print(road)
    


car_lists = {'2017 hyundai i30':'2017 i30 N', '2018 DAECHANG danigo':'2018 다니고', '2018 HYUNDAI grand_starex_limuzine':'2018 그랜드 스타렉스 리무진',
 '2018 hyundai LAFESTA':'2018 라페스타', '2018 HYUNDAI nexo':'2018 넥쏘', '2018 HYUNDAI Veloster':'2018 벨로스터',
 '2018 KIA Ceed_SW':'2018 씨드 SW', '2018 KIA Niro_EV':'2018 니로 EV', '2019 DAECHANG Danago_III':'2019 다니고 III 픽업',
'2019 HYUNDAI Accent':'2019 엑센트', '2019 HYUNDAI Genesis_G90':'2019 G90', '2019 HYUNDAI i30':'2019 i30',
'2019 HYUNDAI Ioniq':'2019 아이오닉 하이브리드', '2019 HYUNDAI Palisade':'2019 팰리세이드', '2019 HYUNDAI SANTA_FE':'2019 싼타페',
'2019 HYUNDAI Solati':'2019 쏠라티', '2020 HYUNDAI Sonata':'2020 쏘나타', '2019 HYUNDAI VENUE': '2019 베뉴',
'2019 KIA Ceed':'2019 씨드', '2019 KIA K7':'2019 K7', '2019 KIA morning':'2019 모닝',
'2019 KIA niro_hybrid':'2019 니로 하이브리드', '2019 KIA Rio':'2019 리오 세단', '2019 KIA Seltos':'2019 셀토스',
'2019 KIA Stonic':'2019 스토닉', '2020 CAMSYS CEVO-C':'2020 캠시스 CEVO-C', '2020 GM DAMAS':'2020 다마스',
'2020 GM LABO':'2020 라보', '2020 HYUNDAI Aura':'2020 아우라', '2020 HYUNDAI Avante':'2020 아반떼',
'2020 HYUNDAI Creta ix25':'2020 ix25', '2020 HYUNDAI Genesis Gv80':'2020 GV80', '2020 HYUNDAI Genesis_G70':'2020 G70',
'2020 HYUNDAI Grand i10':'2020 i10', '2020 HYUNDAI Grand Starex':'2020 그랜드 스타렉스', '2020 HYUNDAI Grandeur':'2020 그랜저',
'2020 HYUNDAI I20 Elite':'2020 i20', '2020 HYUNDAI i30':'2020 i30 왜건', '2020 HYUNDAI Kona':'2020 코나',
'2020 HYUNDAI Lafesta':'2020 라페스타 EV', '2020 HYUNDAI Porter2':'2020 포터2', '2020 HYUNDAI Tucson':'2020 투싼',
'2020 HYUNDAI Veloster':'2020 벨로스터 N', '2020 KIA Bongo3':'2020 봉고3', '2020 KIA Carnival':'2020 카니발',
'2020 KIA K5':'2020 K5', '2020 kia mohave':'2020 모하비', '2020 KIA Proceed':'2020 프로씨드',
'2020 KIA Ray':'2020 레이', '2020 KIA Sorento':'2020 쏘렌토', '2020 KIA spotage':'2020 스포티지',
'2020 KIA stinger':'2020 스팅어', '2020 KIA Telluride':'2020 텔루라이드', '2020 KIA XCeed':'2020 X씨드',
'2020 RenaultSamsung QM6':'2020 QM6', '2020 RenaultSamsung SM6':'2020 SM6', '2020 RenaultSamsung XM3':'2020 XM3',
'2020 SsangYong Korando':'2020 코란도',  '2020 SsangYong Rexton':'2020 렉스턴 스포츠', '2020 SSANGYONG Rexton_G4':'2020 G4 렉스턴',
'2020 SsanYong Tivoli':'2020 티볼리', '2021 HYUNDAI Genesis G80':'2021 G80', '2021 KIA K3':'2021 K3',
'2021 KIA K9':'2021 K9', '2021 KIA SOUL':'2021 쏘울 부스터'}

car_lists = {'2017 hyundai i30':'2017 i30 N', '2018 daechang danigo':'2018 다니고', '2018 hyundai grand_starex_limuzine':'2018 그랜드 스타렉스 리무진',

 '2018 hyundai lafesta':'2018 라페스타', '2018 hyundai nexo':'2018 넥쏘', '2018 hyundai veloster':'2018 벨로스터',
 '2018 kia ceed_sw':'2018 씨드 SW', '2018 kia niro_ev':'2018 니로 EV', '2019 daechang danago_iii':'2019 다니고 III 픽업',
'2019 hyundai accent':'2019 엑센트', '2019 hyundai genesis_G90':'2019 G90', '2019 hyundai i30':'2019 i30',
'2019 hyundai ioniq':'2019 아이오닉 하이브리드', '2019 hyundai palisade':'2019 팰리세이드', '2019 hyundai santa_fe':'2019 싼타페',
'2019 hyundai solati':'2019 쏠라티', '2020 hyundai sonata':'2020 쏘나타', '2019 hyundai venue': '2019 베뉴',
'2019 kia ceed':'2019 씨드', '2019 kia k7':'2019 K7', '2019 kia morning':'2019 모닝',
'2019 kia niro_hybrid':'2019 니로 하이브리드', '2019 kia rio':'2019 리오 세단', '2019 kia seltos':'2019 셀토스',
'2019 kia stonic':'2019 스토닉', '2020 camsys cevo-c':'2020 캠시스 CEVO-C', '2020 gm damas':'2020 다마스',
'2020 gm labo':'2020 라보', '2020 hyundai aura':'2020 아우라', '2020 hyundai avante':'2020 아반떼',
'2020 hyundai creta ix25':'2020 ix25', '2020 hyundai genesis gv80':'2020 GV80', '2020 hyundai genesis_G70':'2020 G70',
'2020 hyundai grand i10':'2020 i10', '2020 hyundai grand starex':'2020 그랜드 스타렉스', '2020 hyundai grandeur':'2020 그랜저',
'2020 hyundai i20 elite':'2020 i20', '2020 hyundai i30':'2020 i30 왜건', '2020 hyundai kona':'2020 코나',
'2020 hyundai lafesta':'2020 라페스타 EV', '2020 hyundai porter2':'2020 포터2', '2020 hyundai tucson':'2020 투싼',
'2020 hyundai veloster':'2020 벨로스터 N', '2020 kia bongo3':'2020 봉고3', '2020 kia carnival':'2020 카니발',
'2020 kia k5':'2020 K5', '2020 kia mohave':'2020 모하비', '2020 kia proceed':'2020 프로씨드',
'2020 kia ray':'2020 레이', '2020 kia sorento':'2020 쏘렌토', '2020 kia spotage':'2020 스포티지',
'2020 kia stinger':'2020 스팅어', '2020 kia telluride':'2020 텔루라이드', '2020 kia xceed':'2020 X씨드',
'2020 renaultsamsung qm6':'2020 QM6', '2020 renaultsamsung sm6':'2020 SM6', '2020 renaultsamsung xm3':'2020 XM3',
'2020 ssangyong korando':'2020 코란도',  '2020 ssangyong rexton':'2020 렉스턴 스포츠', '2020 ssangyong rexton_g4':'2020 G4 렉스턴',
'2020 ssangyong tivoli':'2020 티볼리', '2021 hyundai genesis G80':'2021 g80', '2021 kia k3':'2021 K3',
'2021 kia k9':'2021 K9', '2021 kia soul':'2021 쏘울 부스터'}