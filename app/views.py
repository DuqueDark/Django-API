from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework import generics
from rest_framework import viewsets

from app.models import Todo
from app.serializers import TodoSerializer

#########################
#---------- V3----------#
#########################
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


#########################
#---------- V2----------#
#########################
class TodoListAndCreate2(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
   
class TodoDatailChangeDelete2(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer   
    
#########################
#---------- V1----------#
#########################
class TodoListAndCreate(APIView):
    def get(self, request):
        return Response(TodoSerializer(Todo.objects.all(), many=True).data)
    
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
"""
    @api_view(['GET','POST'])
    def todo_list(request):
        
        if request.method == 'GET':
            return Response(TodoSerializer(Todo.objects.all(), many=True).data)
        
        elif request.method == 'POST':
            serializer = TodoSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

Keyword arguments:
argument -- description
Return: return_description
"""
class TodoDatailChangeDelete(APIView):
    
    def get_pbject(self,id):
        try:
            return Todo.objects.get(pk=id)
            
        except Todo.DoesNotExist:
            raise NotFound()
        
    
    def get(self, request, pk):
        
        return Response(TodoSerializer(self.get_pbject(pk)).data,status.HTTP_200_OK)
    
    def put(self, request, pk):
        
        serializer = TodoSerializer(self.get_pbject(pk),data=request.data)
            
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        
        self.get_pbject(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
"""
    @api_view(['GET','PUT','DELETE'])
    def todo_datail_change_delete(request, pk):
        
        try:
            todo = Todo.objects.get(pk=pk)
            
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            return Response(TodoSerializer(todo).data,status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            serializer = TodoSerializer(todo,data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
Keyword arguments:
argument -- description
Return: return_description
"""