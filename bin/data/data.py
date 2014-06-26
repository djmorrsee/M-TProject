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
	m_data.update({'reading_count':len(readings) or None})

	light = []
	temp = []
	times = []

	for r in readings:
		light.append(IntToLight(r.light))
		temp.append(IntToTemp(r.temp))
		times.append(r.time_stamp)

	m_data.update({'temperature':temp})
	m_data.update({'light':light})
	m_data.update({'times':times})

	return m_data
