from tortoise.models import Model
from tortoise import fields


class Data(Model):
    date = fields.CharField(max_length=15, pk=True)
    cargo_type = fields.CharField(max_length=25, null=True)
    rate = fields.FloatField(max_length=230, null=True)

    def __str__(self):
        return self.date, self.cargo_type, self.rate
