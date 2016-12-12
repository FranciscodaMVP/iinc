from django.contrib import admin
from models import Employee, Shifts, CheckIn, Order
#from models import line, line_chief, quality_chief, reg_employee, pieces
#from models import order, piece_quantity, entrance
# Register your models here.

admin.site.register(Employee)
admin.site.register(Shifts)
admin.site.register(CheckIn)
admin.site.register(Order)

'''
admin.site.register(line)
admin.site.register(line_chief)
admin.site.register(quality_chief)
admin.site.register(reg_employee)
admin.site.register(pieces)
admin.site.register(order)
admin.site.register(piece_quantity)
admin.site.register(entrance)
'''
