from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def UserLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.success(request, ("Login unsuccessful - Please try again"))
            return render(request, 'userlogin')
    else:
        return render(request, 'member/login.html', {})


def UserLogOut(request):
    logout(request)
    return redirect('home')


# class MemberSignUp(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'member/signup.html'
#     success_url = reverse_lazy('login')

#     class Meta:
#         model = UserCreationForm
#         fields = ('username', 'password1', 'password2')

#     def __init__(self, *args, **kwargs):
#         super(MemeberSignUp, self).__init__(*args, **kwargs)

#         self.fields['username'].widget.attrs['class'] = 'form-input'
#         self.fields['password1'].widget.attrs['class'] = 'form-input'
#         self.fields['password2'].widget.attrs['class'] = 'form-input'
