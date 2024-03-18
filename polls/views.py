from django.http import HttpResponse


# Create your views here.
def index(request):
    # 从request里面接受一个参数name，并且在response里面输出
    name = request.GET.get('name', 'world')
    return HttpResponse(f'Hello, {name}. You are at the polls index.')
