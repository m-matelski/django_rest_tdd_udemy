# mocking avaliblity/not avalibility of our db
from unittest.mock import patch
# allows to call command in source code
from django.core.management import call_command
# operational error thrown by django when db is unavalable
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""
        # use patch to mock ConnectionHandler to always set true (connection to db is available ervery time its called)
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        # use patch to mock ConnectionHandler to always set true (connection to db is available ervery time its called)
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
