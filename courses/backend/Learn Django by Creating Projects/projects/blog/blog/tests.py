from django.http import response
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post


class BlogTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user
        )

    def test_string_representation(self):
        post = Post(title='A sample title')
        # print(post)
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        # print(self.post)
        self.assertEqual(f'{ self.post.title }', 'A good title')
        self.assertEqual(f'{ self.post.author }', 'testuser')
        self.assertEqual(f'{ self.post.body }', 'Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        # print(response)    
        self.assertEqual(response.status_code, 200)
        # print(response.content)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed('home')
        self.assertTemplateNotUsed('post_detail')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        print(response)
        no_response = self.client.get("/post/1000/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertContains(response, "Nice body content")
        self.assertTemplateUsed('post_detail')
        # self.assertTemplateUsed('post_detail.html') # same as previous