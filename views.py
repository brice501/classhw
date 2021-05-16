from django.shortcuts import render

def start(request):
    return render(request, 'myapp/start.html')


def second(request):
    result_team = request.GET['teamname']
    ctx = {}
    if result_team == '1':
        ctx = {
            'result': '이 팀이 1팀이네',
        }
    elif int(result_team) in [2, 3, 4, 5]:
        ctx = {
            'result': '저희가 많이 보죠',
        }
    return render(request, 'myapp/second.html', ctx)
