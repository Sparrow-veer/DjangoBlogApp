from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,DOBUpdateForm

# Create your views here.

# def register(request):
#     if(request.method=='post'):
#         form=UserCreationForm(request.POST)
#         if(not form.is_valid()):
#             username=form.cleaned_data.get('username')
#             print(username)
#             messages.success(request, f'Account created for {username}')
#             return redirect('blog-home')
#
#     else:
#         form=UserCreationForm()
#     return render(request,'users/register.html',{'form':form})



class Validation(View):
    def get(self,request,*args,**kwargs):
         form=UserRegisterForm()
         return render(request,'users/register.html',{'form':form})

    def post(self,request,*args,**kwargs):

        if request.method == "POST":
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                print(form.cleaned_data.get('dob'))
                messages.success(request, f'Account created for {username}... U can now Login')
                return redirect('login')
            else:
                return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if(request.method=='POST'):
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        d_form=DOBUpdateForm(request.POST,instance=request.user.dobdetail)

        if(u_form.is_valid() and p_form.is_valid() and d_form.is_valid()):
            u_form.save()
            p_form.save()
            d_form.save()
            messages.success(request, f'User Info Updated!!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        d_form= DOBUpdateForm(instance=request.user.dobdetail)
    context={
        'u_form':u_form,
        'p_form':p_form,
        'd_form':d_form

    }
    return render(request,'users/profile.html',context)
