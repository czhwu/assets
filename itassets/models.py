from django.db import models

# Create your models here.


class State(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Assets(models.Model):
    fid = models.IntegerField()
    fgdzc = models.CharField(max_length=20)
    fname = models.CharField(max_length=50)
    fdate = models.DateTimeField()
    fuser = models.CharField(max_length=50)
    fdep = models.CharField(max_length=50)
    fip = models.GenericIPAddressField()
    fdate_rz = models.DateField()
    fdate_bf = models.DateField()
    smark = models.BooleanField()
    fstore = models.CharField(max_length=50)
    fuserold = models.CharField(max_length=50)
    f1 = models.CharField(max_length=30)
    f2 = models.CharField(max_length=30)
    fdate_ys = models.DateField()
    fstate = models.ForeignKey(State)

    def __str__(self):
        return self.fgdzc
