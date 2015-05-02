import twilio
import unittest
from twilio.rest import TwilioRestClient

#This class needs to run this command to work: $ pip install twilio
class SMS_Sender():
	FROM_PHONE_NUMBER_PROD = "+15208674780"
	# ======================== 	Production credentials	=========================
	account_sid_prod = "AC66c4bbcc65f97595ea05b798e366e92c"
	auth_token_prod  = "f4012b86d339064dbf356978e3ee8967"
	# ======================== 	Test Credentials	=============================
	account_sid_test = "AC4a02c06787cb6792850828af61ce7205"
	auth_token_test  = "1ade2a7aa7ff7be3708082851dcc7f04"
	
	#Method that initialize the values for required behavior
	def __init__(self, from_number="0", testing_mode = True):
		self.testing_mode = True
		self.testing_mode = testing_mode		
		
		if(testing_mode):
			self.from_phone_number = from_number
			self.client = TwilioRestClient(self.account_sid_test, self.auth_token_test)
		else:
			self.from_phone_number = FROM_PHONE_NUMBER_PROD
			self.client = TwilioRestClient(self.account_sid_prod, self.auth_token_prod)
	
	#Method that sends a sms text message to a given number
	def send_sms(self, text_message, send_to_number):
		message = self.client.messages.create(body=text_message,to=send_to_number, from_=self.from_phone_number)
		print("Message send - MessageId = ", message.sid)
		return message
		

#Class that group the JUnit test for SMS_Sender
class SMS_Sender_Test(unittest.TestCase):
	DEFAULT_SENT_TO_NUMBER = "+573154150444"
	DEFAULT_SENT_FROM_NUMBER = "+15005550006"
	DEFAULT_TESTING_MODE = True
		
	#+15005550001	This phone number is invalid.	21212
	def test_from_number_invalid(self):
		try:
			my_sms_client = SMS_Sender("+15005550001", self.DEFAULT_TESTING_MODE)
			response = my_sms_client.send_sms("::: test_from_number_invalid", self.DEFAULT_SENT_TO_NUMBER)
		except twilio.TwilioRestException as e:
			self.assertRaises(twilio.TwilioRestException)
			self.assertEqual(21212, e.code)
		
		
	#+15005550007	This phone number is not owned by your account or is not SMS-capable.	21606
	def test_from_number_not_owned_in_my_account(self):
		try:
			my_sms_client = SMS_Sender("+15005550007", self.DEFAULT_TESTING_MODE)
			response = my_sms_client.send_sms("::: test_from_number_not_owned_in_my_account", self.DEFAULT_SENT_TO_NUMBER)
		except twilio.TwilioRestException as e:
			self.assertRaises(twilio.TwilioRestException)
			self.assertEqual(21606, e.code)
	
	#+15005550008	This number has an SMS message queue that is full.	21611
	def test_from_number_sms_queue_full(self):
		try:
			my_sms_client = SMS_Sender("+15005550008", self.DEFAULT_TESTING_MODE)
			response = my_sms_client.send_sms("::: test_from_number_sms_queue_full", self.DEFAULT_SENT_TO_NUMBER)
		except twilio.TwilioRestException as e:
			self.assertRaises(twilio.TwilioRestException)
			self.assertEqual(21611, e.code)
		
	#+15005550006	This number passes all validation.	No error
	def test_from_number_OK(self):
		my_sms_client = SMS_Sender(self.DEFAULT_SENT_FROM_NUMBER, self.DEFAULT_TESTING_MODE)
		response = my_sms_client.send_sms("::: test_from_number_OK", self.DEFAULT_SENT_TO_NUMBER)
		self.assertIsNotNone(response)
		self.assertIsNotNone(response.sid)
	
	#+15005550001	This phone number is invalid.	21211
	def test_to_number_invalid(self):
		try:
			my_sms_client = SMS_Sender(self.DEFAULT_SENT_FROM_NUMBER, self.DEFAULT_TESTING_MODE)
			response = my_sms_client.send_sms("::: test_to_number_invalid", "+15005550001")
		except twilio.TwilioRestException as e:
			self.assertRaises(twilio.TwilioRestException)
			self.assertEqual(21211, e.code)
		
	#+15005550002	Twilio cannot route to this number.	21612
	def test_to_number_cant_be_routed(self):
		try:
			my_sms_client = SMS_Sender(self.DEFAULT_SENT_FROM_NUMBER, self.DEFAULT_TESTING_MODE)
			response = my_sms_client.send_sms("::: test_to_number_cant_be_routed", "+15005550002")
		except twilio.TwilioRestException as e:
			self.assertRaises(twilio.TwilioRestException)
			self.assertEqual(21612, e.code)
		
	#+15005550003	Your account doesn't have the international permissions necessary to SMS this number.	21408
	def test_to_number_invalid_permissions(self):
		try:
			my_sms_client = SMS_Sender(self.DEFAULT_SENT_FROM_NUMBER, self.DEFAULT_TESTING_MODE)
			response = my_sms_client.send_sms("::: test_to_number_invalid_permissions", "+15005550003")
		except twilio.TwilioRestException as e:
			self.assertRaises(twilio.TwilioRestException)
			self.assertEqual(21408, e.code)
		
	#+15005550004	This number is blacklisted for your account.	21610	
	def test_to_number_in_blacklist(self):
		try:
			my_sms_client = SMS_Sender(self.DEFAULT_SENT_FROM_NUMBER, self.DEFAULT_TESTING_MODE)
			response = my_sms_client.send_sms("::: test_to_number_in_blacklist", "+15005550004")
		except twilio.TwilioRestException as e:
			self.assertRaises(twilio.TwilioRestException)
			self.assertEqual(21610, e.code)
		
	#+15005550009	This number is incapable of receiving SMS messages.	21614	
	def test_to_number_incapable_to_receiving_sms(self):
		try:
			my_sms_client = SMS_Sender(self.DEFAULT_SENT_FROM_NUMBER, self.DEFAULT_TESTING_MODE)
			response = my_sms_client.send_sms("::: test_to_number_in_blacklist", "+15005550009")
		except twilio.TwilioRestException as e:
			self.assertRaises(twilio.TwilioRestException)
			self.assertEqual(21614, e.code)
		
if __name__ == '__main__':
    unittest.main()		

#Run this code to check if sms is sent properly
#my_sms_client = SMS_Sender()
#my_sms_client.send_sms("Mensaje de prueba X", "+573154150444")