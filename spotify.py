import json
from requests import post, get
from dotenv import load_dotenv
import os
import base64
from icecream import ic

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    results = post(url, headers=headers, data=data)
    json_result = json.loads(results.content)
    token = json_result["access_token"]
    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def search_artist(token, artist):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"q={artist}&type=artist&limit=1"
    query_url = url + "?" + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    return json_result['artists']['items'][0]['id']


def search_albums(token, artistID):
    url = "https://api.spotify.com/v1/artists/"
    headers = get_auth_header(token)
    query = "" + artistID + "/albums"
    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    print(json_result)

def search_songs(token, artistID):
    url = "https://api.spotify.com/v1/artists/"
    headers = get_auth_header(token)
    query = "" + artistID + "/top-tracks"
    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    print(json_result)


token = get_token()
#ic(token)
artistID = search_artist(token, "Ruslana")
#ic(artistID)
#search_albums(token, artistID)
search_songs(token, artistID)
#search_songs(token, "Дикі танці")



