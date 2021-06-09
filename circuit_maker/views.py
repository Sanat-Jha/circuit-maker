import json
from django.shortcuts import render
from django.http import JsonResponse
from .circuitmaker import makecircuit
import json
import time
# from django.views.csrf import csrf_exempt
def home(request):
    return render(request,"index.html")

def getsvg(request):
    if request.method == "POST":
        circuit = request.POST.get('circuitlst')
    else:
        circuit = request.GET.get('circuitlst')
    circuit = json.loads(circuit)
    circuitsvg = makecircuit(circuit)
    circuitsvg = str(circuitsvg)
    return JsonResponse({"circuitsvg":circuitsvg})
