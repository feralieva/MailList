class MailListFileAdapter(object):
	"""docstring for MailListFileAdapter"""
	def __init__(self, mail_list):
		self.mail_list = mail_list
 
	def get_file_name(self):
		return self.mail_list.get_name().replace(" ", "_")
 
	def prepare_for_save(self):
		subscribers = self.mail_list.get_subscribers()
		subscribers = map(lambda t: "{} - {}".format(t[0], t[1]), subscribers)
 
		return sorted(subscribers)
 
	def save(self):
		file_to_save = open(self.get_file_name(), "w")
		contents = "\n".join(self.prepare_for_save())
		file_to_save.write(contents)
		file_to_save.close()