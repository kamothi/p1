from rest_framework import serializers
from .models import Users,Customer
from .models import board

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