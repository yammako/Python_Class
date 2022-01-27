jumin = "990120-1234567"

# jumin 변수에서 필요한 정보만을 추출하는 것을 슬라이싱이라 함
print("성별 : " + jumin[7])     # 자료의 시작점은 0부터 시작함
print("연 : " + jumin[0:2])     # jumin의 0번째부터 2번째미만까지의 정보를 추출, 즉 0번째와 1번째 정보 추출
print("월 : " + jumin[2:4])     # jumin의 2번째, 3번째 정보를 추출
print("일 : " + jumin[4:6])     # jumin의 4번째, 5번째 정보를 추출
print("생년월일 : " + jumin[:6])    # jumin의 처음부터 6번째 미만까지의 정보 추출
print("뒤 7자리 : " + jumin[7:])    # jumin의 7번째부터 끝까지의 정보 추출
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:])  # jumin의 마지막은 -1이기 때문에 뒤 7자리의 첫번째 정보는 -7의 위치