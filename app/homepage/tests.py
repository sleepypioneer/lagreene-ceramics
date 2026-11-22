from unittest.mock import patch

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils import timezone

from .models import SlideShowItem, Announcement, NewsItem

small_image = (
    b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x05'
    b'\x04\x04\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00'
    b'\x02\x02\x44\x01\x00\x3b'
)


class SlideShowItemTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.slideShowItem = SlideShowItem.objects.create(
            title="Test slide show item",
            image=SimpleUploadedFile(
                'small.gif', small_image, content_type='image/gif'
            )
        )

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.slideShowItem.title, str)


class AnnouncementTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_date = timezone.make_aware(timezone.datetime(2010, 1, 1))
        cls.announcement = Announcement.objects.create(
            subject="Test subject",
            body="Test body",
            image=SimpleUploadedFile(
                'small.gif', small_image, content_type='image/gif'
            ),
            link="www.testurl.org",
            publish_date=test_date,
            end_date=test_date
        )

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.announcement.subject, str)
        self.assertIsInstance(self.announcement.body, str)
        self.assertIsInstance(self.announcement.link, str)


@override_settings(STORAGES={
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"},
})
class HomepageNewsTests(TestCase):
    def setUp(self):
        instagram = patch(
            'django_instagram.templatetags.instagram_client.instagram_profile_obj',
            return_value=None,
        )
        instagram.start()
        self.addCleanup(instagram.stop)

    def test_news_items_are_displayed_in_order(self):
        later = NewsItem.objects.create(
            title='Later News', main_text='Later text', itemOrder=1
        )
        earlier = NewsItem.objects.create(
            title='Earlier News', main_text='Earlier text', itemOrder=2
        )

        response = self.client.get(reverse('homepage'))
        self.assertQuerySetEqual(response.context['news_items'], [earlier, later])
        self.assertContains(response, 'Earlier text')
        self.assertContains(response, 'Later text')
        self.assertLess(
            response.content.index(b'Earlier News'),
            response.content.index(b'Later News'),
        )

    def test_news_item_renders_optional_image_and_link(self):
        item = NewsItem.objects.create(
            title='News with extras',
            main_text='News text',
            image='img/news/example.jpg',
            link='https://example.com/news',
        )

        response = self.client.get(reverse('homepage'))
        self.assertContains(response, f'src="{item.image.url}"')
        self.assertContains(response, 'href="https://example.com/news"')

    def test_news_item_without_optional_fields(self):
        NewsItem.objects.create(title='Simple news', main_text='News text')

        response = self.client.get(reverse('homepage'))
        self.assertContains(response, 'Simple news')
        self.assertNotContains(response, 'news-item-image-container')
        self.assertNotContains(response, 'Read more')

    def test_news_section_hidden_when_empty(self):
        response = self.client.get(reverse('homepage'))
        self.assertQuerySetEqual(response.context['news_items'], [])
        self.assertNotContains(response, 'id="news-items"')

    def test_upcoming_stockist_section_hidden_when_none(self):
        """The upcoming events section should not render when there are no events."""
        response = self.client.get(reverse('homepage'))
        self.assertNotContains(response, 'id="upcoming-event"')
