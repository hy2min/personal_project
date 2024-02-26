# no.1
# no.2
class Member():
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    # no.3
    def display(self):
        print(f"회원 이름 : {self.name}")
        print(f"회원 아이디 :{self.username}")
        pass

    # no.4


class Post():
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        pass


# no.5
member1 = Member("아무개", "anything", "a12345")
member2 = Member("홍길동", "gildonghong", "b4321")
member3 = Member("이철수", "chalsu", "1234567890")

# no.5-a
members = []
members.append(member1)
members.append(member2)
members.append(member3)

for member in members:
    member.display()

# no.6
post1 = Post("맛집1", "떡볶이,순대,간,어묵,튀김 그리고 김밥", member3)
post2 = Post("맛집2", "마라탕,꿔바로우,딸기탕후루,토망고탕후루", member2)
post3 = Post("맛집3", "알리오올리오,까르보나라,새우크림리조또,루꼴라샐러드 그리고 마르게리따피자", member1)
post4 = Post("명소1", "한옥마을,야시장,객리단길", member1)
post5 = Post("명소2", "세포라,런베뮤,롯데월드 그리고 석촌호수", member2)
post6 = Post("명소3", "해운대,감천문화마을,롯데월드,광안리 그리고 책방골목", member3)
post7 = Post("가수1", "박효신 아이유 그리고 NCT127", member2)
post8 = Post("가수2", "소란,10cm,루시,손애플", member1)
post9 = Post("가수3", "르세라핌,아이브,에스파 그리고 있지", member3)

posts = []
posts.append(post1)
posts.append(post2)
posts.append(post3)
posts.append(post4)
posts.append(post5)
posts.append(post6)
posts.append(post7)
posts.append(post8)
posts.append(post9)

# no.6-a
for post in posts:
    if post.author == member1:
        print(post.title)

# no.6-b
for post in posts:
    if '그리고' in post.content:
        print(post.title)

# 추가과제
name = input('이름을 입력하세요 :')
username = input('아이디를 입력하세요 :')
password = input('비밀번호를 입력하세요 :')

input_member = Member(name, username, password)

input_member.display()

title = input('제목을 입력하세요 :')
content = input('내용을 입력하세요 :')
author = input("저자를 입력하세요 :")

input_post = Post(title, content, author)
