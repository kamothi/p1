from django.db import models
# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=10) # 이름
    address = models.TextField() # 주소
    phone_number = models.CharField(max_length=15) # 번호
    job_position = models.CharField(max_length=10) # 직위
    age = models.IntegerField(max_length=5) # 나이
    dateTimeOfPosting = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["dateTimeOfPosting"]

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField(max_length=2)
    nickname = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

class board(models.Model):
    board_id = models.AutoField(primary_key=True)  # 게시글 id
    title = models.CharField(max_length=50, null=True)  # 제목
    content = models.TextField(null=True)  # 게시글 내용
    update_date = models.DateTimeField(auto_now_add=True, null=True)  # 게시글 올린 시간
    views = models.PositiveIntegerField(max_length=50, null=True)  # 조회수
    comment = models.PositiveIntegerField(max_length=50, null=True)  # 댓글 수
    # comment_id 댓글 id
    userId = models.ForeignKey('Customer', on_delete=models.CASCADE, db_column="userId", null=True)
    liked_users = models.ManyToManyField('Customer', through='Like', related_name='liked_posts')

class Like(models.Model):
    user = models.ForeignKey('Customer', on_delete=models.CASCADE)
    post = models.ForeignKey('board', on_delete=models.CASCADE)
    
class challenge(models.Model):
    challenge_id = models.AutoField(primary_key=True) #챌린지 아이디
    subject = models.CharField(max_length=200) # 챌린지 이름
    content = models.TextField() # 챌린지에 대한 내용
    address = models.URLField() # URL 주소
    update_date = models.DateTimeField(auto_now_add=True) # 생성 날짜
    views = models.PositiveIntegerField(default=0) # 조회수
    rate = models.IntegerField() # 평점
    Bigcategory = models.CharField(max_length=100) # 큰카테고리
    smallcategory = models.CharField(max_length=100, default = '') # 작은 카테고리
    liked_users = models.ManyToManyField('Customer', through='ch_Like', related_name='liked_challenges')

#comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
   #user_id
class ch_Like(models.Model):
    user = models.ForeignKey('Customer', on_delete=models.CASCADE)
    challenge = models.ForeignKey('challenge', on_delete=models.CASCADE)

class Comment(models.Model):
    board = models.ForeignKey('board', on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey('Customer', on_delete=models.CASCADE,related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # def __str__(self):
    #     return self.content
    # 위에 주석 처리한 부분은 리턴시에 객체 자체를 반환하겠다는 의미이다.