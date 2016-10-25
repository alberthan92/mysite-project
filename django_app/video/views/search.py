from django.shortcuts import render
from video.apis.youtube import youtube_search

__all__ = ['search']

def search(request):
    context = {}
    keyword = request.GET.get('keyword')
    page_token = request.GET.get('page_token')
    if keyword:
        response = youtube_search(keyword, page_token)
        context['keyword'] = keyword
        context['response'] = response

    return render(request, 'video/search.html', context)

    # json_str = json.dumps(response, indent=2, sort_keys=True)
    # print(json_str)
    # print(type(json_str))
    # json_object = json.loads(json_str)
    # print(type(json_object))
    #
    # context = {
    #     'response': response,
    # }