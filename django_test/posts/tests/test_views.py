from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from posts.models import Post


class PostViewTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="email1@example.com",
            password="Password1!",
        )
        self.user.post_set.create(
            title="title1",
            content="content1",
        )
        self.post_list_url = reverse("posts:list")
        self.post_create_url = reverse("posts:create")

    def test_post_list_page_redirects_to_signin_page_for_user_not_logged_in(self):
        response = self.client.get(self.post_list_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/signin/?next=/posts/")

    def test_post_list_page_renders_post_list_template_for_user_logged_in(self):
        self.client.login(
            email="email1@example.com",
            password="Password1!",
        )
        response = self.client.get(self.post_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/list.html')

    def test_post_create_page_redirects_to_signin_page_for_user_not_logged_in(self):
        response = self.client.get(self.post_create_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/signin/?next=/posts/create/")

    def test_post_create_page_renders_post_create_template_for_user_logged_in(self):
        self.client.login(
            email="email1@example.com",
            password="Password1!",
        )
        response = self.client.get(self.post_create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/create.html')

    def test_post_create(self):
        self.client.login(
            email="email1@example.com",
            password="Password1!",
        )
        data = {
            "title": "title2",
            "content": "content2",
        }
        response = self.client.post(self.post_create_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("posts:detail", kwargs={"pk": 2}))
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(self.user.post_set.count(), 2)

    def test_post_detail_page_renders_post_detail_template_for_user_logged_in(self):
        self.client.login(
            email="email1@example.com",
            password="Password1!",
        )
        response = self.client.get(reverse("posts:detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/detail.html')

    def test_post_delete(self):
        self.client.login(
            email="email1@example.com",
            password="Password1!",
        )
        response = self.client.post(reverse("posts:delete", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("posts:list"))
        self.assertEqual(Post.objects.count(), 0)
        self.assertEqual(self.user.post_set.count(), 0)

    def test_post_delete(self):
        self.client.login(
            email="email1@example.com",
            password="Password1!",
        )
        data = {
            "title": "title2",
            "content": "content2",
        }
        response = self.client.post(reverse("posts:update", kwargs={"pk": 1}), data)
        post = Post.objects.get(id=1)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("posts:detail", kwargs={"pk": 1}))
        self.assertEqual(post.title, "title2")
        self.assertEqual(post.content, "content2")
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(self.user.post_set.count(), 1)
