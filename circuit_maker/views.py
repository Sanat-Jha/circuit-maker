import json
from django.shortcuts import render
from django.http import JsonResponse
from .circuitmaker import makecircuit
import json
def home(request):
    return render(request,"index.html")

def getsvg(request):
    circuit = request.POST.get('circuitlst')
    circuit = json.loads(circuit)
    circuitsvg = makecircuit(circuit)
    circuitsvg = str(circuitsvg)
    return JsonResponse({"circuitsvg":circuitsvg})
