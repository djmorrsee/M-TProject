#Copyright (C) 2014 Andrey Shprengel <andrey.shprengel@colorado.edu> Daniel Morrissey <daniel.morrissey@colorado.edu>
#This work is free. You can redistribute it and/or modify it under the
#terms of the Do What The Fuck You Want To Public License, Version 2,
#as published by Sam Hocevar. See the COPYING file for more details.
var FONT_CONST = 'Arial, Sans-Serif'
var FONT_COLOR_01 = '#000'

function GetPlotDict (module_num) {
  console.log('Building Graph Dictionary For ' + module_num.toString() + ' Modules')
  return {
    title:FormatTitle(),

    axesDefaults : FormatAxesDefaults(),
    axes:FormatAxes(),
    grid:FormatGrid(),


    seriesDefaults:FormatSeriesDefaults(),
    series:FormatSeries(module_num),

    cursor:FormatCursor(),
    legend:FormatLegend(),
  }
}

function FormatTitle () {
  return {
    text:'24 Hour Temperature/Light Readings',
    fontSize:'24pt',
    fontFamily:FONT_CONST,
    textColor:FONT_COLOR_01,
  }
}

function FormatGrid () {
  return {
    background:"#FFF",
    borderColor:"#000",
    gridLineColor:"#000",
  }
}

function FormatAxesDefaults () {
  return {
    syncTicks:true,

    pad:1.1,

    tickRenderer : $.jqplot.CanvasAxisTickRenderer,
    tickOptions : {
      fontSize:'12pt',
      textColor:FONT_COLOR_01,
      formatString:'%.0f'
    },

    labelOptions : {
      fontSize:'24pt',
      fontFamily:FONT_CONST,
      textColor:FONT_COLOR_01,

    }
  }
}

function FormatAxes () {
  return {
    xaxis:
    {
      label:'Time',
      renderer:$.jqplot.DateAxisRenderer,

      show:true,
      tickOptions: {
        formatString:'%#I:%M:%S',
      },
    },

    yaxis:
    {
      show:true,
      label:'Temperature (degrees F)',
      labelRenderer:$.jqplot.CanvasAxisLabelRenderer,
      min:20,
      max:150,
      autoscale:true
    },

    y2axis:
    {
      min:0,
      max:100,
      show:true,
      label:'Light Intensity (%)',
      labelRenderer:$.jqplot.CanvasAxisLabelRenderer,

      tickOptions:{
        showGridline:false,
      },
      labelOptions:{
        angle:90,

      },

    }
  }
}

function FormatSeriesDefaults () {
  return {

    markerOptions:
    {
      show:true,
      size:4,
      lineWidth:2
    },

    rendererOptions: {
      smooth:true
    }
  }
}

// Legend Label Should be M_ID
function FormatSeries (module_num) {
  Math.seedrandom("djmorrsee<3elephants")

  function _FormatSeries(isTempLine, mod_num, color) {
    var axis_label = ((isTempLine) ? 'yaxis' : 'y2axis')
    var label_label = mod_num.toString() + ((isTempLine) ? ' Temperature' : ' Light Intensity')

    if (isTempLine) {
      for (var i = 0; i < color.length; ++i) {
        color[i] = parseInt(color[i] / 2)
      }
    }

    var color_label = 'rgba(' + color[0] + ', ' + color[1] + ', ' + color[2] + ', 1)'

    return {
      label:label_label,
      yaxis:axis_label,
      color:color_label
    }
  }

  series = []
  var x, y, z, c
  for (i = 0; i < module_num * 2; ++i) {
    if (i % 2 == 0) {
      x = parseInt(Math.random() * 255)
      y = parseInt(Math.random() * 255)
      z = parseInt(Math.random() * 255)
      c = [x, y, z]
    }


    series.push(_FormatSeries(i % 2 == 1, parseInt(i / 2) + 1, c))
  }
  return series
}

function FormatCursor () {
  return {
    showTooltip:false,
    showVerticalLine:true,
    showHorizontalLine:true,
    intersectionThreshold:10,
    zoom:true,
    constrainZoomTo:'x'
  }
}

function FormatHighlighter () {
  return {
    show:true,
    fadeTooltip:false,
  }
}

function FormatLegend () {
  return {
    show:true,
    location:'n',
    placement:'outsideGrid',
    renderer:$.jqplot.EnhancedLegendRenderer,
    fontSize:'12pt',
    textColor:FONT_COLOR_01,
  }
}
