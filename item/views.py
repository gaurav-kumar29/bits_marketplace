from django.shortcuts import render

posts = [
    {
        'seller': 'Gaurav Kumar',
        'title': 'Cycle',
        'desc': 'Hercules cycle',
        'base_price': '2000',
        'date_posted': 'October 12, 2021'
    },
    {
        'seller': 'John Doe',
        'title': 'Cycle',
        'desc': 'Hero cycle',
        'base_price': '3000',
        'date_posted': 'October 12, 2021'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'item/home.html', context)