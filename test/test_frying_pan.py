from unittest import TestCase, mock

from french_toast.frying_pan import FryingPan

def mock_requests_get(*args, **kwargs):
        return "<frenchtoast><status>1 Slice - Low</status></frenchtoast>"


class TestFryingPan(TestCase):

    @mock.patch('requests.get', side_effect=mock_requests_get)
    def test_get_french_toast(self, mock_get):
        pan = FryingPan('foo.html', 'status')
        status = pan.get_french_toast()
        self.assertEquals(status, '1 Slice - Low')
        
