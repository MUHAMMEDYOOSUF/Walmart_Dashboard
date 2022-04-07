from django.db import models
import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Create your models here.

class my_ml(models.Model):

    temp=models.FloatField()
    fuel=models.FloatField()
    cpi=models.FloatField()
    unemp=models.FloatField()
    week=models.IntegerField()
    ishol=models.IntegerField()
    store=models.IntegerField()
    dept=models.IntegerField()
    typ=models.IntegerField()
    size=models.IntegerField()
    pred=models.FloatField(blank=True)

    def save(self,*args,**kwargs):
        ml_model=joblib.load('mt_walmart.joblib')
        self.pred=np.round(ml_model.predict([[self.temp,self.fuel,self.cpi,self.unemp,self.week,self.ishol,self.store,self.dept,self.typ,self.size]]))
        return super().save(*args,*kwargs)

    def __str__(self):
        return self.store


class data(models.Model):
    Store=models.IntegerField()
    Dept=models.IntegerField()
    Weekly_Sales=models.FloatField()





