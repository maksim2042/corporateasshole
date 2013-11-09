      // Diary: appetite block
      $('#mood-chart').highcharts('StockChart', {
            chart: {
                alignTicks: false
            },

            rangeSelector: {
                selected: 1
            },

            title: {
                text: 'Mood'
            },

        series : [{
          name : 'Mood',
          data : env.appetite,
          tooltip: {
            valueDecimals: 2
          }
        }]
        });
    

  // Diary: appetite block
    $('#appetite-chart').highcharts('StockChart', {
          chart: {
              alignTicks: false
          },

          rangeSelector: {
              selected: 1
          },

          title: {
              text: 'Appetite'
          },

      series : [{
        name : 'Appetite',
        data : env.appetite,
        tooltip: {
          valueDecimals: 2
        }
      }]
      });

  
  
  
  // Diary: appetite block
    $('#energy-chart').highcharts('StockChart', {
          chart: {
              alignTicks: false
          },

          rangeSelector: {
              selected: 1
          },

          title: {
              text: 'Energy'
          },

      series : [{
        name : 'Energy',
        data : env.energy,
        tooltip: {
          valueDecimals: 2
        }
      }]
      });
  
      // Diary: appetite block
        $('#activity-chart').highcharts('StockChart', {
              chart: {
                  alignTicks: false
              },

              rangeSelector: {
                  selected: 1
              },

              title: {
                  text: 'Energy'
              },

          series : [{
            name : 'Energy',
            data : env.activity,
            tooltip: {
              valueDecimals: 2
            }
          }]
          });   