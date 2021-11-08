import requests

from conf import settings
from django.contrib.auth.backends import BaseBackend

class MatrixBackend(BaseBackend):
    def get_user(self, user_id):
        """
        Takes a User ID from a Sydent DB via Matrix API
        Returns a set of the user account info
        """
        return None
        pass

    def authenticate(self, request, username=None, password=None):
        """
         
        """
        requestBody = {
            "type": "m.login.password",
            "identifier": {
                "type": "m.id.email",
                "user": username
            },
            "password": password,
            "initial_device_display_name": "Jungle Phone"
        }
        r = requests.post()
        return None
        pass