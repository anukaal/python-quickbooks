import unittest

from quickbooks.objects.employee import Employee


class EmployeeTests(unittest.TestCase):
    def test_unicode(self):
        employee = Employee()
        employee.DisplayName = "test"

        self.assertEquals(unicode(employee), "test")

    def test_to_ref(self):
        employee = Employee()
        employee.DisplayName = "test"
        employee.Id = 100

        ref = employee.to_ref()

        self.assertEquals(ref.name, "test")
        self.assertEquals(ref.type, "Employee")
        self.assertEquals(ref.value, 100)