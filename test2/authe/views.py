#coding=utf-8
from django.shortcuts import render, render_to_response,RequestContext
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
import django.contrib.auth.hashers as hashers
import json
import models
import re
import time
import datetime

from .models import questions
from .models import QUser as User
from .models import Answer


jzxx = ['a','b','c','d','e','f','g','h','i','g','k','l','m','n']

# Create your views here.
def index(request):
    username1 = request.COOKIES.get("username")
    if username1 is None:
        username1 = 0
    return render_to_response('index2.html', {'username': username1},context_instance=RequestContext(request))

def contact(request):
    content = {}
    username = request.COOKIES.get("username")
    if 'member' in request.session:
        user = request.session['member']
        print user
        content = {'username': user}
    content = {"username":username}
    
    return render_to_response('contact2.html', content, context_instance=RequestContext(request))

def signin(request):
    state = None

    try:
        if request.method == "POST":
            usern = request.POST.get('User', '')
            password = request.POST.get('Password', '')
            auth_pw = User.objects.get(username=usern).password
            print auth_pw
            print usern
            print password
            user = User.objects.filter(username=usern, password=password)
            print user
            if hashers.check_password(password, auth_pw):
                print True
                if user is not None:
                    print "auth_sucess"
                    content = {"state": "success", "username": usern}
                    response = render_to_response('index2.html', content, context_instance=RequestContext(request))
                    try:
                        response.set_cookie('username', usern, 15000000)
                        print "session key add"
                    except:
                        print "no session key add"
                    return response
            elif auth_pw == "":
                state = "not_exist"
            else:
                state = "password_error"
        '''
        elif request.COOKIES.get("username") != "":
            return HttpResponseRedirect(reverse('index'))
        '''

    except:
        if request.COOKIES.get("username") != "":
            return HttpResponseRedirect(reverse('index'))
    content = {'state': state, "username": None}
    return render_to_response('signin.html', content, context_instance=RequestContext(request))
    """使用context_instance可以把session里面的自定义标签拿出来，可以把username显示在页面上面，证明保持登陆"""

def signup(request):
    state = None
    try:
        if request.method == "POST":
            print request
            print request.POST.get('Email', '')
            print request.POST.get('Password', '')
            print request.POST.get('User', '')
            user = request.POST.get('User', '')
            email = request.POST.get('Email', '')
            password = request.POST.get('Password', '')
            repeat_password = request.POST.get('Repeat_Password', '')
            """
                使用request.POST.get获取表单中的用户名、密码、email
            """
            if password != repeat_password:
                return render(request, 'signup.html', {"password":1})
            else:
                if User.objects.filter(username=user):
                    return render(request, 'signup.html', {"user":1})
                else:
                    print "in_process"
                    encrypt_password = hashers.make_password(password)
                    print encrypt_password
                    new_user = User.objects.get_or_create(username=user, password=encrypt_password, email=email)
                    state = "success"
                    """
                        django已经内置了多种的加密模块方式，采取了PDK2+sha256的对密码进行加密（没有采用bcrypt+sha256）
                    """
                    print state
                    return render(request, 'signup.html', {"state1":1})
        '''
        elif request.COOKIES.get("username") != "":
            return HttpResponseRedirect(reverse('index'))
        '''
    except:
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('index'))

    contents = {'state': state}
    return render_to_response('signup.html', {'state': state})

