from datetime import timedelta

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils import timezone

from .models import SlideShowItem, Announcement
from pages.models import Stockist, Venue

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
class HomepageUpcomingStockistTests(TestCase):
    def setUp(self):
        self.venue = Venue.objects.create(name='Test Venue')

    def test_upcoming_stockist_shows_earliest_by_start_date(self):
        """Homepage should show the stockist with the earliest start_date."""
        today = timezone.localdate()
        future = today + timedelta(days=30)

        Stockist.objects.create(
            title='Later Event',
            venue=self.venue,
            start_date=today + timedelta(days=10),
            end_date=future,
        )
        early_stockist = Stockist.objects.create(
            title='Earlier Event',
            venue=self.venue,
            start_date=today + timedelta(days=2),
            end_date=future,
        )

        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.context['upcoming_stockist'], early_stockist)

    def test_upcoming_stockist_with_null_start_date_comes_last(self):
        """Stockist with null start_date should not be selected over one with a date."""
        today = timezone.localdate()
        future = today + timedelta(days=30)

        stockist_with_date = Stockist.objects.create(
            title='Has Start Date',
            venue=self.venue,
            start_date=today + timedelta(days=5),
            end_date=future,
        )
        Stockist.objects.create(
            title='No Start Date',
            venue=self.venue,
            start_date=None,
            end_date=future,
        )

        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.context['upcoming_stockist'], stockist_with_date)

    def test_no_upcoming_stockist_when_all_past(self):
        """Homepage should have no upcoming_stockist when all events are in the past."""
        today = timezone.localdate()

        Stockist.objects.create(
            title='Past Event',
            venue=self.venue,
            start_date=today - timedelta(days=30),
            end_date=today - timedelta(days=1),
        )

        response = self.client.get(reverse('homepage'))
        self.assertIsNone(response.context['upcoming_stockist'])

    def test_upcoming_stockist_section_hidden_when_none(self):
        """The upcoming events section should not render when there are no events."""
        response = self.client.get(reverse('homepage'))
        self.assertNotContains(response, 'id="upcoming-event"')
