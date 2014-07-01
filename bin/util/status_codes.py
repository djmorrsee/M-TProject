status_codes = {
# Server Response Codes
	701:'Operation Successful',
	702:'Operation Unsuccessful',
	703:'Bad Data Form',
	704:'Bad Authorization ID',
	705:'Bad Module ID',
	706:'Bad Module Authorization ID'
}


class StatusCode:
	def Success(self):
		return self.GetCodeString(701)

	def Failure(self):
		return self.GetCodeString(702)

	def BadForm(self):
		return self.GetCodeString(703)

	def BadAuth(self):
		return self.GetCodeString(704)

	def BadMID(self):
		return self.GetCodeString(705)

	def BadMAuth(self):
		return self.GetCodeString(706)

	def GetCodeString(self, code):
		if not code in status_codes:
			return 'BAD CODE'

		return status_codes[code]

SC = StatusCode()
