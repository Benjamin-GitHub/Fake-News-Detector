import unittest

import h11
import mistune
from flask import Flask, session
from nbconvert import HTMLExporter
from nbformat import v4
from sklearn.naive_bayes import MultinomialNB

from vectorizer_utils import create_pipeline


class DependencyRegressionTests(unittest.TestCase):
    def test_http_parser_rejects_malformed_chunk_terminator(self):
        connection = h11.Connection(h11.SERVER)
        connection.receive_data(
            b'POST / HTTP/1.1\r\nHost: example.com\r\n'
            b'Transfer-Encoding: chunked\r\n\r\n1\r\naX\n0\r\n\r\n'
        )
        with self.assertRaises(h11.RemoteProtocolError):
            while connection.next_event() is not h11.NEED_DATA:
                pass

    def test_deep_markdown_does_not_exhaust_recursion(self):
        self.assertIsInstance(mistune.html('*' * 1000), str)

    def test_session_membership_marks_response_as_cookie_dependent(self):
        application = Flask(__name__)
        application.secret_key = 'local-test-key'

        @application.get('/')
        def index():
            return str('user' in session)

        response = application.test_client().get('/')
        self.assertIn('Cookie', response.vary)

    def test_notebook_export(self):
        notebook = v4.new_notebook(cells=[v4.new_markdown_cell('# Security smoke test')])
        body, _ = HTMLExporter().from_notebook_node(notebook)
        self.assertIn('Security smoke test', body)

    def test_classifier_pipeline(self):
        pipeline = create_pipeline(MultinomialNB())
        texts = ['verified science evidence', 'fabricated rumour hoax',
                 'confirmed research report', 'invented gossip fiction']
        pipeline.fit(texts, [1, 0, 1, 0])
        self.assertEqual(pipeline.predict_proba(['science research']).shape, (1, 2))


if __name__ == '__main__':
    unittest.main()
