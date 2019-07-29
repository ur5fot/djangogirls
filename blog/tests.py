from django.conf.urls import url
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.utils import json

from blog.models import Post


class PostsTests(APITestCase):

    def test_create_post(self):
        post = {
            'title': "Title: 1",
            "text": "xcdascas",
            "created_date": "2019-07-29 00:00",
            "published_date": "2019-07-29 00:00",
            "author_id": 1
        }

        response = self.client.post(reverse('post-list'), post, format='json')
        # response = self.client.post(reverse('post-list'), post,  content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.get().title, 'Title: 1')

    def test_update_post(self):
        Post.objects.create(
            title='Title: 1',
            text='Давно выяснено, что при оценке дизайна и композиции ч',
            created_date='2019-07-29 00:00',
            published_date='2019-07-29 00:00',
            author_id=1
        )

        updated_post = {
            'title': 'updated_post Title: 1',
            'text': 'Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает сосредоточиться.',
            'created_date': '2019-07-29 00:00',
            'published_date': '2019-07-29 00:00',
            'author_id': 1
        }

        response = self.client.put(reverse('post-detail', kwargs={'pk': Post.objects.get().pk}),
                                   updated_post, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.get().title, 'updated_post Title: 1')

    def test_delete_post(self):
        Post.objects.create(
            title='Title: 1',
            text='Давно выяснено, что при оценке дизайна и композиции ч',
            created_date='2019-07-29 00:00:00',
            published_date='2019-07-29 00:00:00',
            author_id=1
        )
        response = self.client.delete(reverse('post-detail', kwargs={'pk': Post.objects.get().pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
