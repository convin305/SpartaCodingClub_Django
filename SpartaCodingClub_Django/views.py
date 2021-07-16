from django.http import HttpResponse
# HttpResponse는 괄호 안의 내용을 전달

from django.shortcuts import render
# render는 html을 보여주는 역할

# 함수를 만들었으면, ulrs로 가서 url과 연결을 시켜야 함
def base_response(request):
    return HttpResponse("안녕하세요! 장고의 시작입니다!")

# first_view 함수는 my_test.html을 보여주는 함수
def first_view(request):
    return render(request,'my_test.html')