from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
import random

nextId = 4
topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ..'},
    {'id':2, 'title':'view', 'body':'View is ..'},
    {'id':3, 'title':'model', 'body':'Model is ..'}
]

def HTMLTemplate(articleTag, id=None):
    global topics
    contextUI = ''  # UI가 만들어 지는지 확인
    if id != None:
        contextUI = f'''
                <li>
                    <form action="/delete/" method="post">
                        <input type="hidden" name="id" value={id}>
                        <input type="submit" value="delete">
                    </form>
                </li>
                <li>
                    <a href="/update/{id}">update</a>
                </li>
            '''
    ol = ''

    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'

    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ul>
            {ol}
        </ul>
        {articleTag}
        <ul>
            <li><a href="/create/">create</a></li>
            {contextUI}
        </ul>
    </body>
    </html>
    '''

# 클라이언트로 정보를 전송하기 위한 역할을 할 함수
def index(request):  # 요청과 관련된 여러 정보를 매개 변수로 전달 받음
    article = '''
        <h2>Welcome</h2>
        Hello, Django!
    '''
    # return HttpResponse('<h1>Random!</h1>' + str(random.random()))  # 페이지를 불러올 때마다 동적으로 반응
    return HttpResponse(HTMLTemplate(article))

def read(request, id):
    global topics
    article = ''

    for topic in topics:
        if str(topic["id"]) == id:
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article, id))

@csrf_exempt
def create(request):
    global nextId
    print('request.method', request.method)

    if request.method == 'GET':
        article = '''
            <form action="/create/" method="post">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id":nextId, "title":title, "body":body}
        topics.append(newTopic)
        url = '/read/' + str(nextId)
        nextId = nextId + 1
        # return HttpResponse(request.POST['title'])
        # return HttpResponse(HTMLTemplate('의미없는 정보'))
        return redirect(url)  # 어떤 주소로 이동할 것인가

@csrf_exempt
def update(request, id):
    global topics
    if request.method == 'GET':
        for topic in topics:
            if topic['id'] == int(id):
                selectTopic = {"title":topic['title'], "body":topic['body']}
        article = f'''
            <form action="/update/{id}/" method="post">
                <p><input type="text" name="title" placeholder="title" value={selectTopic['title']}></p>
                <p><textarea name="body" placeholder="body">{selectTopic['body']}</textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article, id))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        for topic in topics:
            if topic['id'] == int(id):  # 기존 글과 일치 한다면
                topic['title'] = title
                topic['body'] = body
        return redirect(f'/read/{id}')

@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST':
        id = request.POST['id']
        newTopics = []
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics
        return redirect('/')
