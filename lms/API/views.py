from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils.aws.get_user_token import GetUserToken
from API.utils.decode_user_token import GetUserTokenDetails
from rest_framework.decorators import api_view
import yaml

@api_view(['POST'])
def UserTokenViewSet(request, *args, **kwargs):
    req_args = ['username', 'password']
    for req_arg in req_args:
        if req_arg not in request.data:
            return Response({'error': "{} not found".format(req_arg)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    user_token_obj = GetUserToken("srm")
    status_api, token = user_token_obj.get_user_token(request.data['username'], request.data['password'])
    if status_api:
        try:
            res_token = GetUserTokenDetails(token)
            return Response(res_token)
        except:
            if 'ChallengeParameters' in token and 'userAttributes' in token['ChallengeParameters']:
                userAttributes = token['ChallengeParameters']['userAttributes']
                userAttributes = yaml.load(userAttributes)
                if 'custom:user_portal' in userAttributes and userAttributes['custom:user_portal'].lower() in ['srm', 'school', 'reporter', 'business_partner']:
                    return Response(token)
            
            return Response({'status': 'Failed', 'reason': "User not found"}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({ 'error': "{}".format(token)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        
    return Response({'status': 'Failed', 'reason': "unauthorized"}, status= status.HTTP_422_UNPROCESSABLE_ENTITY)


@api_view(['POST'])
def UserRefreshTokenViewSet(request, *args, **kwargs):
    if "user_uuid" in request.data and "refresh_token" in request.data:
        username = request.data.get('user_uuid')
        username = username.lower()
        username = username.strip()
        refresh_token = request.data.get('refresh_token')
        
        user_token_obj = GetUserToken("srm")
        status_api, token = user_token_obj.get_user_token_using_refresh_token(username, refresh_token)
        if status_api:
            try:
                res_token = GetUserTokenDetails(token)
                return Response(res_token)
            except Exception as e:
                return Response({ 'error': "{}".format(e.__str__())}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        else:
            return Response({ 'error': "{}".format(token)}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            
        return Response({'status': 'Failed', 'reason': "unauthorized"}, status= status.HTTP_422_UNPROCESSABLE_ENTITY)