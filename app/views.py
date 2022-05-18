from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from app.serializers import *

# Create your views here.

def HTMLTemplate(articleTag):
    return f''' 
    <html>
    <body>
        <h1><a href="/">Image Upload</a></h1>
        {articleTag}
    </body>
    </html>
    '''

def imageupload(request):
    article = '''
            <form action="/create/" method="post">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit"</p>
            </form>
        '''
    return HttpResponse(HTMLTemplate(article))

"""
[fashion matching test] : FashionTest(fashion matching test)
"""

class FashionTest(APIView):
    """
    POST : [fashion matching test] personal color와 옷 이미지를 분석해 적합도(rate) 반환
    """

    parser_classes = [FormParser, MultiPartParser]

    """
    post 내용
    'color' : personal color
    'image'
    """
    def post(self, request, format=None):
        data = {'color': request.data['color'], 'image' : request.data['image']}
        
        ''' serializer : django의 모델 instance를 rest api의 json 형태로 변환'''
        serializer = FashionTestSerializer(data=data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response({
                'id' : instance.id.hashid,
                'spring_rate' : instance.spring_rate,
                'summer_rate' : instance.summer_rate,
                'autumn_rate' : instance.autumn_rate,
                'winter_rate' : instance.winter_rate,
                'result' : instance.result
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTP_400_BAC_REQUEST)