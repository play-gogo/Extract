import pandas as pd
import requests
import os
import json

def get_key():
    """영화진흥위원회 가입 및 API 키 생성 후 환경변수 선언 필요"""
    key = os.getenv('MOVIE_API_KEY')
    return key

def movie_url(dt="20120101", url_param = {}):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"
    for key, value in url_param.items():
        #url = url + "&multiMovieYn=N"
        url = url + f"&{key}={value}"

    return url


