# 피클 : 프로그램상에서 사용하는 값을 파일로 저장하는 기능

import pickle
profile_file = open("profile.pickle", "wb")     # wb는 바이너리로 저장 (반드시 바이너리로 저장해야 함)
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)      # profile에 있는 정보를 file에 저장
profile_file.close()

# 저장한 파일 내용 가져오기
profile_file = open("profile.pickle", "rb")     # rb는 바이너리로 읽기 (반드시 바이너리로 저장해야 함)
profile = pickle.load(profile_file)     # 파일에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()