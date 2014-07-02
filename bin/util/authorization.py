#Copyright (C) 2014 Andrey Shprengel <andrey.shprengel@colorado.edu> Daniel Morrissey <daniel.morrissey@colorado.edu>
#This work is free. You can redistribute it and/or modify it under the
#terms of the Do What The Fuck You Want To Public License, Version 2,
#as published by Sam Hocevar. See the COPYING file for more details.
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
