from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status


class HelloWorld(APIView):
    """
    クラスベースのAPIViewです。
    """
    def get(self, request, format=None):
        return Response({"message": "Hello World!!"},
                        status=status.HTTP_200_OK)

    def post(self, request, format=None):
        request_data = request.data

        return Response({"message": request_data["message"]},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def hello_world(request):
    """
    関数ベースのAPIViewです。
    """
    if request.method == 'GET':
        return Response({"message": "Hello function base APIView GET!!"},
                        status=status.HTTP_200_OK)
    elif request.method == 'POST':
        if request.data:
            request_data = request.data
            return Response({"message": request_data["message"]},
                            status=status.HTTP_201_CREATED)
