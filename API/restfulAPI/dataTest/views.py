from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Users,Customer,board
from .serializer import userSerializer,signSerializer,boardSerializer,writeSerializer
import bcrypt
from rest_framework_jwt.utils import jwt_decode_handler, jwt_get_username_from_payload_handler
from rest_framework.response import Response
from .createjwt import generate_jwt_token
import jwt
from django.conf import settings
from .models import challenge
from .serializer import userSerializer
from .serializer import challengeSerializer
from .serializer import mainchallengeSerializer
from .serializer import smallchallengeSerializer
from .serializer import contentchallengeSerializer
from .serializer import updatechallengeSerializer
from .serializer import rankchallengeSerializer

@csrf_exempt
def user_list(request):
    if request.method == 'GET': # GET 방식일 때
        query_set = Users.objects.all() # ORM으로 Users의 모든 객체 받아옴
        serializer = userSerializer(query_set, many=True) # JSON으로 변환
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False}) # JSON타입의 데이터로 응답
    elif request.method == 'POST':  # POST방식일 때
        data = JSONParser().parse(request)  # 요청들어온 데이터를 JSON 타입으로 파싱
        serializer = userSerializer(data=data)  # Serializer를 사용해 전송받은 데이터를 변환하기 위함
        if serializer.is_valid():  # 생성한 모델과 일치하면
            serializer.save()  # 데이터 저장
            return JsonResponse(serializer.data, status=201, json_dumps_params={'ensure_ascii': False})  # 정상 응답 201
        return JsonResponse(serializer.errors, status=400, json_dumps_params={'ensure_ascii': False})  # 모델에 일치하지 않는 데이터일 경우
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        nickname= data['nickname']
        password= data['password']
        try:
            if not Customer.objects.filter(nickname=data['nickname']).exists():
                return JsonResponse(data, status=400, json_dumps_params={'ensure_ascii': False})
            else:
                customer = Customer.objects.filter(nickname=data['nickname'])
                serializer = signSerializer(customer, many=True)
                hashed_password = serializer.data[0]['password']
                if bcrypt.checkpw(data['password'].encode('utf-8'), hashed_password.encode('utf-8')):
                    token = generate_jwt_token(serializer.data[0]['id'])
                    return JsonResponse({'message': 'SUCCESS', 'access_token': token.decode('utf-8')}, status=200)
                else:
                    return JsonResponse(data, status=400, json_dumps_params={'ensure_ascii': False})
        except:
            DATA = {
                "results": {
                    "msg": "유저 정보가 올바르지 않습니다.",
                    "code": "E4010"
                }

            }
            return JsonResponse(data=DATA, status=400,json_dumps_params={'ensure_ascii': False})



@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            if Customer.objects.filter(nickname=data['nickname']).exists():
                return JsonResponse(data, status=400, json_dumps_params={'ensure_ascii': False})
            byted_password = data['password'].encode('utf-8')
            hashed_password = bcrypt.hashpw(byted_password, bcrypt.gensalt())
            password = hashed_password.decode('utf-8')
            Customer.objects.create(age=data['age'],nickname=data['nickname'],password=password).save()
            return JsonResponse(data,safe=False, status=200, json_dumps_params={'ensure_ascii': False})
        except KeyError:
            return JsonResponse({"message": "INVALID_KEY"}, status=400)

@csrf_exempt
# @permission_classes([IsAuthenticated])
def check_login(request):
    if request.method == 'GET':
        token = request.headers['tokenkey']
        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        id = decoded.get('user_id')
        cus = list(Customer.objects.filter(id=id).values())
        return JsonResponse(cus[0],safe=False, json_dumps_params={'ensure_ascii': False})

@csrf_exempt
def board_list(request):
    if request.method == 'GET':  # GET 방식일 때
        query_set = board.objects.all()  # ORM으로 board의 모든 객체 받아옴
        serializer = boardSerializer(query_set, many=True)  # JSON으로 변환
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})  # JSON타입의 데이터로 응답

    elif request.method == 'POST':  # POST방식일 때
        data = JSONParser().parse(request)  # 요청들어온 데이터를 JSON 타입으로 파싱
        serializer = writeSerializer(data=data)  # Serializer를 사용해 전송받은 데이터를 변환하기 위함

        if serializer.is_valid():  # 생성한 모델과 일치하면
            serializer.save()  # 데이터 저장
            return JsonResponse(data, status=201, json_dumps_params={'ensure_ascii': False})  # 정상 응답 201
        # Board = board(title=data['title'], content=data['content'], user_id=data['userId'])
        # Board.save()

        return JsonResponse(serializer.errors, status=400)  # 모델에 일치하지 않는 데이터일 경우
        

def challenge_list(request):
    if request.method == 'GET':  # GET 방식일 때
        query_set = challenge.objects.all()  # ORM으로 Users의 모든 객체 받아옴
        serializer = challengeSerializer(query_set, many=True)  # JSON으로 변환
        return JsonResponse(serializer.data, safe=False)  # JSON타입의 데이터로 응답

    elif request.method == 'POST': # POST방식일 때
        data = JSONParser().parse(request) # 요청들어온 데이터를 JSON 타입으로 파싱
        serializer = challengeSerializer(data=data) # Serializer를 사용해 전송받은 데이터를 변환하기 위함
        if serializer.is_valid(): # 생성한 모델과 일치하면
            serializer.save() # 데이터 저장
            return JsonResponse(serializer.data, status=201) # 정상 응답 201
        return JsonResponse(serializer.errors, status=400) # 모델에 일치하지 않는 데이터일 경우

def challenge_home(request):
    if request.method == 'GET':  # GET 방식일 때
        query_set = challenge.objects.all()  # ORM으로 Users의 모든 객체 받아옴
        serializer = mainchallengeSerializer(query_set, many=True)  # JSON으로 변환
        return JsonResponse(serializer.data, safe=False)  # JSON타입의 데이터로 응답

def challenge_smallcategory(request):
    if request.method == 'GET':  # GET 방식일 때
        query_set = challenge.objects.all()  # ORM으로 Users의 모든 객체 받아옴
        serializer = smallchallengeSerializer(query_set, many=True)  # JSON으로 변환
        return JsonResponse(serializer.data, safe=False)  # JSON타입의 데이터로 응답

def challenge_content(request,pk):
    object = challenge.objects.get(pk=pk)
    if request.method == "GET":
        serializer = contentchallengeSerializer(object)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT': # POST방식일 때
        update_data = JSONParser().parse(request) # 요청들어온 데이터를 JSON 타입으로 파싱
        serializer = updatechallengeSerializer(data=update_data) # Serializer를 사용해 전송받은 데이터를 변환하기 위함
        if serializer.is_valid(): # 생성한 모델과 일치하면
            serializer.save() # 데이터 저장
            return JsonResponse(serializer.data, status=201) # 정상 응답 201
        return JsonResponse(serializer.errors, status=400) # 모델에 일치하지 않는 데이터일 경우

def challenge_rank(request):
    if request.method == 'GET':  # GET 방식일 때
        query_set = challenge.objects.all()  # ORM으로 Users의 모든 객체 받아옴
        serializer = rankchallengeSerializer(query_set, many=True)  # JSON으로 변환
        return JsonResponse(serializer.data, safe=False)  # JSON타입의 데이터로 응답
