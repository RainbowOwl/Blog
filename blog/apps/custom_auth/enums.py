from django.utils.translation import ugettext_lazy as _


class RoleTypes:
    ADMINISTRATOR = 'administrator'
    MANAGER = 'manager'
    COMMON = 'common'

    Choices = (
        (ADMINISTRATOR, _('Administrator')),
        (MANAGER, _('Manager')),
        (COMMON, _('Common')),
    )