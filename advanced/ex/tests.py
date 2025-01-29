from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Article


class ViewsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='aboba')
        self.article = Article.objects.create(title='Test Article', author=self.user, synopsis='aboba', content='aboba')
        
        self.favourites_url = reverse('favourites')
        self.publications_url = reverse('publications')
        self.publish_url = reverse('publish')
        self.home_url = reverse('home')
        self.login_url = reverse('login')
        self.registration_url = reverse('register')
        
    def test_favourites_publications_publish_only_for_registered_users(self):
        response = self.client.get(self.favourites_url)
        self.assertRedirects(response, self.login_url + '?next=/en/favourites/')
        
        response = self.client.get(self.publications_url)
        self.assertRedirects(response, self.login_url + '?next=/en/publications/')
        
        response = self.client.get(self.publish_url)
        self.assertRedirects(response, self.login_url + '?next=/en/publish/')
        
        self.client.login(username='testuser', password='aboba')
        
        response = self.client.get(self.favourites_url)
        self.assertEqual(response.status_code, 200)        
        
        response = self.client.get(self.publications_url)
        self.assertEqual(response.status_code, 200)
                
        response = self.client.get(self.publish_url)
        self.assertEqual(response.status_code, 200)

    def test_registered_user_cant_access_to_register_page(self):
        self.client.login(username='testuser', password='aboba')
        
        response = self.client.get(self.registration_url)
        self.assertRedirects(response, self.home_url)
        
    def test_user_cant_add_same_article_twice(self):
        self.client.login(username='testuser', password='aboba')
        self.client.post("/add_fav/", {"article_id": self.article.id})
        
        response = self.client.post("/add_fav/", {"article_id": self.article.id})
        self.assertEqual(response.status_code, 400)

