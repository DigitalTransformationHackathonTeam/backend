import unittest

from scoring.business import BusinessType, Business


class TestBusiness(unittest.TestCase):
    def test_run(self):
        business = Business('pharmacy')

        print(business.businessType.weight)
