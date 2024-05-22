import unittest
from unittest.mock import patch
import datetime
from main import alarm_clock

class TestAlarmClock(unittest.TestCase):

    @patch('winsound.PlaySound')
    @patch('datetime.datetime')
    def test_alarm_clock(self, mock_datetime, mock_winsound):
        mock_datetime.now.return_value = datetime.datetime(2023, 5, 25, 12, 30, 0)
        mock_datetime.side_effect = [datetime.datetime(2023, 5, 25, 12, 30, 0)]
        alarm_clock(12, 30, 0)
        mock_winsound.assert_called_once_with('anyfile.wav', mock_winsound.SND_ASYNC)

    @patch('winsound.PlaySound')
    @patch('datetime.datetime')
    def test_alarm_clock_different_time(self, mock_datetime, mock_winsound):
        mock_datetime.now.return_value = datetime.datetime(2023, 5, 25, 10, 0, 0)
        mock_datetime.side_effect = [datetime.datetime(2023, 5, 25, 10, 0, 0)]
        alarm_clock(12, 30, 0)
        mock_winsound.assert_not_called()

    @patch('winsound.PlaySound')
    @patch('datetime.datetime')
    def test_alarm_clock_invalid_time(self, mock_datetime, mock_winsound):
        mock_datetime.now.return_value = datetime.datetime(2023, 5, 25, 25, 0, 0)
        mock_datetime.side_effect = [datetime.datetime(2023, 5, 25, 25, 0, 0)]
        with self.assertRaises(ValueError):
            alarm_clock(25, 0, 0)
        mock_winsound.assert_not_called()

if __name__ == '__main__':
    unittest.main()
