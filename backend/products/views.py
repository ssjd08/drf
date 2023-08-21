from rest_framework import generics, mixins, permissions, authentication
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffEditorPermissions
from api.authentications import TokenAuthentication


# class ProdoctMixinAPIView(
#     mixins.CreateModelMixin,
#     mixins.ListModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     mixins.RetrieveModelMixin,
#     generics.GenericAPIView):
    
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = 'pk'
    
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         if pk is not None:
#             return self.retrieve(request, *args, **kwargs)
        
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs) 
    
#     def perform_create(self, serializer):
#         # serializer.save(user=self.request.user)
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content') or None
#         if content is None:
#             content = title
#         serializer.save(content=content)
#         # send a Django signal   
    
#     def update(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)
    
#     def perform_update(self, serializer):
#         instance = serializer.save()
#         if not instance.content:
#             instance.content = instance.title
    
#     def destroy(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs) 

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication,
                              TokenAuthentication]
    permission_classes = [IsStaffEditorPermissions]

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)
        # send a Django signal
   
    
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
    
    
class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)