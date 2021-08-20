from django.db import models


class Items(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.UUIDField()
    parent_uuid = models.UUIDField()
    type = models.CharField(max_length=20)
    name = models.TextField()
    meta = models.TextField()
    data = models.TextField()
    modified = models.DateTimeField()

    def __str__(self):
        return self.id
