# from rest_framework import permissions
# from django.contrib.auth.models import Group

# # get_group_permissions(obj=None)

# class ProductManagerPermission(permissions.IsAdminUser):
    

#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return bool(request.user and request.user.is_staff)

    # def has_permission(self, request, view):
    #     group = Group.objects.filter(user_id = request.user.id)
    #     print(group)
    #     return True
#         return bool(request.user and request.group.id == 2)

# class IsStafforReadOnly(permissions.IsAdminUser):
    
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return bool(request.user and request.user.is_staff)