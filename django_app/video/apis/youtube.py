from django.shortcuts import render
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from video.models import Video


DEVELOPER_KEY = "AIzaSyAHbqOAoglx5EX-fCoSaAkjM14rF02g4YE"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(keyword, page_token, max_results=10,):
    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY
    )

    search_response = youtube.search().list(
        q=keyword,
        part="id,snippet",
        maxResults=max_results,
        pageToken=page_token
    ).execute()


    video_id_list = []

    print(page_token)

    for item in search_response['items']:
        cur_video_id = item['id']['videoId']
        video_id_list.append(cur_video_id)
    video_id = ','.join(video_id_list)

    # print(video_id)

    video_response = youtube.videos().list(
        id=video_id,
        part="id,snippet,statistics,contentDetails",
        maxResults=max_results,
    ).execute()


    for item in video_response['items']:
        cur_video_id = item['id']
        if Video.objects.filter(youtube_id=cur_video_id).exists():
            item['is_exist'] = True

    # video_id_list = [item['id']['videoId'] for item in search_response['items']]
    # exist_list = Video.objects.filter(youtube_id__in=video_id_list)
    # exist_id_list = [video.youtube_id for video in exist_list]
    # for item in search_response['items']:
    #     cur_video_id = item['id']['videoId']
    #     if cur_video_id in exist_id_list:
    #         item['is_exist'] = True

    video_response['prevPageToken'] = search_response.get('prevPageToken')
    video_response['nextPageToken'] = search_response.get('nextPageToken')
    # return search_response
    return video_response







