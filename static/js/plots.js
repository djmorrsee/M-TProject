$(document).ready(function () {
  // For Plugins
  $.jqplot.config.enablePlugins = true;

  // Basic JQPlot Syntax
  $.jqplot('test-chart0',  [[[1, 2],[3,5.12],[5,13.1],[7,33.6],[9,85.9],[11,219.9]]],
  {
    cursor:{style:'nw-resize', followMouse:true}
  });

  // Plot with included options
  $.jqplot('test-chart1',  [[[1, 2],[3,5.12],[5,13.1],[7,33.6],[9,85.9],[11,219.9]]],
  { title:'Exponential Line',
    axes:{yaxis:{min:-10, max:240}},
    series:[{color:'#5FAB78'}],
    cursor:{style:'nw-resize', followMouse:true}
  });

  // JQPlot Pluggins
  // Requires addiotional js files
  $.jqplot('test-chart2',  [[[1, 2],[3,5.12],[5,13.1],[7,33.6],[9,85.9],[11,219.9]]],
  { title:'Exponential Line',
    axes:{yaxis:{renderer: $.jqplot.LogAxisRenderer}},
    series:[{color:'#5FAB78'}],
    cursor:{style:'nw-resize', followMouse:true}
  });

  // Customized Plugin
  $.jqplot('test-chart3',  [[[1, 2],[3,5.12],[5,13.1],[7,33.6],[9,85.9],[11,219.9]]],
  { title:'Exponential Line',
    axes:{yaxis:{renderer: $.jqplot.LogAxisRenderer, tickDistribution:'power'}},
    series:[{color:'#5FAB78'}],
    cursor:{style:'nw-resize', followMouse:true}
  });

});
