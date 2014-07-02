#Copyright (C) 2014 Andrey Shprengel <andrey.shprengel@colorado.edu> Daniel Morrissey <daniel.morrissey@colorado.edu>
#This work is free. You can redistribute it and/or modify it under the
#terms of the Do What The Fuck You Want To Public License, Version 2,
#as published by Sam Hocevar. See the COPYING file for more details.
$.jqplot.config.enablePlugins = true;

// Document Ready, Perform DOM Actions
$(document).ready(function () {

  URL = '/all/'
  $.ajax({url:URL})
    .done(function (data) {
      parsed_data = JSON.parse(data)
      var c = parsed_data.length

      lines = []

      for (var i = 0; i < c; ++i) {
        dataset = parsed_data[i]
        CreateTableEntry(dataset)

        generated_lines = CreateLinesForModule(dataset)

        lines.push(generated_lines[0])
        lines.push(generated_lines[1])
      }

      var options = GetPlotDict(c)
      $.jqplot('test-chart', lines, options);

      // The plot will not draw correctly if the panel is hidden //
      $('#hist-panel').collapse('hide')

    })


  var hist_showing = false;
  $("#hist-btn").click(function () {
    if (hist_showing) {
      // Do Nothing
    } else {
      $('#hist-panel').collapse('toggle')
      $('#current-panel').collapse('toggle')
      hist_showing = !hist_showing
    }
  });

  $("#current-btn").click(function () {
    if (hist_showing) {
      $('#hist-panel').collapse('toggle')
      $('#current-panel').collapse('toggle')
      hist_showing = !hist_showing
    } else {
      // Do Nothing
    }
  });

});




// Defined Functions
function CreateTableEntry(m_data) {
  var m_id = m_data['module_id']
  var count = m_data['reading_count']

  if (count > 0) {
    var light = m_data['light'][0]
    var temp = m_data['temperature'][0]
    var time = m_data['times'][0] * 1000
    var r_html = GenerateReadingHTML(m_id, temp, light, time)
    // Inject it into our table //
    $("#reading-table").append(r_html)
  }
}

function CreateLinesForModule(m_data) {
  var m_id = m_data['module_id']

  var count = m_data['reading_count']

  var temp_array = m_data['temperature']
  var light_array = m_data['light']
  var time_array = m_data['times']

  var light_line = []
  var temp_line = []

  for (var c = 0; c < count; ++c) {

    var time_stamp = time_array[c] * 1000
    var light_point = [time_stamp, light_array[c]]
    var temp_point = [time_stamp, temp_array[c]]

    light_line.push(light_point)
    temp_line.push(temp_point)

  }
  return [light_line, temp_line]
}

function GenerateReadingHTML (m_key, temp, light, time) {

  var keyString = "<div class='col-xs-3'><p>" + m_key.toString() + "</p></div>"
  var tempString = "<div class='col-xs-3'><p>" + temp.toFixed(1) + " degrees F</p></div>"
  var lightString = "<div class='col-xs-3'><p>" + light.toFixed(1) + "% </p></div>"

  var date = new Date(time)
  var day = date.getDate()
  var hour = date.getHours()
  var minute = date.getMinutes()
  var second = date.getSeconds()



  var timeString = "<div class='col-xs-3'><p>" + date.toLocaleTimeString() + " </p></div>"

  return keyString + tempString + lightString + timeString
}
