
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response

class CrudApi(APIView):
    def post(self, request):
        print(request.data)
        serializers=CrudSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=202)
        return Response(serializers.errors, status=400)

    def get(self, request):
        allData = CrudModel.objects.all()
        serializer = CrudSerializer(allData, many=True)
        return Response(serializer.data, status=200)

    def put(self, request):
        print("put=", request.data)
        udata = CrudModel.objects.get(id=request.data['id'])
        serializers = CrudSerializer(udata, data=request.data)
        if serializers.is_valid():
            serializers.save()
        else:
            return Response(status=400)
        return Response(status=200)

    def delete(self, request):
        ddata = CrudModel.objects.get(id=request.data['id'])
        ddata.delete()
        return Response(status=200)


class DataGetById(APIView):
    def post(self, request):
        print(request.data['uid'])
        udata = CrudModel.objects.get(id=request.data['uid'])
        serializers = CrudSerializer(udata)
        return Response(serializers.data, status=200)
