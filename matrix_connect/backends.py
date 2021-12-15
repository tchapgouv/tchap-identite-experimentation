import requests
import json
from django.conf import settings
from django.contrib.auth.backends import RemoteUserBackend
from matrix_connect.models import MatrixUser
from django.core.cache import cache

class MatrixBackend(RemoteUserBackend):

    create_unknown_user = False

    def get_user(self, user_id):
        """
        Takes a User ID from a Sydent DB via Matrix API
        Returns a set of the user account info
        """
        try:
            return cache.get(user_id)
        except MatrixUser.DoesNotExist: # A CHANGER
            return None

    def authenticate(self, request, username=None, password=None):
        """
            1. Get the homeserver URL from the ID server
            2. Perform a POST request to /login with credentials to the homeserver URL
            3. Construct and return a User Object from the User Model
        """

        # 1

        # 2
        payload = {
            "type": "m.login.password",
            "identifier": {
                "type": "m.id.thirdparty",
                "medium": "email",
                "address": username
            },
            "password": password,
            "initial_device_display_name": "tchap_id"
        }
        r = requests.post(settings.MATRIX_LOGIN_URL, json.dumps(payload))
        response = r.json()
        print(response)
        if r.status_code == 200:
            user = MatrixUser()
            user.email = username
            user.matrix_user_id = response['user_id']
            cache.set(username, user, 3600)
            return user
        elif r.status_code == 403:
            return None
        pass