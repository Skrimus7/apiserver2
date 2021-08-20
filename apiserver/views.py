from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Items
from .serializer import ItemsSerializer


class ItemsView(APIView):
    def get(self, request):
        items = Items.objects.all()
        serializer = ItemsSerializer(items, many=True)
        return Response({"items": serializer.data})

    def post(self, request):
        items = request.data.get("items")

        serializer = ItemsSerializer(data=items)
        if serializer.is_valid(raise_exception=True):
            items_saved = serializer.save()
        return Response({
            "success": "Items '{}' created successfully".format(items_saved.id)
        })

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        saved_items = get_object_or_404(Items.objects.all(), pk=pk)
        data = request.data.get('items')
        serializer = ItemsSerializer(instance=saved_items, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            items_saved = serializer.save()
        return Response({
            "success": "Items '{}' updated successfully".format(items_saved.id)
        })

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        items = get_object_or_404(Items.objects.all(), pk=pk)
        items.delete()
        return Response({
            "message": "Items with id `{}` has been deleted.".format(pk)
        }, status=204)