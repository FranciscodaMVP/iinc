from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import datetime

# Create your models here.
class employee(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=50)

    is_lineCh = models.BooleanField(default=False, blank=True)
    is_qtCh = models.BooleanField(default=False, blank=True)
# CATEGORIES
    Auto = 1
    Micro = 2
    Nothing = 3
    CATEGORIES = [
        (Auto, 'Auto'),
        (Micro, 'Micro'),
        (Nothing, 'Nothing')
    ]
    category=models.IntegerField(choices=CATEGORIES, default=0)
    line = models.IntegerField(blank=True, null=True, default=None)
    is_production = models.BooleanField(default=False, blank=True)
    is_storage = models.BooleanField(default=False, blank=True)
    shift = models.ManyToManyField('shifts', blank=True)

    def __unicode__(self):
        if (self.line == None):
            return "%s, Zone : %s"%(self.name, self.user.username)
        else:
            return "%s, %s, Line : %s"%(self.name, self.get_category_display(), self.line)

# shifts
WEEKDAYS = [
    (1, ("Monday")),
    (2, ("Tuesday")),
    (3, ("Wednesday")),
    (4, ("Thursday")),
    (5, ("Friday")),
    (6, ("Saturday")),
    (7, ("Sunday")),
]
class shifts(models.Model):
    weekday = models.IntegerField(choices = WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()
    def __unicode__(self):
        return "Day : %s, In : %s, Out %s"%(self.get_weekday_display(), self.from_hour, self.to_hour)


class checkIn(models.Model):
    ck_employee=models.ManyToManyField(employee)
    date = models.DateField(auto_now=True)
    in_hour = models.TimeField(auto_now=True, blank=True)
    out_hour = models.TimeField(blank=True)

class order(models.Model):
    STATUSES = [
        ('p', 'pending'),
        ('c', 'closed'),
    ]
    or_delivery = models.ForeignKey(employee, related_name = 'sender', on_delete = models.CASCADE)
    or_receive = models.ForeignKey(employee, related_name ='receiver', on_delete = models.CASCADE)
    or_lineCh = models.ForeignKey(employee, related_name ='LineChief', on_delete = models.CASCADE)
    or_date = models.DateField(auto_now=True)
    or_time = models.TimeField(auto_now=True)
    or_status = models.CharField(choices=STATUSES, default='p', max_length=1)
    or_pieces = models.IntegerField(blank=True, default=0)
    or_finished = models.IntegerField(blank=True, default=0)

    def __unicode__(self):
        return "Order: %s, LineChief : %s"%(self.id, self.or_lineCh)
        
'''
class employee(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=50)

class pieces(models.Model):
    pz_number = models.IntegerField()
    pz_name = models.CharField(max_length=40)

class order(models.Model):
    or_number = models.AutoField
    or_delivery = models.OneToOneField(reg_employee, related_name = 'sender', on_delete = models.CASCADE)
    or_receive = models.OneToOneField(reg_employee, related_name ='receiver', on_delete = models.CASCADE)
    or_line_chief = models.OneToOneField(line_chief, on_delete = models.CASCADE)
    or_piece = models.OneToOneField(pieces)
    or_pieces_number = models.IntegerField()
    or_date = models.DateTimeField(default=datetime.date.today)
    or_is_open = models.BooleanField(default = True)

class piece_quantity(models.Model):
    pq_order = models.ForeignKey(order, related_name='order_number', on_delete = models.CASCADE)
    pq_piece = models.ForeignKey(order, related_name='piece_number', on_delete = models.CASCADE)
    pz_quantity = models.IntegerField()

class entrance(models.Model):
    date = models.DateField(default=datetime.date.today)
    entrance = models.TimeField()
    departure = models.TimeField()
    employee = models.OneToOneField(User, on_delete = models.CASCADE)

    class Meta:
        unique_together = ('date', 'employee')


#faltan los turnos


class line(models.Model):
    ln_number = models.IntegerField()
    CATEGORIES = [
        (1, ('Auto')),
        (2, ('Micro')),
    ]
    ln_category = models.IntegerField(
    choices = CATEGORIES,
    )

    def __unicode__(self):
        return 'Line : %s -> %s'%(self.ln_number, self.ln_category)

class line_chief(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    chief_name = models.CharField(max_length=70)

    CH_CATEGORIES = [
        (1, ('Auto')),
        (2, ('Micro')),
    ]
    ch_category = models.IntegerField(
    choices = CH_CATEGORIES,
    )
    lc_line = models.OneToOneField(line)

class quality_chief(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    chief_name = models.CharField(max_length=70)

    QL_CATEGORIES = [
        (1, ('Production')),
        (2, ('Storage')),
    ]
    ch_category = models.IntegerField(
    choices = QL_CATEGORIES,
    )
    qc_line = models.OneToOneField(line)

class reg_employee(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    reg_name = models.CharField(max_length=70)
    REG_CATEGORIES = [
        (1, ('Production')),
        (2, ('Storage')),
    ]
    reg_category = models.IntegerField(
    choices = REG_CATEGORIES,
    )
'''
