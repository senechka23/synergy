from django.test import TestCase
from django.urls import reverse
from .models import Visitor


class WelcomePageTests(TestCase):
    def test_welcome_page_opens(self):
        response = self.client.get(reverse("welcome_page"))
        self.assertEqual(response.status_code, 200)

    def test_visitor_is_saved(self):
        response = self.client.post(reverse("welcome_page"), {"display_name": "Роман"})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Visitor.objects.filter(display_name="Роман").exists())
        self.assertContains(response, "Здравствуйте, Роман!")

    def test_empty_visitor_is_rejected(self):
        response = self.client.post(reverse("welcome_page"), {"display_name": "   "})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Visitor.objects.count(), 0)

    def test_outer_spaces_are_trimmed(self):
        self.client.post(reverse("welcome_page"), {"display_name": "  Роман  "})
        self.assertTrue(Visitor.objects.filter(display_name="Роман").exists())

    def test_compound_name_is_accepted(self):
        response = self.client.post(reverse("welcome_page"), {"display_name": "Анна-Мария Иванова"})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Visitor.objects.filter(display_name="Анна-Мария Иванова").exists())

    def test_symbols_are_rejected(self):
        for display_name in ["Роман*", "Иван)", "Анна;", "Петр%", "№Роман"]:
            with self.subTest(display_name=display_name):
                Visitor.objects.all().delete()
                response = self.client.post(reverse("welcome_page"), {"display_name": display_name})
                self.assertEqual(response.status_code, 200)
                self.assertEqual(Visitor.objects.count(), 0)
                self.assertContains(
                    response,
                    "Имя может содержать только буквы, пробелы и дефис.",
                )
