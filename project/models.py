from peewee import *

data_base = DatabaseProxy()


class BaseModel(Model):
    class Meta:
        database = data_base


class OriginReport(BaseModel):
    id = AutoField(null=False)
    abbr = CharField(max_length=100)
    name = CharField(max_length=100)
    team = CharField(max_length=100)
    duration = CharField(max_length=100)
    start = CharField(max_length=100)
    end = CharField(max_length=100)

    class Meta:
        table_name = 'race_report'
