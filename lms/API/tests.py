from django.test import TestCase
from .views import UserTokenViewSet
from rest_framework.test import APITestCase, APIClient
from .utils.aws.get_user_token import GetUserToken
from API.utils.aws.add_user import AddUser
from API.utils.aws.get_users import get_users, get_matching_user,get_user_details

# Create your tests here.


class BaseAPITestcase(APITestCase):

    token = ""
    client = APIClient()

    def get_token(self, username="ajith.sundararaj+local@accionlabs.com", password="Accion@123"):
        user_token_obj = GetUserToken("srm")
        status_api, user_token = user_token_obj.get_user_token(data['username'], data['password'])
        token = user_token["access"]
        return token

    def get(self,url,code = None):
        if not self.token:
            self.token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        res = self.client.get(url, format='json')
        if code:
            self.assertEqual(res.status_code, code)
        else:
            self.assertEqual(res.status_code, 200)
        return res

    def post(self, url, data, code=200, username=None, password=None):
        if not self.token:
            self.token = self.get_token(username, password)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        res = self.client.post(url, dataformat='json')
        if code:
            self.assertEqual(res.status_code, code)
        else:
            self.assertEqual(res.status_code, 200)
        return res


class LoginAPITestcase(BaseAPITestcase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_user(self):
        add_srm_user_obj = AddUser("SRM_USER")
        data = {
        "first_name": "tested ",
        "last_name": "s",
        "email": "a@bm12.com",
        "department": "HR",
         "institution_id": 124,
         "user_type": "College Administrator",
        "notes": "Random",
        "phone_number": "+11234567890"
            }
        status_api, create_user = add_srm_user_obj.add_user(data['email'],
                                                            "9",
                                                            data["first_name"],
                                                            data["last_name"],
                                                            data["user_type"],
                                                            data["phone_number"],
                                                            data["department"],
                                                            "9",
                                                            "76bcf848-7d8e-4c74-86cb-fc835e52c090",
                                                            data.get('notes', ''),
                                                            "",
                                                            "",
                                                            "srm",
                                                            )

        # print(status_api,create_user)
        self.assertEqual(status_api,True)

    def test_get_user(self):
        self.get("/api/user/")

    def test_get_milestone(self):
        self.get("/api/milestone/")

    def get_user_info(self,*args,**kwargs):
        response = self.get("/api/user/")
        # print(response.json())

    def test_get_apis(self):
        api =["/api/institute/", "/api/onboarding-type/"]
        for i in api:
            self.get(i)

    def test_search(self):
        self.get("/api/user/?search=")




