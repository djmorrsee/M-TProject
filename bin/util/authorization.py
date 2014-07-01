import os

auth_ids = []

def BuildAuthIDs():
	this_directory = os.path.dirname(__file__)
	auth_file = os.path.join(this_directory, 'auth_file.txt')
	with open(auth_file, 'r') as f:
		for _id in f.readlines():
			if(_id != ''):
				auth_ids.append(int(_id)) # Note int
		f.close()


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
