from datetime import timedelta

from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.test import SimpleTestCase, TestCase, override_settings
from django.urls import path, reverse
from django.utils import timezone

from pages.models import Stockist, Venue


def response_error_handler(request, exception=None):
    return HttpResponse('Permission denied!', status=403)


def permission_denied_view(request):
    raise PermissionDenied


urlpatterns = [
    path('403/', permission_denied_view),
]

handler403 = response_error_handler


# ROOT_URLCONF must specify the module that contains handler403 = ...
@override_settings(ROOT_URLCONF=__name__)
class CustomErrorHandlerTests(SimpleTestCase):

    def test_handler_renders_template_response(self):
        response = self.client.get('/403/')
        # Make assertions on the response here. For example:
        self.assertContains(response, 'Permission denied!', status_code=403)


@override_settings(STORAGES={
    "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
    "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"},
})
class StockistsViewTests(TestCase):
    def setUp(self):
        self.venue = Venue.objects.create(name='Test Venue')

    def test_current_stockists_ordered_by_start_date(self):
        """Current stockists should be ordered by start_date ascending."""
        now = timezone.now().date()
        future = now + timedelta(days=30)

        # Create stockists with future end_dates and varying start_dates
        stockist_late = Stockist.objects.create(
            title='Late Start',
            venue=self.venue,
            start_date=now + timedelta(days=10),
            end_date=future,
        )
        stockist_early = Stockist.objects.create(
            title='Early Start',
            venue=self.venue,
            start_date=now + timedelta(days=2),
            end_date=future,
        )
        stockist_mid = Stockist.objects.create(
            title='Mid Start',
            venue=self.venue,
            start_date=now + timedelta(days=5),
            end_date=future,
        )

        response = self.client.get(reverse('stockists'))
        current = list(response.context['current_stockists'])

        self.assertEqual(current, [stockist_early, stockist_mid, stockist_late])

    def test_current_stockists_null_start_date_last(self):
        """Current stockists with null start_date should appear last."""
        now = timezone.now().date()
        future = now + timedelta(days=30)

        stockist_with_date = Stockist.objects.create(
            title='Has Start Date',
            venue=self.venue,
            start_date=now + timedelta(days=5),
            end_date=future,
        )
        stockist_null = Stockist.objects.create(
            title='No Start Date',
            venue=self.venue,
            start_date=None,
            end_date=future,
        )

        response = self.client.get(reverse('stockists'))
        current = list(response.context['current_stockists'])

        self.assertEqual(current, [stockist_with_date, stockist_null])

    def test_past_stockists_ordered_by_end_date_desc(self):
        """Past stockists should be ordered by end_date descending."""
        now = timezone.now().date()

        stockist_oldest = Stockist.objects.create(
            title='Oldest',
            venue=self.venue,
            start_date=now - timedelta(days=60),
            end_date=now - timedelta(days=30),
        )
        stockist_newest = Stockist.objects.create(
            title='Newest',
            venue=self.venue,
            start_date=now - timedelta(days=10),
            end_date=now - timedelta(days=1),
        )
        stockist_middle = Stockist.objects.create(
            title='Middle',
            venue=self.venue,
            start_date=now - timedelta(days=30),
            end_date=now - timedelta(days=15),
        )

        response = self.client.get(reverse('stockists'))
        past = list(response.context['past_stockists'])

        self.assertEqual(past, [stockist_newest, stockist_middle, stockist_oldest])