'''
def create(request):
    if request.method == "POST":
        question = request.POST
        question_name = question['qname']
        print question
        print question.get("1"+"_"+"0", "")
        tid = "id"
        t_id = 1
        x_id = 0
        info = ""
        jznum = 0
        optionarr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t","u", "v", "w", "x", "y", "z"]
        num_list = range(0, 26)
        Flag = True
        """上面的FLAG是用来继续进行矩阵题选项的添加的判断，当request.post.get拿到“”的时候，flag会变成false，然后矩阵题就能把剩下的
        的小题目全部搞进去。
        """
        while 1:
            if question.get(str(t_id)+"_"+str(x_id), ""):
                Flag = True
                if question.get(str(t_id)+"_"+"1", "") != "填空":
                    info += (tid+str(t_id)+"_"+str(x_id))+":"+question.get(str(t_id)+"_"+str(x_id), "")+"||"
                    x_id += 1
                    print str(t_id)+str(x_id)
                else:
                    for i in range(2):
                        info += (tid + str(t_id) + "_" + str(i)) + ":" + question.get(str(t_id) + "_" + str(i), "") + "||"
                    t_id += 1
                    x_id = 0

            elif question.get(str(t_id)+"_" + str(x_id) + optionarr[jznum], "") != "":
                    print "inloop"
                    info += (tid+str(t_id)+"_"+str(x_id))+optionarr[jznum]+":"+question.get(str(t_id)+"_"+str(x_id)+optionarr[jznum], "")+"||"
                    print info
                    jznum += 1

            else:
                if Flag:
                    if question.get(str(t_id) + "_" + str(x_id) + optionarr[jznum], "") == "":
                        print "ready input small question"
                        x_id += 1
                        print str(t_id) + "_" + str(x_id)
                        Flag = False
                        print Flag
                elif question.get(str(t_id)+"_"+"0", "") == "":
                    break
                else:
                    t_id += 1
                    x_id = 0
                    jznum = 0


        """
            只能使用request.POST.get才能把用户post上来的问卷全部用中文入库，如果直接使用列表入库，是只能显示unicode字符（这个坑了自己3天）
            前端题目id的逻辑为 x.0为题目  x.1为题型   x.2（如果是矩阵题）就是变成 x.2.(a-z)为选项   否则从 x.2开始都是题目的选项
        """


        print info

        qa = models.questions(q_name=question_name, question=info)
        qa.save()
        username1 = request.session['member']

        username1 = str(username1)
        username2 = auth.models.User.objects.get(username=username1)
        print username1+"||"
        print username2
        id = qa.id
        print qa
        print id
        u = user.objects.create(user=username2, qid=qa)
        print u

        try:
            u.save()
            print "nothing"
        except:
            print "user表入库失败"
        return render_to_response("createsuccess.html", context_instance=RequestContext(request))

    return render_to_response("createquestion.html", context_instance=RequestContext(request))
'''

def tiqu(request):
    username = request.COOKIES.get("username")
    """
    question_name = []
    for item in question:
        if item.q_name not in question_name:
            print item.q_name
            question_name.append(item.q_name)
    """
    if request.method == "POST":
        name = request.POST.get("search", "")
        type = request.POST.get("type", "")
        if type == "usern":
            question = questions.objects.filter(user=name)
        elif type == "qnn":
            question = questions.objects.filter(q_name=name)
        print "question={}".format(question)


    else:
        question = questions.objects.all().exclude(question="")
        print question



    page_num = request.GET.get('page')
    paginator = Paginator(question, 6)
    try:
        question = paginator.page(page_num)
    except PageNotAnInteger:
        question = paginator.page(1)
    except EmptyPage:
        question = paginator.page(paginator.num_pages)
    """
                上面使用django自带的分页功能来实现对单页显示问卷数量的控制
    """
    content = {"questions": question, "username":username}
    print content



    return render_to_response('tiqu2.html', content, context_instance=RequestContext(request))

def get_ques(qid):
    
    question = questions.objects.filter(id=qid)[0]
    timu = question.question

    timu_dict = {}
    t_id = 1
    x_id = 0
    dict_sort = []
    new_dict = {}

    timus = timu.split("||")
    timus.pop()
    print "timus",timus
    print type(timus)

    for item in timus:
        print item
        if item != "":
        	r = item.split(":")
        	timu_dict[str(r[0])] = r[1]
        # if "id"+str(t_id) in item:
        #     r = item.split(":")
        #     timu_dict[str(r[0])] = r[1]

        # elif str(t_id+1) in item:
        #     r = item.split(":")
        #     timu_dict[str(r[0])] = r[1]
        #     t_id += 1
        # else:
        #     t_id += 1
        """
            因为这里会出现2.0 id还是等于1的情况，所以需要用多一个elif来进行判断，否则x.0这个html标签的东西就会消失
        """

    timu_dict = sorted(timu_dict.items())

    print "timu_dict:",timu_dict

    """
        排序后返回的是一个大列表，列表里面包含的是元祖而不是字典
    """

    for i in timu_dict:
        new_dict[i[0]] = i[1]

    print new_dict

    new_dict = json.dumps(new_dict)
    print new_dict
    content = {"timu": new_dict}
    return content

def xuanranwj(request):
    qid = request.GET['id']
    username = request.COOKIES.get("username")
    content = get_ques(qid)
    content['id'] = qid
    content['username'] = username
    return render_to_response('xuanran.html', content)

def logout(request):
    response = HttpResponseRedirect(reverse('index'))
    #清除cookie里保存的username
    response.delete_cookie('username')
    return response

def houtai(request):
    username1 = request.COOKIES.get("username")
    print username1
    content= {'username': username1}
    return render_to_response("houtai.html",content, context_instance=RequestContext(request))

