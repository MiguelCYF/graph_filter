from django.http import JsonResponse, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from graph_yv.graph_filter import filter_edges


def response_json(self):
    result = {"name": "laowang"}
    return JsonResponse(result)


@csrf_exempt
def add(request):
    print(request.POST)
    a = request.POST.get('a')

    result = {'add': int(a) + 100}
    return JsonResponse(result)


@csrf_exempt
def from_json(request):
    input_json = json.loads(request.body)
    print(input_json)
    return HttpResponse("ok")


@csrf_exempt
def graph_test(request):
    input_json = json.loads(request.body)

    re_edges = input_json["edges"]
    re_input_nodes = input_json["input_nodes"]
    threshold = input_json["threshold"]

    edges = []
    for x in re_edges:
        edges.append((x["src"], x["desc"]))

    result = {}
    try:
        data = filter_edges(edges, re_input_nodes, threshold)
        result["data"] = data
        result["code"] = 200
        result["msg"] = "success"
    except Exception as e:
        result["data"] = None
        result["code"] = 500
        result["msg"] = str(e)

        print(str(e))

    return HttpResponse(json.dumps(result))