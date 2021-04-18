from datetime import datetime
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import SlideShowItem, Announcement

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
            image=SimpleUploadedFile('small.gif', small_image, content_type='image/gif')
        )

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.slideShowItem.title, str)


class AnnouncementTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.announcement = Announcement.objects.create(
            subject="Test subject",
            body="Test body",
            image=SimpleUploadedFile('small.gif', small_image, content_type='image/gif'),
            link="www.testurl.org",
            publish_date=datetime(2010, 1, 1),
            end_date=datetime(2010, 1, 1)
        )

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.announcement.subject, str)
        self.assertIsInstance(self.announcement.body, str)
        self.assertIsInstance(self.announcement.link, str)