def jieshou(request):
    if request.method == "POST":
        res = request.POST
        qid = request.GET['id']
        user = request.COOKIES.get("username")
        content= {"username": user}
        res1 = ""
        username = request.COOKIES.get("username")
        print username

        if username == None:
            username = "匿名"

        answer_info = questions.objects.get(id=qid).result
        qname = questions.objects.get(id=qid).q_name

        content = {}

        print answer_info,"1"*20
        print "res=%s"%(res)
        if answer_info != "":
            for r in res:
                if "_" in r:
                    rr = r[0:-1] + str(int(r[-1]) - 2)
                    abc = res.getlist(r)[0]
                    print "%s:%s\$.*?&" % (rr, abc.lower())
                    thdata = re.findall("%s:%s\$.*?&" % (rr, abc.lower()), answer_info)[0]
                    num = int(re.findall("\$(.*?)&", thdata)[0])+1
                    answer_info = answer_info.replace(thdata, "%s:%s$%s&"%(rr, abc.lower(), num))
                else:
                    abc = res.getlist(r)
                    for ab in abc:
                        ab = ab.lower()
                        if ab in jzxx:
                            print answer_info,"ds"*10
                            thdata = re.findall("%s:%s\$.*?&" % (r, ab), answer_info)[0]
                            num = int(re.findall("\$(.*?)&", thdata)[0])+1
                            answer_info = answer_info.replace(thdata, "%s:%s$%s&" % (r, ab, num))
            questions.objects.filter(id=qid).update(result=answer_info)

            for a in answer_info.split("||"):
                if len(a):
                    th = re.findall('(\w+):', a)[0]
                    abc = re.findall('\$(\d+)&', a)
                    abc = [int(i) for i in abc]
                    print sum(abc)
                    for i in range(len(abc)):
                        content[th + jzxx[i]] = abc[i]
        
        date = time.strftime('%Y-%m-%d', time.localtime(time.time()))

        tid = 1
        xid = 3

        flag0 = True

        while flag0:
            if res.get(str(tid), ""):
                print "except jz"
                a = res.get(str(tid), "")
                res1 += str(tid) + "&" + a + "||"
                tid += 1
            elif res.get(str(tid)+"_"+str(xid), ""):
                print "jz in"
                a = res.get(str(tid)+"_"+str(xid), "")
                res1 += str(tid) + "_" + str(xid) + "&" + a + "||"
                xid += 1
            elif not(res.get(str(tid)+"_"+str(xid), "")) and res.get(str(tid)+"_"+str(xid-1), ""):
                xid = 3
                tid += 1
            else:
                flag0 = False


        Answer.objects.create(qid=qid, answer=res1, user=username, date=date)

    return render_to_response("txcg.html", context_instance=RequestContext(request))

def create_houtai(request):
    if request.method == "POST":
        question = request.POST
        question_name = question['qname']
        print question
        print question.get("1"+"_"+"0", "")
        tid = "id"
        t_id = 1
        x_id = 0
        info = ""
        anw_info = ""
        jznum = 0
        optionarr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t","u", "v", "w", "x", "y", "z"]
        num_list = range(0, 26)
        Flag = True
        """上面的FLAG是用来继续进行矩阵题选项的添加的判断，当request.post.get拿到“”的时候，flag会变成false，然后矩阵题就能把剩下的
        的小题目全部搞进去。
        """
        while 1:
            if question.get(str(t_id)+"_"+str(x_id), ""):
                Flag = True
                if question.get(str(t_id)+"_"+"1", "") != "填空":
                    info += (tid+str(t_id)+"_"+str(x_id))+":"+question.get(str(t_id)+"_"+str(x_id), "")+"||"
                    x_id += 1
                    print str(t_id)+str(x_id)
                else:
                    for i in range(2):
                        info += (tid + str(t_id) + "_" + str(i)) + ":" + question.get(str(t_id) + "_" + str(i), "") + "||"
                    t_id += 1
                    x_id = 0

            elif question.get(str(t_id)+"_" + str(x_id) + optionarr[jznum], "") != "":
                    print "inloop"
                    info += (tid+str(t_id)+"_"+str(x_id))+optionarr[jznum]+":"+question.get(str(t_id)+"_"+str(x_id)+optionarr[jznum], "")+"||"
                    print info
                    jznum += 1

            else:
                if Flag:
                    if question.get(str(t_id) + "_" + str(x_id) + optionarr[jznum], "") == "":
                        print "ready input small question"
                        x_id += 1
                        print str(t_id) + "_" + str(x_id)
                        Flag = False
                        print Flag
                elif question.get(str(t_id)+"_"+"0", "") == "":
                    break
                else:

                    if jznum:
                        for i in range(x_id-4):
                            for j in range(jznum):
                                anw_info += "id%s_%s:%s$0&" % (t_id, i+1,optionarr[j])
                            anw_info += "||"
                    else:
                        for i in range(x_id-3):
                            anw_info += "id%s:%s$0&" % (t_id, optionarr[i])
                        anw_info += "||"

                    t_id += 1
                    x_id = 0
                    jznum = 0

        print anw_info
        """
            只能使用request.POST.get才能把用户post上来的问卷全部用中文入库，如果直接使用列表入库，是只能显示unicode字符（这个坑了自己3天）
            前端题目id的逻辑为 x.0为题目  x.1为题型   x.2（如果是矩阵题）就是变成 x.2.(a-z)为选项   否则从 x.2开始都是题目的选项
        """

        print info
        
        username1 = request.COOKIES.get("username")
        date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        print date

        if info != "":
            qa = models.questions.objects.get_or_create(q_name=question_name, question=info, user=username1, result=anw_info, date=date)
        print username1+"||"

        return render_to_response("houtaisuccess.html", context_instance=RequestContext(request))

    username1 = request.COOKIES.get("username")
    print username1
    content = {'username': username1}
    return render_to_response("cjwj.html", content, context_instance=RequestContext(request))

