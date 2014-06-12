$.jqplot.config.enablePlugins = true;

$(document).ready(function () {

  URL = '/get_data'

  $.get(URL, function (d) {

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

  }, "json");

});
