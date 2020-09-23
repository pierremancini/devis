from django.shortcuts import render, redirect

def accueil(request):
    if request.user.is_authenticated:
        return render(request, 'accueil.html')
    else:
        return redirect('login')