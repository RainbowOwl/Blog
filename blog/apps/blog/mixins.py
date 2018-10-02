from django.http import HttpResponseRedirect
from django.urls import reverse


class RoleVerificationMixin:

    @property
    def role_types(self):
        """
        Class with 'RoleVerificationMixin' should have roly_types attribute.
        :return:
        """
        raise NotImplementedError

    def verify_role(self, user):
        if hasattr(user, 'role'):
            if user.role in self.role_types:
                return True
        return False
        # return HttpResponseRedirect(reverse('blog:index'))

    def post(self, request, *args, **kwargs):
        if self.verify_role(request.user):
            return super().post(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('blog:index'))

    def get(self, request, *args, **kwargs):
        if self.verify_role(request.user):
            return super().get(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('blog:index'))
