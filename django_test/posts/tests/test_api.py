import json

from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from posts.models import Post


class PostAPIViewTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="email1@example.com",
            password="Password1!",
        )
        self.user.post_set.create(
            title="title1",
            content="content1",
        )
        self.api_post_list_url = reverse("api:posts")

    def test_api_post_list_for_user_not_logged_in(self):
        response = self.client.get(self.api_post_list_url)
        self.assertEqual(response.status_code, 403)

    def test_api_post_list_for_user_logged_in(self):
        self.client.login(
            email="email1@example.com",
            password="Password1!",
        )
        response = self.client.get(self.api_post_list_url)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(len(data), 1)
        self.assertDictEqual(
            data[0],
            {
                "id": 1,
                "title": "title1",
                "content": "content1",
                "url": reverse("posts:detail", kwargs={"pk": 1}),
                "author_email": "email1@example.com",
            }
        )

    def test_api_post_detail(self):
        self.client.login(
            email="email1@example.com",
            password="Password1!",
        )
        response = self.client.get(reverse("api:post_detail", kwargs={"pk": 2}))
        self.assertEqual(response.status_code, 404)

        response = self.client.get(reverse("api:post_detail", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode("utf-8"))
        self.assertDictEqual(
            data,
            {
                "id": 1,
                "title": "title1",
                "content": "content1",
                "url": reverse("posts:detail", kwargs={"pk": 1}),
                "author_email": "email1@example.com",
            }
        )
