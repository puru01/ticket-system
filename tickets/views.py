# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Ticket
#from .serializers import ticketSerializer
from django.http import HttpResponse
from django.template import loader


class Get_tickets_List(APIView):
    def get(self, request):
        tics = Ticket.objects.all()
        serialized = ticketSerializer(tics, many=True)
        return Response(serialized.data)


def index(request):
    tics = Ticket.objects.all()
    return render(request, 'index.html', { 'tics' : tics} )


def insert(request):
    insertintodb(request)
    return render(request, 'insert.html', {})


def insertintodb(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('requestuser'):
                newticket=Ticket()
                newticket.title= request.POST.get('title')
                newticket.requestuser = request.POST.get('requestuser')
                if request.POST.get('ttype'):
                    newticket.ttype = request.POST.get('ttype')
                if request.POST.get('category'):
                    newticket.category = request.POST.get('category')
                if request.POST.get('priority'):
                    newticket.priority = request.POST.get('priority')

                newticket.save()
                
                return render(request, 'index.html')  

        else:
                return render(request,'index.html')

'''
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
'''






#def homepage(request):
#    tics = Ticket.objects.all()
#    return render(request, 'index.html', { 'tics' : tics })
'''
def index(request):
    tic_list = Ticket.objects.order_by('tid')
    template = loader.get_template(tickets/index.html)
    context = {
    	'tic_list' : tic_list,
    }
    #output = ', '.join([p.name for p in tic_list])
    #return HttpResponse(output)
    return HttpResponse(template.render(context,request))
def get_users(request):
    users = User.objects.all().values('first_name', 'last_name')  # or simply .values() to get all fields
    users_list = list(users)  # important: convert the QuerySet to a list object
    return JsonResponse(users_list, safe=False)
'''