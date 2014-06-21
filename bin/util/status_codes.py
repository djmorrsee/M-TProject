# Server Response Codes
status_codes = {
	701 : 'Operation Successful',
	702 : 'Operation Unsuccessful',
	703 : 'Bad Data Form',
	704 : 'Bad Authorization ID',
	705 : 'Bad Module ID',
	706 : 'Bad Module Authorization ID'
}

def GetCode (code):
	if not code in status_codes:
		return '**Bad Code**'
	else:
		return status_codes[code]