def editor(request):
    qid = request.GET['id']
    content = get_ques(qid)
    # action = request.POST.get("action", "")
    '''
    xs = request.POST.get("xs", "")
    tg = request.POST.get("tg", "")
    tx = request.POST.get("tx", "")
    '''
    # print action
    content["id"] = qid
    username = request.COOKIES.get("username")
    content["username"] = username
    return render_to_response('change2.html', content)





select = {"danx":"单选", "duox":"多选", "tk":"填空", "jz":"矩阵"}


def teditor(request):
    action = request.POST.get("action", "")
    username = request.COOKIES.get("username")
    wenjuan_id = request.POST.get("qid", "")
    wenjuan_id = int(wenjuan_id)
    print wenjuan_id
    print username

    que = questions.objects.get(id=wenjuan_id).question
    res = questions.objects.get(id=wenjuan_id).result

    print "@" * 10
    if action == "修改":
        tg = request.POST.get("tg", "")
        xs = request.POST.get("xs", "")
        sel = request.POST.get("sel", "")

        print sel * 10
        xs = xs.split("\n")
        th = re.findall("(\d+)\.", tg)[0]

        '''根据id删除题目'''
        deldata = re.findall("id%s.*?\|\|" % th, que)
        for dd in deldata:
            que = que.replace(dd, '')

        que += "id%s_0:%s||" % (th, tg.replace("%s." % th, ""))
        que += "id%s_1:%s||" % (th, select[sel])
        jznum = 0
        xtnum = 0
        if sel == "jz":
            xx = re.findall("\S+", xs[0])
            jznum = len(xx)

            for x in xx:
                que += "id%s_2%s:%s||" % (th, jzxx[xx.index(x)], x)
            for x in xs[1:]:
                if len(x):
                    que += "id%s_%s:%s||" % (th, xs.index(x) + 2, x)
                    xtnum = xs.index(x)
        else:
            for x in xs:
                if len(x):
                    que += "id%s_%s:%s||" % (th, xs.index(x) + 2, x)
                    xtnum = xs.index(x) + 1

        lres = res.split("||")
        for l in lres:
            if len(l):
                if th == int(re.findall("\d+", l)[0]):
                    res.replace(l + "||", "")

        print jznum, "j" * 20
        print xtnum, "x" * 20
        if jznum:
            for i in range(xtnum):
                for j in range(jznum):
                    res += "id%s_%s:%s$0&" % (th, i + 1, jzxx[j])
                    res += "||"
        elif xtnum:
            for i in range(xtnum):
                res += "id%s:%s$0&" % (th, jzxx[i])
                res += "||"

        '''更新数据库'''
        questions.objects.filter(id=wenjuan_id).update(question=que)
        questions.objects.filter(id=wenjuan_id).update(result=res)



    elif action == "插入":
        xs = request.POST.get("xs", "")
        sel = request.POST.get("sel", "")
        tg = request.POST.get("tg", "")
        th = request.POST.get("th", "")
        xs = xs.split("\n")

        print action * 10
        '''更新后面的题号'''

        ii = int(th)
        i = ii
        tnum = 0
        while "id%s" % i in que:
            tnum = i
            i = i + 1

        for j in range(tnum):
            if (tnum - j) < ii:
                break
            # print "id%s_"%(tnum - j)
            if "id%s_" % (tnum - j) in res:
                res = res.replace("id%s_" % (tnum - j), "id%s_" % (tnum - j + 1))
            else:
                res = res.replace("id%s:" % (tnum - j), "id%s:" % (tnum - j + 1))
            que = que.replace("id%s_" % (tnum - j), "id%s_" % (tnum - j + 1))

        print select[sel].decode("utf-8") * 10

        que += "id%s_0:%s||" % (th, tg)
        que += "id%s_1:%s||" % (th, select[sel])

        jznum = 0
        xtnum = 0
        if sel == "jz":
            xx = re.findall("\S+", xs[0])
            jznum = len(xx)

            for x in xx:
                que += "id%s_2%s:%s||" % (th, jzxx[xx.index(x)], x)
            for x in xs[1:]:
                if len(x):
                    que += "id%s_%s:%s||" % (th, xs.index(x) + 2, x)
                    xtnum = xs.index(x)
        else:
            for x in xs:
                if len(x):
                    que += "id%s_%s:%s||" % (th, xs.index(x) + 2, x)
                    xtnum = xs.index(x) + 1

        lres = res.split("||")
        for l in lres:
            if len(l):
                if th == int(re.findall("\d+", l)[0]):
                    res = res.replace(l + "||", "")

        print jznum, "j" * 20
        print xtnum, "x" * 20
        if jznum:
            for i in range(xtnum):
                for j in range(jznum):
                    res += "id%s_%s:%s$0&" % (th, i + 1, jzxx[j])
                    res += "||"
        elif xtnum:
            for i in range(xtnum):
                res += "id%s:%s$0&" % (th, jzxx[i])
                res += "||"
        # '''更新数据库'''
        questions.objects.filter(id=wenjuan_id).update(question=que)
        questions.objects.filter(id=wenjuan_id).update(result=res)




    else:
        tg = request.POST.get("tg", "")
        th = re.findall("(\d+)\.", tg)[0]
        i = int(th)

        deldata = re.findall("id%s.*?\|\|" % th, que)
        for dd in deldata:
            que = que.replace(dd, '')

        lres = res.split("||")
        print lres
        for l in lres:
            if len(l):
                if th == (re.findall("\d+", l)[0]):
                    res = res.replace(l + "||", "")

        print que
        i = i + 1
        while "id%s" % i in que:
            print i
            que = que.replace("id%s_" % (i), "id%s_" % (i - 1))
            if "id%s_" % (i) in res:
                res = res.replace("id%s_" % (i), "id%s_" % (i - 1))
            else:
                res = res.replace("id%s:" % (i), "id%s:" % (i - 1))
            i = i + 1
        print que
        print res
        questions.objects.filter(id=wenjuan_id).update(question=que)
        questions.objects.filter(id=wenjuan_id).update(result=res)

    return render_to_response("change2.html")


