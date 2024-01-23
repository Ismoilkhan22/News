import requests as re
from news.models import Category, New


def valyuta(request):
    url = "https://cbu.uz/oz/arkhiv-kursov-valyut/json/"

    respons = re.get(url).json()

    return {"val": respons}


def ctg(request):
    return {
        "ctgs": Category.objects.filter(is_menu=True),
        "sql_img_url": "http://127.0.0.1:8000/media/"

    }


def yangilar(request):
    news = New.objects.all().order_by('-pk')
    return {
        "svejilar0": news[:4],  # 0,1,2,3
        "svejilar1": news[4:8]  # 4,5,6,7

    }
