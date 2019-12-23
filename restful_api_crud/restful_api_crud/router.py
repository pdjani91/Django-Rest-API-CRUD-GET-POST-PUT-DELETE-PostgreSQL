from employee_api.viewsets import EmployeeViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee',EmployeeViewset)


#localhost:project/api/employe/3
#GET, POST, UPDATE(PUT), DELETE
#List, Retrive