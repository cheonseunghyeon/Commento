from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from .models import MainContent
def index(request):

 # - 이 붙었으니 역순으로 정렬
 content_list = MainContent.objects.order_by('-pub_date')
 context = {'content_list': content_list}
 # render 함수는 mysite/content_list.html 파일에 content_list 데이터를 적용
 return render(request, 'mysite/content_list.html', context)

def detail(request, content_id):
 content_list = MainContent.objects.get(id=content_id)
 context = { 'content_list': content_list}
 return render(request, 'mysite/content_detail.html', context)