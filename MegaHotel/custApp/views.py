from django.shortcuts import render

# Create your views here.
def board(request):
     return render(request,'custTemp/board.html')

def logout(request):
     try:
        print("Before delete session=",request.session['em'],request.session['pwd'])
        del request.session['em']
        del request.session['pwd']
        print("session deleteed")
        print("after delete session=",request.session['em'],request.session['pwd'])
       
     except KeyError:
        pass
     return render(request,'megaTemp/logout.html')