#Copyright (C) 2014 Andrey Shprengel <andrey.shprengel@colorado.edu> Daniel Morrissey <daniel.morrissey@colorado.edu>
#This work is free. You can redistribute it and/or modify it under the
#terms of the Do What The Fuck You Want To Public License, Version 2,
#as published by Sam Hocevar. See the COPYING file for more details.
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
