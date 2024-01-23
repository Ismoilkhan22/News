from django.shortcuts import render
from .models import *
from .forms import ContactForm
from .services import search_sql


# Create your views here.

def index(request):
    ctx = {
        'title': "index"

    }
    return render(request, "index.html", ctx)


def ctg(request, slug):
    ctg = Category.objects.filter(slug=slug).first()
    if not ctg:
        return render(request, "category.html", {"error": 404})
    cnews = New.objects.filter(ctg=ctg).order_by('-pk')

    ctx = {
        'title': "category",
        'ctg': ctg,
        'cnew': cnews[1:]

    }

    try:
        ctx['big'] = cnews[0]
    except:
        return render(request, "category.html", {"error": 404})

    return render(request, "category.html", ctx)


def cnt(request):
    ctx = {
        'title': "contact"

    }
    if request.POST:
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            ctx['success'] = True

    return render(request, "contact.html", ctx)


def search(request):
    key = request.GET.get('search')
    natijalar = search_sql(key)

    ctx = {
        'title': "search",
        'natijalar': natijalar,
        'key': key,
        'len': len(natijalar)

    }
    return render(request, "search.html", ctx)


def view(request, pk: int):
    # new
    root = New.objects.filter(id=pk).first()

    if not root:
        return render(request, "category.html", {"error": 404})

    # comment
    if request.POST:
        ism = request.POST.get('ism')
        msg = request.POST.get('msg')
        Comments.objects.create(

            user=ism,
            msg=msg,
            new=root
        )
    else:
        root.view += 1
        root.save()

    comments = Comments.objects.filter(new=root).order_by('-pk')

    # for html | result  
    ctx = {
        'title': "view",
        'root': root,
        "comments": comments,
        "cson": comments.count()

    }

    return render(request, "view.html", ctx)