def myques(request):
    username1 = request.COOKIES.get("username")
    print username1
    qa = questions.objects.filter(user=username1).exclude(question="")
    print qa
    print type(qa)
    """
        下面使用django自带的分页功能来实现对单页显示问卷数量的控制，跟提取问卷那里相同的处理方法
    """
    page_num = request.GET.get('page')
    paginator = Paginator(qa, 5)
    try:
        qa = paginator.page(page_num)
    except PageNotAnInteger:
        qa = paginator.page(1)
    except EmptyPage:
        qa = paginator.page(paginator.num_pages)

    content = {'username': username1, 'question': qa}
    return render_to_response('myques.html', content, context_instance=RequestContext(request))

def deleteque(request):
    qname = request.GET['qname']
    print qname
    username1 = request.COOKIES.get("username")
    print username1
    questions.objects.filter(q_name=qname, user=username1).delete()
    return HttpResponseRedirect(reverse('myques'))


def genggaipw(request):
    username = request.COOKIES.get("username")
    print username
    content = {"username": username, "status": None}
    if request.method == "POST":
        old_password = request.POST.get("Oldpassword", "")
        new_password = request.POST.get("Newpassword", "")
        new_password2 = request.POST.get("Newpassword2", "")
        """
        获取旧密码，新密码，新密码的重复
        """
        print old_password
        print new_password
        print new_password2
        auth_pw = User.objects.get(username=username).password

        if hashers.check_password(old_password, auth_pw):
            user = User.objects.filter(username=username)
            print user
            print "in_define"
            if new_password == new_password2:
                encrypt_new_password = hashers.make_password(new_password)
                print encrypt_new_password
                user = user = User.objects.filter(username=username).update(password=encrypt_new_password)
                content["status"] = 'pw_change'
                """
                django已经内置了多种的加密模块方式，采取了PDK2+sha256的对密码进行加密（没有采用bcrypt+sha256）
                """
            else:
                content["status"] = 'pw_repeat_error'
        else:
            content["status"] = 'oldpw_error'

    return render_to_response('genggaipw.html', content)


