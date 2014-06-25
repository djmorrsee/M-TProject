""" Reading Data

This file contains methods to ensure data format conformation
"""

from bin.data.conversions import IntToTemp, IntToLight

def ReadingsToHistoryJSON(m_id, readings):
    """ Helper method to build properly formated JSON

    Conforms to module_history_reading.json

    Args:
        m_id (int) : The module ID for these readings
        readings (list) : A list of ModuleReading's

    """
    m_data = {}
    m_data.update({'module_id':m_id})
    if readings == None:
        m_data.update({'reading_count':0})
    else:
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
