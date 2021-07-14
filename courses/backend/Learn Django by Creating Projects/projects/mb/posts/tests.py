from django.test import TestCase
from .models import Post
from django.urls import reverse
# Create your tests here.


class PostModelTest(TestCase):

    # not used for test
    def setUp(self):
        # create a simple post, text is our model field
        Post.objects.create(text='just a test')

    # used for test because this method
    # start with "test_something"
    def test_text_content(self):
        post = Post.objects.get(id=1)
        excepted_object_name = f'{post.text}'
        self.assertEqual(excepted_object_name, 'just a test')


class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        print(Post.objects.all())
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        # reverse(optional_name) return the
        # actual url, for current situation it is just '/'
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        print(resp)
        self.assertTemplateUsed(resp, 'posts/home.html')
