function GetPlotDict () {
  console.log('Building Graph Dictionary')
  return {
    title:'Temp/Light Readings',
    titleOptions:{
      fontSize:'32pt',
    },

    seriesColors:['#F00', '#00F'],

    axesDefaults : FormatAxesDefaults(),
    axes:FormatAxes(),
    grid:FormatGrid(),


    seriesDefaults:FormatSeriesDefaults(),
    series:FormatSeries(),

    cursor:FormatCursor(),
  }
}

function FormatGrid () {
  return {
    background:"#FFF",
    shadowAlpha:0,
    borderWidth:1,
    borderColor:"#000",
    gridLineColor:"#000"
  }
}

function FormatAxesDefaults () {
  return {
    syncTicks:true,
    useSeriesColor:true,

    pad:1.1,

    tickRenderer : $.jqplot.CanvasAxisTickRenderer,
    tickOptions : {
      fontSize:'10pt',
      markSize:10
    },

    labelOptions : {
      fontSize:'16pt',
      fontFamily:'Georgia, Serif'
    }
  }
}

function FormatAxes () {
  return {
    xaxis:
    {
      renderer:$.jqplot.DateAxisRenderer,
      tickOptions: {
        formatString:'%#I:%M:%S'
      },
      show:true,
      label:'Time',
    },
    yaxis:
    {
      show:true,
      syncTicks:true,

      label:'Temperature',
      labelRenderer:$.jqplot.CanvasAxisLabelRenderer,
      tickOptions: {
        formatString:'%.0f',
      },
    },

    y2axis:
    {
      show:true,
      syncTicks:true,

      label:'Light Intensity',
      labelRenderer:$.jqplot.CanvasAxisLabelRenderer,
      tickOptions: {
        formatString:'%.0f'
      },
      labelOptions:{
        angle:90
      }
    }
  }
}

function FormatSeriesDefaults () {
  return {

    lineWidth:2,
    markerOptions:
    {
      show:true,
      size:4,
      lineWidth:2
    },
    shadow:true,
    shadowAngle: 45,
    shadowOffset: .25,
    shadowDepth: 5,
    shadowAlpha: 1,
    rendererOptions: {
      smooth:true
    }
  }
}

function FormatSeries () {
  function _FormatSeries(isTempLine) {
    if (isTempLine) {
      return {
        yaxis:'yaxis',
      }
    } else {
      return {
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
    tooltipFadeSpeed:'def',
    bringSeriesToFront:true
  }
}
