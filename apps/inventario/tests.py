# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import hashlib

from django.test import TestCase

# Create your tests here.


# class Foo(object):
#
#     def gravatar_url(self, email):
#         hash = hashlib.md5(email.lower()).hexdigest()
#         return "https://www.gravatar.com/avatar/" + hash
#
#     # Después el código de nuestra prueba
#
#
# class FooTestCase(unittest.TestCase):
#         # Instanciamos un objeto foo antes de correr cada prueba
#     def setUp(self):
#             self.foo = Foo()
#
#     def test_get_gravatar_url(self):
#             result = self.foo.gravatar_url("example1@gmail.com")
#             self.assertEquals(result,
#                               "https://www.gravatar.com/avatar/f3e820cc128ffde207328176830dff87")
#
# if __name__ == "__main__":
#         unittest.main()



class Patient:
    def __init__(self, prescriptions=None):
        self.prescriptions = prescriptions or []

    def add_prescription(self, prescription):
        self.prescriptions.append(prescription)

    def days_taking(self, medicine_name):
        prescriptions = filter(lambda p: p.name == medicine_name, self.prescriptions)
        days = set()
        for prescription in prescriptions:
            days.update(prescription.days_taken())
        return days

    def clash(self, medicine_names):
        days_taking = [self.days_taking(medicine_name) for medicine_name in medicine_names] or [set()]
        return set.intersection(*days_taking)


from datetime import date, timedelta

# from patient import Patient
# from prescription import Prescription


def days_ago(days):
    return date.today() - timedelta(days=days)


class TestPatient:
    def test_clash_with_no_prescriptions(self):
        patient = Patient(prescriptions=[])
        assert patient.clash([]) == set()

    def test_clash_with_one_irrelevant_prescription(self):
        patient = Patient(prescriptions=[Prescription("Codeine", dispense_date=days_ago(days=2), days_supply=2)])
        assert patient.clash(["Prozac"]) == set()

    def test_clash_with_one_prescription(self):
        patient = Patient(prescriptions=[Prescription("Codeine", dispense_date=days_ago(days=2), days_supply=2)])
        assert patient.clash(["Codeine"]) == {days_ago(days=2), days_ago(days=1)}

    def test_clash_with_two_different_prescriptions(self):
        patient = Patient(prescriptions=[Prescription("Codeine", dispense_date=days_ago(days=2), days_supply=2),
                                         Prescription("Prozac", dispense_date=days_ago(days=2), days_supply=2)])
        assert patient.clash(["Codeine", "Prozac"]) == {days_ago(days=2), days_ago(days=1)}

    def test_clash_with_two_prescriptions_for_same_medication(self):
        patient = Patient(prescriptions=[Prescription("Codeine", dispense_date=days_ago(days=2), days_supply=2),
                                         Prescription("Codeine", dispense_date=days_ago(days=3), days_supply=2)])
        assert patient.clash(["Codeine"]) == {days_ago(days=3), days_ago(days=2), days_ago(days=1)}

    def test_days_taking_for_irrelevant_prescription(self):
        patient = Patient(prescriptions=[Prescription("Codeine", dispense_date=days_ago(days=2), days_supply=2)])
        assert patient.days_taking("Prozac") == set()

    def test_days_taking(self):
        patient = Patient(prescriptions=[Prescription("Codeine", dispense_date=days_ago(days=2), days_supply=2),
                                         Prescription("Codeine", dispense_date=days_ago(days=3), days_supply=2)])
        assert patient.days_taking("Codeine") == {days_ago(days=3),
                                                  days_ago(days=2),
                                                  days_ago(days=1)}

    def test_clash_overlapping_today(self):
        patient = Patient(prescriptions=[Prescription("Codeine", dispense_date=days_ago(days=2), days_supply=3),
                                         Prescription("Prozac", dispense_date=days_ago(days=2), days_supply=3)])
        assert patient.clash(["Codeine", "Prozac"]) == {days_ago(days=2), days_ago(days=1)}