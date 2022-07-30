from django.shortcuts import render

# Create your views here.
def index(request):
    #latest_question_list=Question.objects.order_by('-pub_date')[:5]

    #return HttpResponse(template.render(context,request))
    return render(request,'question1/index.html')
