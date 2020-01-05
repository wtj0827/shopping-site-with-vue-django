from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from .serializers import SaleInfoSerializer
from .models import SaleInfo


@csrf_exempt
@api_view(['GET', 'POST'])
def saleinfo_list(request):

    if request.method == 'GET':
        saleinfo = SaleInfo.objects.all()
        serializer = SaleInfoSerializer(saleinfo, context={'request': request}, many=True)
        return Response({'data': serializer.data})
    elif request.method == 'POST':
        serializer = SaleInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

