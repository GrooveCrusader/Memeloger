import datetime
import unittest
import weeklog_utility as wutil

class TestDatetimeMethods(unittest.TestCase):
    '''
    Tests related to datetime
    '''

    def test_midweek_year_change(self):
        '''
        Test passes if weeklog_utility functions
        handle midweek year change correctly
        '''
        test_dt = datetime.datetime(2017,1,1)
        self.assertEqual(52, wutil.get_week(test_dt))
        self.assertEqual(2016, wutil.get_year(test_dt))

    def test_week_of_sunday(self):
        '''
        Test passes if 23:59:59 of Sunday belongs to the
        same week as 00:00:01 of Monday of the same week
        '''
        test_dt_monday = datetime.datetime(2017,8,21, 0, 0, 1)
        test_dt_sunday = datetime.datetime(2017,8,27,23,23,59)
        self.assertEqual(wutil.get_week(test_dt_monday), wutil.get_week(test_dt_sunday))

if __name__ == '__main__':
    unittest.main()