from django.db import models
from django.shortcuts import render
from django.urls import reverse

# Create your models here.
class Surgeon(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name="Имя")
    birdhday = models.DateField(auto_now_add=False, verbose_name="Дата рождения")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('surgeon', kwargs={'surg_id': self.pk})
    
    class Meta:
        ordering = ['id']
    
class Workschedule(models.Model):
    start = models.CharField(max_length=255)
    beforedinner = models.CharField(max_length=255)
    dinner = models.CharField(max_length=255)
    afterdinner = models.CharField(max_length=255)
    end = models.CharField(max_length=255)
    surg = models.ForeignKey('Surgeon', on_delete=models.PROTECT)

    class Meta:
        ordering = ['id']

class Receptiondays(models.Model):
    monday = models.CharField(max_length=255, null=True)
    tuesday = models.CharField(max_length=255, null=True)
    wensday = models.CharField(max_length=255, null=True)
    thursday = models.CharField(max_length=255, null=True)
    friday = models.CharField(max_length=255, null=True)
    surg = models.ForeignKey('Surgeon', on_delete=models.PROTECT)

    class Meta:
        ordering = ['id']

class Scheddepartures(models.Model):
    monday = models.CharField(max_length=255, null=True)
    tuesday = models.CharField(max_length=255, null=True)
    wensday = models.CharField(max_length=255, null=True)
    thursday = models.CharField(max_length=255, null=True)
    friday = models.CharField(max_length=255, null=True)
    surg = models.ForeignKey('Surgeon', on_delete=models.PROTECT)

    class Meta:
        ordering = ['id']

class Duty(models.Model):
    month = models.CharField(max_length=255, null=True)
    day = models.CharField(max_length=255, null=True)
    dutytype = models.CharField(max_length=255, null=True)
    dutytime = models.CharField(max_length=255, null=True)
    dayornight = models.CharField(max_length=255, null=True)
    surg = models.ForeignKey('Surgeon', on_delete=models.PROTECT)

    class Meta:
        ordering = ['id']

# class Operation(models.Model):
#     operationdate = models.DateTimeField()
#     surg = models.ForeignKey('Surgeon', on_delete=models.PROTECT)

#     # def __str__(self):
#     #     return self.surg
    
#     def get_absolute_url(self):
#         return reverse('operation', kwargs={'oper_id': self.pk})

    

#     class Meta:
#         ordering = ['id']
    


# class OpeartionSchedule(models.Model):
#     operationdate = models.DateTimeField()
#     surg = models.ForeignKey('Surgeon', on_delete=models.PROTECT)
#     oper = models.ForeignKey('Operation', on_delete=models.PROTECT)

#     # def __str__(self):
#     #     return self.oper

#     def get_absolute_url(self):
#         return reverse('operations', kwargs={'oper_id': self.pk})
    
#     class Meta:
#         ordering = ['id']


# class PatientInfo(models.Model):
#     patientname = models.CharField(max_length=255)
#     diagnosis = models.CharField(max_length=255)
#     chrronicdeseases = models.CharField(max_length=255)
#     transferredoperations = models.CharField(max_length=255)
#     medicalcontraindications = models.CharField(max_length=255)
#     oper = models.ForeignKey('Operation', on_delete=models.PROTECT)

#     # def get_absolute_url(self):
#     #     return reverse('operations', kwargs={'oper_id': self.pk})

#     class Meta:
#         ordering = ['id']




class Operation(models.Model):
    operationdate = models.DateTimeField()
    surg = models.ForeignKey('Surgeon', on_delete=models.PROTECT)

    # def __str__(self):
    #     return self.operationdate
    
    def get_absolute_url(self):
        return reverse('operations', kwargs={'oper_id': self.pk})

    

    class Meta:
        ordering = ['id']
    


class OpeartionSchedule(models.Model):
    operationdate = models.DateTimeField()
    surg = models.ForeignKey('Surgeon', on_delete=models.PROTECT)
    oper = models.ForeignKey('Operation', on_delete=models.PROTECT, null=True, unique=False)

    # def __str__(self):
    #     return self.oper

    def get_absolute_url(self):
        return reverse('operationnn', kwargs={'oper_id': self.pk})
    
    class Meta:
        ordering = ['id']


class PatientInfo(models.Model):
    patientname = models.CharField(max_length=255)
    diagnosis = models.CharField(max_length=255)
    chrronicdeseases = models.CharField(max_length=255)
    transferredoperations = models.CharField(max_length=255)
    medicalcontraindications = models.CharField(max_length=255)
    oper = models.ForeignKey('Operation', on_delete=models.PROTECT)

    # def get_absolute_url(self):
    #     return reverse('operations', kwargs={'oper_id': self.pk})

    class Meta:
        ordering = ['id']