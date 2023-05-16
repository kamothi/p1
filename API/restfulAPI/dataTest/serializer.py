from rest_framework import serializers
from .models import Users,Customer
from .models import board
from .models import challenge

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
        fields = ["title", "content", "comment", "update_date"]
# 제목/ 게시글 내용/ 댓글 수/ 좋아요 수/ 게시글 올린 시간  // 익명은 프론트에서

class writeSerializer(serializers.ModelSerializer):
    class Meta:
        model = board
        fields = ["title", "content", "userId"]
 
class challengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = challenge
        fields = "__all__"

class mainchallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = challenge
        fields = ["subject", "Bigcategory", "smallcategory"]

class smallchallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = challenge
        fields = ["subject", "like", "dislike", "rate", "views"]

class contentchallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = challenge
        fields = ["subject", "content", "address","challenge_id","views"]

class updatechallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = challenge
        fields = ["rate", "like", "dislike","views"]

class rankchallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = challenge
        fields = ["subject", "like"]
