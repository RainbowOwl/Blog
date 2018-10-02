from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from apps.custom_auth.enums import RoleTypes
from apps.custom_auth.models import User


class Command(BaseCommand):
    help = 'Create three users with different permissions'

