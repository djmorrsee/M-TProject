import os

auth_ids = []

def BuildAuthIDs():
	this_directory = os.path.dirname(__file__)

	with open(os.path.join(this_directory, 'auth_file.txt'), 'r') as auth_file:

		auth_ids = []
		for _id in auth_file.readlines():
			auth_ids.append(_id)

		auth_file.close()

def VerifyAuthData(data):
	return data.keys() == ["auth_id"]

def VerifyModuleData(data):
	return data.keys() == ["module_auth_id", "module_id", "reading"]

def AuthorizeAuthData(data):
	return data["auth_id"] in auth_ids

def HashModuleID(m_id):
	m_id = int(m_id)
	h_id = ((m_id >> 16) ^ m_id) * 0x45d9f3b
	h_id = ((h_id >> 16) ^ h_id) * 0x45d9f3b
	h_id = ((h_id >> 16) ^ h_id)
	return h_id

BuildAuthIDs()
