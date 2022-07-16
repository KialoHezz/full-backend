from django.shortcuts import render

# Inside dictionary have Key and Value ,therefore ,to access value you can use the key
def index(request):
    name = 'Hezron'
    context = {
        'name':name
    }
    return render(request, 'blog/home.html',context)


def counter(request):
    words = request.POST['words']
    amount_of_words = len(words.split())
    ctx = {
        "amount": amount_of_words,
    }
    return render(request, 'blog/counter.html',ctx)