def optiontime(arr, dict1, num1):
    tt_dict = {}
    for a in arr:
        tt_dict[a] = [0 for i in num1]
    key = [i for i in dict1]
    for i in arr:
        for j,it in enumerate(num1):

            if it+':'+i in key:
                if dict1[it+':'+i]:
                    tt_dict[i][j] += int(dict1[it+':'+i])

    for k in tt_dict:
        strl = []
        for num in tt_dict[k]:
            strl.append(str(num))
        tt_dict[k] = strl

    return tt_dict


def Tongji(request):
    qid = request.GET.get("id")
    user = request.COOKIES.get("username")
    result = questions.objects.get(user=user, id=qid).result
    qname = questions.objects.get(user=user, id=qid).q_name
    result = result.split("||")
    re_dict = {}
    for i in result:
        k = i.split("&")
        k = k[0:-1]
        for item in k:
            item = item.split("$")
            re_dict[item[0]] = item[1]
    "re_dict的作用是把每道题的每个选项和选择的次数以字典方式存进去"
    print "re_dict:", re_dict
    num_set = set()
    optionset = set()
    num_list = []
    option_list = []
    '''num_set使用来填充图形的x轴的,放到percent.html的xaxix的catagory那里'''
    for item0 in re_dict.keys():
        item0 = item0.split(":")
        num_set.add(item0[0])
        optionset.add(item0[1])

    num_list = sorted(list(num_set))
    option_list = sorted(list(optionset))

    print "list=%s" % (num_list)
    print "op_list=%s" % (option_list)

    print "numset=", num_set

    print 'optionset:', optionset
    a_dict = optiontime(option_list, re_dict, num_list)
    print "a_dict=%s" % (a_dict)

    '''a_dict的格式是按percent.html里面的格式放好了,example:{'a':[1,2,5,6,7,0]}'''

    num_str = "||".join(num_list)
    num_str = str(num_str)
    option_str = "||".join(option_list)
    option_str = str(option_str)
    aa_dict = {}
    for i in a_dict:
        time = "||".join(a_dict[i])
        aa_dict[i] = time
    print aa_dict
    """使用num_str,option_str，aa_dict来进行传递是为了解决json不能直接传递集合和列表的问题"""

    num_dict = {"num_dict": num_str}
    option_dict = {"option_dict": option_str}
    qname_dict = {"qname": qname}

    num_dict = json.dumps(num_dict)
    option_dict = json.dumps(option_dict)
    aa_dict = json.dumps(aa_dict)
    qname_dict = json.dumps(qname_dict)
    print "num_dict=%s" % (num_dict)
    print "optionset_print=%s" % (option_dict)
    print "aa_dict=%s" % (aa_dict)

    """content是传给前端的内容，有：题号，选项，每个选项在每道题的值"""
    content = {}
    content['num'] = num_dict
    content['option'] = option_dict
    content['aa_dict'] = aa_dict
    content['username'] = user
    content['qname'] = qname_dict

    return render_to_response('data2.html', content)

"""getnum_list这个函数是为了给用户选择哪些题目是可以进行关联查询获取的题号"""
def getnum_list(username, id):
    result = questions.objects.get(user=username, id=id).result
    result = result.split("||")
    re_dict = {}
    for i in result:
        k = i.split("&")
        k = k[0:-1]
        for item in k:
            item = item.split("$")
            re_dict[item[0]] = item[1]
    "re_dict的作用是把每道题的每个选项和选择的次数以字典方式存进去"
    print "re_dict:", re_dict
    num_set = set()
    for item0 in re_dict.keys():
        item0 = item0.split(":")
        num_set.add(item0[0])

    num_list = list(num_set)
    """num_list是把可以选的题号(除了填空题以为的题号)传到前段的select给用户进行选择"""
    num_list = sorted(num_list)
    return num_list

def Guanlian(request):
    qid = request.GET.get('id', '')
    user = request.COOKIES.get("username")

    content = {}
    content["username"] = user
    content["qid"] = qid

    num_list = getnum_list(user, qid)
    print num_list
    content["num_list"] = num_list

    return render_to_response('Guanlian.html', content)


