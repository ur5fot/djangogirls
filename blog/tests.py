from django.test import TestCase, client
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase, APIRequestFactory
from django.conf.urls import url
from rest_framework.utils import json


class PostsTests(APITestCase):
    urlpatterns = [
        path('', include('blog.urls')),
    ]

    def test_create_post(self):
        data = {
            "title": "Title: 1 test  test test test",
            "text": "Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает сосредоточиться. Lorem Ipsum используют потому, что тот обеспечивает более или менее стандартное заполнение шаблона, а также реальное распределение букв и пробелов в абзацах, которое не получается при простой дубликации \"Здесь ваш текст.. Здесь ваш текст.. Здесь ваш текст..\" Многие программы электронной вёрстки и редакторы HTML используют Lorem Ipsum в качестве текста по умолчанию, так что поиск по ключевым словам \"lorem ipsum\" сразу показывает, как много веб-страниц всё ещё дожидаются своего настоящего рождения. За прошедшие годы текст Lorem Ipsum получил много версий. Некоторые версии появились по ошибке, некоторые - намеренно (например, юмористические варианты).",
            "created_date": "2019-07-27 14:19:25+00:00",
            "published_date": "2019-07-27 14:21:55+00:00",
            "author_id": 1
        }
        response = self.client.post(reverse('api_post-list'), json.dumps(data), format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
