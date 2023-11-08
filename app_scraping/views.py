#proses pengambilan data komntar dari api youtube

import csv
from django.shortcuts import render
from googleapiclient.discovery import build
from django.conf import settings
from django.http import HttpResponse, JsonResponse

# Create your views here.
#ambil id video menggunakan form

def index(request):
    context = {
        'title' : 'title',
        'data' : settings.API_KEY_YOUTUBE,
    }
    return render(request, 'pages/scraping/index.html', context)

def proses_id(request):
    if request.method == 'GET':
        id_video = request.GET.get('id_video')
        max_komentar = request.GET.get('jumlah_komentar')
        api_key = settings.API_KEY_YOUTUBE

        youtube = build('youtube', 'v3', developerKey=api_key)
        comments = []

        nextPageToken = None
        while True:
            response = youtube.commentThreads().list(
                part= 'snippet',
                videoId= id_video,
                maxResults= max_komentar,
                textFormat= 'plainText',
                pageToken= nextPageToken
            ).execute()

            for index, item in enumerate(response['items'], start=1):
                username = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
                comment_text = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comments.append({'number': index, 'username': username, 'comment': comment_text})

            nextPageToken = response.get('nextPageToken')

            if not nextPageToken:
                break

        context = {
            'comments': comments,
        }

        return render(request, 'pages/scraping/proses_id.html', context)
    else:
        return JsonResponse({'error': 'Invalid request method'})

def export_to_csv(request):
    if request.method == 'GET':
        comments_data = request.GET.getlist('comments[]')

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="comments.csv"'

        writer = csv.writer(response)
        writer.writerow(['No.', 'Username', 'Komentar'])

        for index, comment_data in enumerate(comments_data, start=1):
            number, username, comment_text = comment_data.split('|')
            writer.writerow([index, username, comment_text])

        return response
    else:
        return HttpResponse('Invalid request method')

    