def GLPrint(request):
    user = request.COOKIES.get("username")
    content = {}
    content["username"] = user

    if request.method == "POST":
        qid = request.POST.get('id', '')
        tm1 = request.POST.get("tm1", "")
        tm2 = request.POST.get("tm2", "")

        tm1 = tm1.decode("utf-8")
        tm2 = tm2.decode("utf-8")

        tm1 = tm1[2:]
        tm2 = tm2[2:]
        print tm1
        print tm2

        tm3 = tm1
        tm4 = tm2



        if re.findall("_", tm1):
            tm1 = tm1.split("_")
            realtm = int(str(tm1[1])) + 2
            tm1 = tm1[0]+"_"+str(realtm)


        if re.findall("_", tm2):
            tm2 = tm2.split("_")
            realtm = int(str(tm2[1]))+2
            tm2 = tm2[0]+"_"+str(realtm)

        print tm2

        num_list = getnum_list(user, qid)
        content["num_list"] = num_list
        content["qid"] = qid


        answer = Answer.objects.filter(qid=qid)
        qname = questions.objects.get(id=qid).q_name
        answer_dict = {}

        for item in answer:
            aanswer1 = item.answer
            print type(item.answer)
            """读取数据库条目用于进行匹配"""
            aanswer1 = aanswer1.split("||")
            a_dict = {}

            print "aanswer=%s"%(aanswer1)
            for i in aanswer1:
                print i
                i = i.split("&")
                print i
                if len(i) > 1:
                    a_dict[str(i[0])] = str(i[1])
            print aanswer1
            try:
                answer1 = a_dict[tm1]
                print "answer1=%s" % (answer1)
            except:
                answer1 = "Null"
            try:
                answer2 = a_dict[tm2]
                print "answer2=%s" % (answer2)
            except:
                answer2 = "Null"

            if answer1+answer2 in answer_dict:
                answer_dict[answer1 + answer2] += 1
            else:
                answer_dict[answer1 + answer2] = 1


        print answer_dict
        qname_dict = {"qname": qname}
        qname_dict = json.dumps(qname_dict)
        content['qname'] = qname_dict
        answer_dict = json.dumps(answer_dict)
        print answer_dict
        content['answer_dict'] = answer_dict

        num_list = getnum_list(user, qid)
        print num_list
        content["num_list"] = num_list

        tm3 = str(tm3)
        tm4 = str(tm4)
        tm34 = tm3 + "||" + tm4
        print tm34
        print type(tm34)
        tm_dict = {"tm34":tm34}
        tm_dict = json.dumps(tm_dict)
        content["tm_dict"] = tm_dict
    return render_to_response('Guanlian2.html', content)

def Chongzhipw(request):
    content = {}
    if request.method == "POST":
        user = request.POST.get("user", "")
        email = request.POST.get("email", "")
        newpassword = request.POST.get("newpassword", "")
        newpassword2 = request.POST.get("newpassword2", "")
        print user
        print email
        print newpassword
        print newpassword2

        try:
            record = User.objects.get(username=user)
            if record.email == email:
                print record.email
                if newpassword == newpassword2:
                    password = hashers.make_password(newpassword)
                    User.objects.filter(username=user).update(password=password)
                    content["status"] = "您已成功修改密码"
                else:
                    print "password_error"
                    content["status"] = "请确认两次输入的是相同的密码"
            else:
                content["status"] = "邮箱错了"


        except:
            record1 = User.objects.filter(username=user)
            print "record1=%s"%(record1)
            print type(record1)
            print len(record1)
            if len(record1) == 0:
                print "false loop"
                content['status'] = "用户不存在"
        print content

    return render_to_response("findpw.html", content)

def Duibi(request):
    qid = request.GET.get('id', '')
    user = request.COOKIES.get("username")
    content = {}
    content["username"] = user
    content["qid"] = qid

    return render_to_response('Duibi.html', content)

def dbreturn(item_dict, optionset, num_list):
    real_item_dict = {}
    optionset = sorted(optionset)
    print optionset
    for item in optionset:
        real_item_dict[item] = ""
        for tm in num_list:
            tm = tm[2:]
            item = str(item)
            opt = tm + "||" + item
            print opt
            if opt in item_dict:
                print item
                print item_dict[opt]
                real_item_dict[item] += str(item_dict[opt]) + "||"
            else:
                real_item_dict[item] += "0" + "||"
    return real_item_dict

