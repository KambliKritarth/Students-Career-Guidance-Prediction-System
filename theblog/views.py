from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import InputForm
from django.http import JsonResponse
from theblog.models import Score, Comment, Contact
import pickle
#import random
# Create your views here.
#def home(request):
    #return render(request,'home.html',{})
def myform(request):
    return render(request,'myform.html')


def careeroptions(request):
    return render(request,'careeroptions.html')

def aptitude(request):
    return render(request,'aptitude.html')

def aptitude_cse(request):
    return render(request,'aptitude_cse.html')

def aptitude_extc(request):
    return render(request,'aptitude_extc.html')

def getPredictions(Tenthmarks, Twelfthmarks, Gender, Sports, Indo, Danc, Teach, Art, Sing, WestClass, Fest, Speech, Gam, Strict, ClassR, Pers, Oly, OlyMar,  Head):
    
    model = pickle.load(open("careerguide.sav","rb"))
    scaled = pickle.load(open("careerguidescaler.sav","rb"))
    prediction = random.choice(tuple(sample_set))
    return prediction

def submitmyform(request):
    '''dbf = request.GET['DBF'] #not getting dbf
    return dbf'''
    model = Score
    all_scores = Score.objects.all
    
    #print(mydictionary["name"]), name = mydictionary["name"], lastname = mydictionary["lastname"],
    result =getPredictions(request.POST.get('Tenthmarks',0) , request.POST.get('Twelfthmarks',0), request.POST.get('Gender',0) , request.POST.get('Sports',0) ,request.POST.get('Indo',0) , request.POST.get('Danc',0), request.POST.get('Teach',0), request.POST.get('Art',0), request.POST.get('Sing',0), request.POST.get('WestClass',0), request.POST.get('Fest',0), request.POST.get('Speech',0), request.POST.get('Gam',0), request.POST.get('Strict',0), request.POST.get('ClassR',0),request.POST.get('Pers',0), request.POST.get('Oly',0), request.POST.get('OlyMar',0), request.POST.get('Head',0))
    sample_set = {"Software Engineer", "Investment Banker", "Consultant", "Product Designer","Financial Accountant","Bank Engineer","Jr. College Professor","Physiotherapist","Civil Engineer","Architect","Orthodontist","Sales Manager"}
   
    ins = Score( result, DataBaseF, CA, DCS, Net, SoftWD, ProgSkills, AIML, SWE, BusinessAnalysis, DataScience, GraphDesign)

    ins.save()
    print(result)
    return render(request,'submitmyform.html',{'submitmyform':result})
    #print(result)
    #{'result':result}
    #this function is called in myform.html in {%%}
    #return JsonResponse(mydictionary)

def contact(request):
    model = Contact
    all_contacts = Contact.objects.all
    name = request.POST.get('name',"Anonymous")
    user_contact = request.POST.get('contact',"Contactless")
    user_query = request.POST.get('query',"Queryless")
    ins = Contact(name=name,contact = user_contact,query = user_query)
    ins.save()
    print(name)
    return render(request, 'contact.html')


class ScoreView(ListView):
    model = Score
    template_name = 'submitmyform.html'

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post 
    template_name = 'article_details.html'

class ContactView(ListView):
    model = Post
    template_name = 'contact.html'

class AddQueryView(CreateView):
    model = Comment
    #form_class = QueryForm
    template_name = 'add_query.html' 
    fields = ('name','body')
    
    #success_url = reverse_lazy('home')

 

'''def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})'''
