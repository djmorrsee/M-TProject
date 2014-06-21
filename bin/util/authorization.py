
auth_ids = []

def BuildAuthIDs():
	auth_file = open('auth_file.txt', 'r')

	auth_ids = []
	for _id in auth_file.readlines():
		auth_ids.append()

	auth_file.close()

def VerifyAuthData(data):
	return data.keys() == ["auth_id"]

def VerifyModuleData(data):
	return data.keys() == ["module_auth_id", "module_id", "reading"]

def AuthorizeAuthData(data):
	return data["auth_id"] in auth_ids

BuildAuthIDs()
