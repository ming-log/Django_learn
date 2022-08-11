from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from app1.forms import PersonForm
import datetime
from app1.models import Person

# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def article(request, id):
    content = f"this articles id is {id}"
    return HttpResponse(content)

def article_detail(request, year, month, slug):
    content = f"this year is {year}, this month is {month}, this slug is {slug}"
    return HttpResponse(content)

def year_archive(request, year):
    return HttpResponse(year)

def get_name(request):
    # 判断请求方法是否为POST
    if request.method == 'POST':
        # 将请求数据填充到PersonForm实例中
        form = PersonForm(request.POST)
        # 判断form是否为有效表单
        if form.is_valid():
            # 使用form.cleaned_data获取请求的数据
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            # 响应拼接后的字符串
            return HttpResponse(first_name + ' ' + last_name)
        else:
            return HttpResponseRedirect('/error/')
    # 请求GET方法
    else:
        return render(request, 'name.html', {'form': PersonForm()})

# 定义一个视图方法，必须带有请求对象作为参数
def current_datetime(request):
    now = datetime.datetime.now()  # 获取当前时间
    html = f"It is now {now}"
    return HttpResponse(html)

def person_detail(request, pk):
    try:
        P =  Person.objects.filter(first_name=pk)  # 获取Person数据
    except Person.DoesNotExist:
        raise Http404('Person Does Nont Exist')
    return render(request, 'person_detail.html', {'pk': [p.last_name for p in P]})
