from rest_framework import serializers
from .models import Users,Customer
from .models import board
from .models import challenge, Comment

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["name","phone_number","job_position","age"]

class signSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class boardSerializer(serializers.ModelSerializer):
    class Meta:
        model = board
        fields = ["title", "content", "comment", "update_date","board_id"]
# 제목/ 게시글 내용/ 댓글 수/ 좋아요 수/ 게시글 올린 시간  // 익명은 프론트에서

class writeSerializer(serializers.ModelSerializer):
    class Meta:
        model = board
        fields = ["title", "content", "views","comment","userId"]
 
class challengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = challenge
        fields = "__all__"

class mainchallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = challenge
        fields = ["subject", "Bigcategory", "smallcategory", "challenge_id"]

class smallchallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = challenge
        fields = ["challenge_id", "subject", "rate", "views", "smallcategory"]

class contentchallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = challenge
        fields = ["subject", "content", "address", "challenge_id", "views"]

class updatechallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = challenge
        fields = ["rate"]

class rankchallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = challenge
        fields = ["subject", "like"]

class updateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["board","user","content"]

class showCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["user","content"]