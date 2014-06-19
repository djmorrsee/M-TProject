var FONT_CONST = 'Arial, Sans-Serif'
var FONT_COLOR_01 = '#000'

function GetPlotDict () {
  console.log('Building Graph Dictionary')
  return {
    title:FormatTitle(),


    seriesColors:['#F00', '#00F'],

    axesDefaults : FormatAxesDefaults(),
    axes:FormatAxes(),
    grid:FormatGrid(),


    seriesDefaults:FormatSeriesDefaults(),
    series:FormatSeries(),

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
    useSeriesColor:true,

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

function FormatSeries () {
  function _FormatSeries(isTempLine) {
    if (isTempLine) {
      return {
        label:'Temp',
        yaxis:'yaxis',

      }
    } else {
      return {
        label:'Light',
        yaxis:'y2axis',
      }
    }
  }
  series = []
  for (i = 0; i < 20; ++i) {
    series.push(_FormatSeries(i % 2 == 1))
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
    location:'e',
    placement:'outsideGrid',
    renderer:$.jqplot.EnhancedLegendRenderer,
    rowSpacing:'2em',
    border:'none',
    marginBottom:'75px',
    fontSize:'12pt',
    textColor:FONT_COLOR_01,
  }
}
