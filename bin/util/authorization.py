
auth_ids = [123, 321]

def BuildAuthIDs():
	auth_file = open('auth_file.txt')

def VerifyAuthData(data):
	return data.keys() == ["auth_id"]

def VerifyModuleData(data):
	return data.keys() == ["module_auth_id", "module_id", "reading"]

def AuthorizeAuthData(data):
	return data["auth_id"] in auth_ids

BuildAuthIDs()
