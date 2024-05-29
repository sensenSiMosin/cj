from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import Article
from .models import User
from django.http import HttpResponse
from .forms import ArticleForm


def user_list(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request,'templates/article/user.html',context)

def article_list(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request,'templates/article/list.html',context)

def article_detail(request,id):
    articles = Article.objects.get(id=id)
    context = {'articles':articles}
    print(context)
    return render(request,'templates/article/detail.html',context)

def article_create(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            article_post_form = ArticleForm(data=request.POST)
            if article_post_form.is_valid():
                new_article = article_post_form.save(commit=False)
                new_article.author = request.user
                new_article.save()
                return redirect('list')
            else:
                return HttpResponse(article_post_form.errors)
        else:
            return HttpResponse('请先登录')
    else:
        article_post_form = ArticleForm()
        context = {'article_post_form':article_post_form}
        return render(request,'templates/article/create.html',context)

def article_delete(request,id):
    try:
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        return HttpResponse("文章不存在")

    if article.author == request.user:
        article.delete()
        return redirect('list')
    else:
        return HttpResponse("您没有权限删除这篇文章")


# 更新文章
def article_update(request, id):
    # 获取需要修改的具体文章对象
    article = Article.objects.get(id=id)
    # 判断用户是否为 POST 提交表单数据
    if request.method == "POST":
        print(article)
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticleForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid():
            # 保存新写入的 title、body 数据并保存
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            # 完成后返回到修改后的文章中。需传入文章的 id 值
            # return redirect("article:article_detail", id=id)
            return redirect("detail",id=id)
        # 如果数据不合法，返回错误信息
        else:
            return HttpResponse("表单内容有误，请重新填写。")
    # 如果用户 GET 请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticleForm()
        # 赋值上下文，将 article 文章对象也传递进去，以便提取旧的内容
        context = {'article': article, 'article_post_form': article_post_form}
        # 将响应返回到模板中
        return render(request, 'templates/article/update.html', context)

