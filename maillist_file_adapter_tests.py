from maillist import MailList
from maillist_file_adapter import MailListFileAdapter
import unittest
 
 
class MailListFileAdapterTest(unittest.TestCase):
	"""docstring for MailListFileAdapterTest"""
	def setUp(self):
	self.m = MailList("Hack Bulgaria")
	self.m.add_subscriber("Rado", "rado@rado")
	self.m.add_subscriber("Ivan", "ivan@ivan")
 
	self.maillist_adapter = MailListFileAdapter(self.m)
 
	def test_get_file_name(self):
	self.assertEqual("Hack_Bulgaria", self.maillist_adapter.get_file_name())
 
	def test_prepare_for_save(self):
	expected = sorted(["Rado - rado@rado", "Ivan - ivan@ivan"])
 
	self.assertEqual(expected, self.maillist_adapter.prepare_for_save())
if __name__ == '__main__':
unittest.main()