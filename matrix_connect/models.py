from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import uuid

class MatrixUser(AbstractBaseUser):

    #user_id =           models.CharField(max_length=8, null=False, editable=False, primary_key=True)
    #user_id =           models.CharField(max_length=8, null=False, editable=False, default=uuid.uuid4, primary_key=True)
    email =             models.EmailField(max_length=50, primary_key=True)
    matrix_user_id =    models.CharField(max_length=256, null=False, editable=False)
    #display_name =      models.CharField(max_length=256, null=False, editable=False)
    #session_token

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = None

    class Meta:
        managed=False

    def save(self, update_fields):
        pass

    def get_group_permissions (self):
        """If you don't make your own permissions module,
        the default also will use the DB. Throw it away"""
        return [] # likewise with the other permission defs

    def get_and_delete_messages (self):
        """Messages are stored in the DB. Darn!"""
        return []