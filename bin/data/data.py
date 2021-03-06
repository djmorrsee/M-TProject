#Copyright (C) 2014 Andrey Shprengel <andrey.shprengel@colorado.edu> Daniel Morrissey <daniel.morrissey@colorado.edu>
#This work is free. You can redistribute it and/or modify it under the
#terms of the Do What The Fuck You Want To Public License, Version 2,
#as published by Sam Hocevar. See the COPYING file for more details.
""" Reading Data

This file contains methods to ensure data format conformation
"""

from bin.data.conversions import IntToTemp, IntToLight

def ReadingsToHistoryJSON(m_id, readings):
	""" Helper method to build properly formated JSON

	Conforms to module_history_reading.json

	:param m_id: The module ID for these readings
	:type m_id: int

	:param readings:A list of ModuleReadings
	:type readings: list [ ]

	:returns: JSON Dictionary -- Formatted for browser consumption
	"""
	m_data = {}
	m_data.update({'module_id':m_id})

	light = []
	temp = []
	times = []

	if readings == None:
			m_data.update({'reading_count':0})
	else:
			m_data.update({'reading_count':len(readings)})

			for r in readings:
				light.append(IntToLight(r.light))
				temp.append(IntToTemp(r.temp))
				times.append(r.time_stamp)

	m_data.update({'temperature':temp})
	m_data.update({'light':light})
	m_data.update({'times':times})

	return m_data
