from peewee import *
import click

data_base = DatabaseProxy()


class BaseModel(Model):
    class Meta:
        database = data_base


class OriginReport(BaseModel):
    id = PrimaryKeyField(null=False)
    abbr = CharField(max_length=100)
    name = CharField(max_length=100)
    team = CharField(max_length=100)
    duration = CharField(max_length=100)

    class Meta:
        db_table = 'race_report'


