from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserformAPI, UserRegisterAPI      #dev'ing of models
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
# @login_required
def index(request):
    return render(request, 'base.html', {})
    
def signin(request):
    form = UserformAPI()
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email = email, password = password)
        login(request, user)
        if user == None:
            return HttpResponse("Invalid credentials.")
            
            return redirect('/')  #watch here again
        else:
            form = UserformAPI()
    return render(request, 'login.html', {'form': form})
        
    # return HttpResponse("Valid credentials.")
        

def signout(request):
    logout(request)
    return redirect('/')
    
        

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        newuser = User.objects.create_user( first_name = firstname, last_name = lastname, username = username, email= email, password = password)
        try:
            newuser.save()
        except:
            return render('Something went wrong')
    else:
        form = UserRegisterAPI()
    return render(request, 'register.html', {'form': form})


from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes



def passwordChangeDone(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "templates/reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("passwordChange/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="templates/reset_pages_template/reset_page.html", context={"password_reset_form":password_reset_form})
