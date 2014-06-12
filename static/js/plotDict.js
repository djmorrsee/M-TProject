function GetPlotDict () {
  console.log('Building Graph Dictionary')
  return {
    title:'Temp/Light Readings',
    titleOptions:{
      fontSize:'32pt'
    },

    seriesColors:['#F00', '#00F'],

    axesDefaults : FormatAxesDefaults(),
    axes:FormatAxes(),



    seriesDefaults:FormatSeriesDefaults(),
    series:FormatSeries(),

    cursor:FormatCursor(),
  }
}

function AlternatingYAxisArray () {
  var ar = []
  for (i = 0; i < 20; ++i) {
    if (i % 2 == 1) {
      ar.push({yaxis:'yaxis'})
    } else {
      ar.push({yaxis:'y2axis'})
    }
  }

  return ar
}

function FormatAxesDefaults () {
  return {
    pad:1.1,
    tickRenderer : $.jqplot.CanvasAxisTickRenderer,
    tickOptions : {
      fontSize:'10pt',
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
      label:'Date',
    },
    yaxis:
    {
      show:true,
      label:'Temp',
      labelRenderer:$.jqplot.CanvasAxisLabelRenderer
    },

    y2axis:
    {
      show:true,
      label:'Light',
      labelRenderer:$.jqplot.CanvasAxisLabelRenderer,
      labelOptions:{
        angle:90
      }
    }
  }
}

function FormatSeriesDefaults () {
  return {
    trendline: {
      show:false
    },

    lineWidth:1.5,
    markerOptions:
    {
      show:false
    },
    shadow:true,
    shadowAngle: 45,
    shadowOffset: .25,
    shadowDepth: 5,
    shadowAlpha: 1,
    renderOptions: {
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
    zoom:true
  }
}

function FormatHighlighter () {
  return {
    show:true,
    tooltipFadeSpeed:'def',
    bringSeriesToFront:true
  }
}
