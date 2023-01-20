from secretss import refresh_Token, base64
import requests
import json




# class Refresh:
#
#     def __init__(self):
#         self.refresh_Token = refresh_Token
#         self.base_64 = base64
#
#     def refresh(self):
#         query = "https://accounts.spotify.com/api/token"
#         response = requests.post(query,
#                                  data={"grant_type": "refresh_token",
#                                        "refresh_token": refresh_Token},
#                                  headers={"Authorization": "Basic " + base64})
#         return (response.json()["access_token"])


def refresh():
    query = "https://accounts.spotify.com/api/token"
    response = requests.post(query,
                             data={"grant_type": "refresh_token",
                                   "refresh_token": refresh_Token},
                             headers={"Authorization": "Basic " + base64})
    return (response.json()["access_token"])

