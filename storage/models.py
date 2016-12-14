from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime import date
from django.utils import timezone

# CATEGORIES
CATEGORIES = (
    ('1', 'Automotive'),
    ('2', 'Microtechnology'),
)
# LINES
LINES = (
    ('1', 'Line 1'),
    ('2', 'Line 2'),
    ('3', 'Line 3'),
    ('4', 'Line 4'),
    ('5', 'Line 5'),
    ('6', 'Line 6'),
    ('7', 'Line 7'),
    ('8', 'Line 8'),
)

# Departments
DEPARTMENTS = (
    ('q', 'quality'),
    ('p', 'production'),
    ('s', 'storage'),
)

# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True)
    name = models.CharField(max_length=50)

    department = models.CharField(
        choices = DEPARTMENTS,
        blank=True,
        null=True,
        max_length=1,
    )

    category=models.CharField(
        choices=CATEGORIES,
        blank=True,
        null=True,
        max_length=1,
    )

    line = models.CharField(
        choices=LINES,
        blank=True,
        default=0,
        max_length=1,
    )

    chief_type = models.CharField(
        choices = (
        ('GM', 'General Manager'),
        ('Ch', 'Chief'),
        ),
        blank=True,
        null=True,
        max_length=2,
    )
    # shift = models.ManyToManyField('shifts', blank=True)

    def __unicode__(self):
        if (self.line == None):
            return "%s, Zone : %s"%(self.name, self.user.username)
        else:
            return "%s, %s, Line : %s"%(self.name, self.get_category_display(), self.line)

# shifts
WEEKDAYS = (
    (1, ("Monday")),
    (2, ("Tuesday")),
    (3, ("Wednesday")),
    (4, ("Thursday")),
    (5, ("Friday")),
    (6, ("Saturday")),
    (7, ("Sunday")),
)
class Shifts(models.Model):
    weekday = models.IntegerField(choices = WEEKDAYS, default = 0)
    from_hour = models.TimeField()
    to_hour = models.TimeField()
    def __unicode__(self):
        return "Day : %s, In : %s, Out %s"%(self.get_weekday_display(), self.from_hour, self.to_hour)



class CheckIn(models.Model):
    CK_TIPO = (
        ('i', 'in'),
        ('o', 'out'),
    )
    ck_employee=models.ForeignKey("Employee", default= 1, blank = True)
    dateTime = models.DateTimeField(default = timezone.now, blank=True)
    ck_tipo = models.CharField(max_length = 1, choices = CK_TIPO)

    def __unicode__(self):
        if self.ck_tipo == 'i':
            return " employee : %s, in -> %s"%(self.ck_employee, self.dateTime)
        else:
            return " employee : %s, out -> %s"%(self.ck_employee, self.dateTime)

class Order(models.Model):
    STATUSES = (
        ('p', 'pending'),
        ('c', 'closed'),
    )
    or_delivery = models.ForeignKey(
        Employee,
        related_name = 'sender',
        on_delete = models.CASCADE,
        limit_choices_to = {
            'department': 's',
        }
    )

    or_receive = models.ForeignKey(
        Employee,
        related_name ='receiver',
         on_delete = models.CASCADE,
         limit_choices_to = {
            'department': 'p',
         }
    )
    or_lineCh = models.ForeignKey(
        Employee,
        related_name ='LineChief',
        on_delete = models.CASCADE,
        limit_choices_to = {
            'category': 'p',
            'chief_type': 'Ch'
        },
    )
    # or_date = models.DateField(auto_now=True)
    or_date_time = models.DateTimeField(default = timezone.now, blank=True)
    or_pieces = models.IntegerField(blank=True, default=0)
    or_status = models.BooleanField(default=True, blank=True)

    def __unicode__(self):
        return "Order: %s, LineChief : %s"%(self.id, self.or_lineCh)

class Shift(models.Model):
    sh_date = models.DateField(default=date.today, blank=True)
    sh_category = models.CharField(max_length=2, choices=CATEGORIES)
    sh_line = models.CharField(max_length=1, choices=LINES)
    sh_total = models.IntegerField()
    sh_finished = models.IntegerField()
    sh_unfinished = models.IntegerField()
    sh_qlty_chkd = models.BooleanField(default=False, blank=True)
    sh_approved = models.IntegerField(blank=True, null=True)
    sh_not_approved = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return "Line -> %s, Date -> %s"%(self.get_sh_line_display(), self.get_sh_category_display)




#   COMENTARIOS

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
