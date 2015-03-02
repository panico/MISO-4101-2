from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.core import mail


class CorreoTest(TestCase):    
    def test_enviarGmail(self):
        # Send message.
        mail.send_mail('Correo de pruebas', 'Here is the message.',
            'mysmarthome4101@gmail.com', ['jhonyt37@gmail.com'],
            fail_silently=False)

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Correo de pruebas')