def DBPrint(request):
    user = request.COOKIES.get("username")
    content = {}
    content["username"] = user

    if request.method == "POST":
        qid = request.POST.get('id', '')
        content["qid"] = qid
        time1 = request.POST.get('time1', '')
        time2 = request.POST.get('time2', '')
        qid = int(qid)
        num_list = getnum_list(user, qid)
        print "num_list%s"%(num_list)
        """使用NUM_list来进行那些题需要进行统计输出(把填空题排除在外)"""
        qname = questions.objects.get(id=qid).q_name
        all_answer = Answer.objects.all()
        item_dict1 = {}
        item_dict2 = {}
        option_set = set()
        option_dict = {}
        option_dict["options"] = ""
        """item_dict1、2分别用来存储第一段时间的统计结果和第二段时间的统计结果"""

        for i in all_answer:
            date = i.date
            date = date.strftime('%Y-%m-%d')
            qq_id = i.qid
            print "i.answer=%s" % (i.answer)
            if qid == qq_id:
                """先匹配问卷号，然后封开两段时间进行统计"""
                if re.search(time1, date):
                    item_answer = i.answer
                    item_answer = item_answer.split("||")
                    item_answer = item_answer[:-1]

                    for item in item_answer:
                        item = item.split("&")
                        print item[0]
                        print type(item[0])
                        tm0 = []
                        if re.search("_", item[0]):
                            tm0 = item[0].split("_")
                            digit = int(tm0[1]) - 2
                            print type(digit)
                            id_item = "id" + tm0[0] + "_" + str(digit)
                            """这段if是为了判断矩阵题用的，因为数据库里面存的题号跟实际处理题号差2"""
                        else:
                            id_item = "id" + item[0]
                        # print "id_item=%s" %(id_item)
                        # print type(id_item),id_item
                        # print type(num_list[0]),num_list
                        if id_item in num_list:
                            print True
                            print "tm0={}".format(tm0)
                            if tm0 != []:
                                tm1 = tm0[0] + "_" + str(int(tm0[1]) - 2)
                                real_item = tm1 + "||" + item[1]
                            else:
                                real_item = item[0] + "||" + item[1]

                            print real_item, real_item
                            print item_dict1, item_dict1

                            if real_item not in item_dict1:
                                item_dict1[real_item] = 1
                            else:
                                item_dict1[real_item] += 1

                            option_set.add(item[1])


                        else:
                            print False

                        """对应if是用来判断是否在第一段时间里面有匹配成功的时间，若无，则直接处理下一个"""

                elif re.search(time2, date):
                    item_answer = i.answer
                    item_answer = item_answer.split("||")
                    item_answer = item_answer[:-1]

                    for item in item_answer:
                        item = item.split("&")
                        print item[0]
                        print type(item[0])
                        tm0 = []
                        if re.search("_", item[0]):
                            tm0 = item[0].split("_")
                            digit = int(tm0[1])-2
                            print type(digit)
                            id_item = "id"+tm0[0]+"_"+str(digit)
                            """这段if是为了判断矩阵题用的，因为数据库里面存的题号跟实际处理题号差2"""
                        else:
                            id_item = "id"+item[0]
                        # print "id_item=%s" %(id_item)
                        # print type(id_item),id_item
                        # print type(num_list[0]),num_list
                        if id_item in num_list:
                            print True
                            print "tm0={}".format(tm0)
                            if tm0 != []:
                                tm1 = tm0[0] + "_" + str(int(tm0[1])-2)
                                real_item = tm1 + "||" + item[1]
                            else:
                                real_item = item[0] + "||" + item[1]

                            print real_item, real_item
                            print item_dict2, item_dict2

                            if real_item not in item_dict2:
                                item_dict2[real_item] = 1
                            else:
                                item_dict2[real_item] += 1

                            option_set.add(item[1])


                        else:
                            print False

        option_set = sorted(option_set)

        dict1 = dbreturn(item_dict1, option_set, num_list)
        dict2 = dbreturn(item_dict2, option_set, num_list)

        print "dict1={}".format(dict1)
        print "dict2={}".format(dict2)

        option_set_str = "||".join(option_set)
        option_dict["options"] = option_set_str
        print "option_set={}".format(option_set)
        option_dict = json.dumps(option_dict)
        print "option_dict={}".format(option_dict)
        content["option_dict"] = option_dict

        dict1 = json.dumps(dict1)
        dict2 = json.dumps(dict2)

        print "dict1={}".format(dict1)
        print "dict2={}".format(dict2)

        print "num_list={}".format(num_list)
        num_list = "||".join (num_list)
        num_dict = {"num_list": str(num_list)}
        qname_dict = json.dumps({"qname":qname})
        content["num_list"] = num_dict
        content["dict1"] = dict1
        content["dict2"] = dict2
        content["qname"] = qname_dict

    return render_to_response('DBPrint.html', content)







