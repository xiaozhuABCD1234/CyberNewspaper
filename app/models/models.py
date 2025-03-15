# models/models.py
from tortoise.models import Model
from tortoise import fields


class Website(Model):
    id = fields.IntField(primary_key=True)
    name = fields.TextField()
    url = fields.TextField()

    class Meta:
        table = "websites"


class HotItem(Model):
    id = fields.IntField(primary_key=True)
    title = fields.TextField()
    url = fields.TextField()
    heat = fields.TextField(null=True)
    description = fields.TextField(null=True)
    author = fields.TextField(null=True)
    source = fields.ForeignKeyField("models.Website", related_name="hot_items")
    time = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "hot_items"
