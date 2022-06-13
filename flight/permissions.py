from rest_framework import permissions



class IsStufforReadOnly(permissions.IsAdminUser):
    def has_permission(self, request,view):
        if request.method in permissions.SAFE_METHODS:   # bu Safe_method=[Get, Head,options] demek sen burda  request.method=='GET de yazabilirdin'
            return True
        return bool(request.user and request.user.is_staff)