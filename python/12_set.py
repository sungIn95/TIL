set_a = {1,2,3,1,1}
set_b = {"hi",1,2}

# 내부적으로 "표현"만 똑깉이 하는 방법이 있을 뿐
# 순서가 없어요!!!
print(set_a) # {1 ,2 ,3}
print(set_b) # {'hi', 2, 1}

# 활용 예시
locations = ["서울", "서울","대전","대구","제주","부산","부산","서울","광주","서울",]
print(set(locations))
# 4
set(locations)
# {'서울', '광주', '부산', '대구', '제주', '대전'}