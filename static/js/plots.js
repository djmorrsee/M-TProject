// The front end is subject to a rework                      //
// Data formats have changed, breaking all these functions   //
// Shoul take full advantage of the new REST API             //

$.jqplot.config.enablePlugins = true;

$(document).ready(function () {

  URL = '/all/'
  $.ajax({url:URL})
    .done(function (data) {
      parsed_data = JSON.parse(data)
      var c = parsed_data.length

      lines = []

      for (var i = 0; i < c; ++i) {
        dataset = parsed_data[i]
        generated_lines = CreateLinesForModule(dataset)

        lines.push(generated_lines[0])
        lines.push(generated_lines[1])
      }

      var options = GetPlotDict()
      $.jqplot('test-chart', lines, options);
    })
});

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




function FillTable (d) {
  readings = []
  for (var m_key in d) {
    var module = d[m_key]
    var light = module['light']
    var temp = module['temp']

    var light_v = light['ys'][0]
    var temp_v = temp['ys'][0]

    readings.push(GenerateReadingHTML(m_key, temp_v, light_v))
  }
  $("#reading-table").append(readings)
}

function BuildPlot (d) {
  lines = []
  for(var m_key in d) {

    var module = d[m_key]
    var light = module['light']
    var temp = module['temp']

    var light_line = []
    var temp_line = []

    for(var i = 0; i < light['ys'].length; ++i) {

      var light_point = [light['xs'][i] * 1000, light['ys'][i]]
      var temp_point = [temp['xs'][i] * 1000, temp['ys'][i]]

      light_line.push(light_point)
      temp_line.push(temp_point)

    }

    lines.push(light_line)
    lines.push(temp_line)

  }

  var options = GetPlotDict()
  $.jqplot('test-chart', lines, options);
}

function GenerateReadingHTML (m_key, temp, light) {

  var keyString = "<div class='col-xs-3'><p>" + m_key.toString() + "</p></div>"
  var tempString = "<div class='col-xs-4'><p>" + temp.toFixed(1) + " degrees F</p></div>"
  var lightString = "<div class='col-xs-4'><p>" + light.toFixed(1) + "% </p></div>"
  return keyString + tempString + lightString
}
