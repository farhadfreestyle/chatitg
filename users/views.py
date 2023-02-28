from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import View, TemplateView
from users.forms import LoginForm, RegisterForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from users.models import Users
class LoginView(View):
    template_name = 'users/login.html'
    form_class = LoginForm
    

    def get(self, request):
        form = self.form_class()
        
        return render(request, self.template_name, context={'login_form':form, 'register_form':RegisterForm,})
    
    def post(self, request):
        message = []
        if 'loginform' in request.POST:
            
            form = self.form_class(request.POST)
  
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = authenticate(
                    email = email,
                    password = password
                )
                

                if user is not None:
                    login(request, user)
                    return redirect('/home/')
                
                elif len(Users.objects.filter(email=email))==0:
                    message.append('Oh dear, You do not have account with this email. Try to sign up!')
                
            else:
                message.append('''Oh dear, You wrote something wronggg!!!''')

            

            return render(request, self.template_name, context={'login_form':form,'error_message':message, 'register_form':RegisterForm})

        elif 'registerform' in request.POST:
            registerForm = RegisterForm(request.POST)
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            email = request.POST['email']

            users = Users.objects.filter(email = email)
            
                
            if len(users)!=0:
                message.append('This email is already in our database. Try to login!')


            elif password1!=password2:
                    message.append('Type slowly ;)')
        
     
    
            elif registerForm.is_valid():

                            
                
                
              
                email = registerForm.cleaned_data['email']
              
              
                
                registerForm.save()
                
                user = Users.objects.get(email = email)
         
                user.username = email
                user.save()
                
                return redirect('/login/')
            else:
                message.append('Use stronger password my dear! Do not use your first or last name in password. Hackers like it :)')
                print('Error happened')
                registerForm = RegisterForm()
            
          
                

            

            return render(request, 'users/login.html', context={'register_form':registerForm, 'error_message':message[::-1], 'login_form':LoginForm})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/home/')
    



class ProfileView(View):
    template_name = 'users/profile.html'
    form_class = ProfileForm
 
    
    def get(self, request):
        form = self.form_class()
        
        return render(request, self.template_name, context={'profile_form':form,})
