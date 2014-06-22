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
      for (var i = 0; i < c; ++i) {
        dataset = parsed_data[i]
        console.log(dataset['module_id'])
      }
    })
});

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
