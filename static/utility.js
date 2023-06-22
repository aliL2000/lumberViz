const colourDictionary = {
  "open": ["#FF6384", "#FFB1C180"],
  "high": ["#FF63FC", "#F2B1FF80"],
  "low": ["#6B63FF", "#B1B6FF80"],
  "close": ["#63FF92", "#B1FFD780"],
  "adjusted_close": ["#BAB63F", "#D6D98280"],
  "volume": ["#FFB663", "#FFDCB180"]
};

function render_slider(data,field,chart) {
  const dataList = data.map(row => row.date);
  const earliestDate = new Date(dataList[0]);
  const latestDate = new Date(dataList.slice(-1));
  update_displayed_date(earliestDate, latestDate);
  
  $(function() {
    $( "#slider-range" ).slider({
      range: true,
      min: earliestDate.getTime() / 1000,
      max: latestDate.getTime() / 1000,
      step: 86400,
      values: [ earliestDate.getTime() / 1000, latestDate.getTime() / 1000 ],
      slide: function( event, ui ) {
        const newEarlyDate = new Date(ui.values[0] * 1000);
        const newLatestDate = new Date(ui.values[1] * 1000);
        update_displayed_date(newEarlyDate,newLatestDate);
        chart.destroy();
        const newDataSet = data.filter(row => new Date(row.date) >= newEarlyDate && new Date(row.date) <= newLatestDate);
        chart = render_graph(newDataSet,field);
      }
    });
  });
}

function update_displayed_date(earliestDate, latestDate) {
  //This will update the displayed value of the amount component, which is the date string
  $( "#amount" ).val(earliestDate.toDateString() + " - " + latestDate.toDateString());
}

function render_graph(data, field) {
    const dataList = data.map(row => [row.date.slice(0, 10), row.value]);
    const graph = document.getElementById('transaction_graph');

    return new Chart(graph, {
      type: 'line',
      data: {
        labels: dataList.map(dateValuePair => dateValuePair[0]),
        datasets: [{
          label: field[0].toUpperCase() + field.slice(1),
          data: dataList.map(dateValuePair => dateValuePair[1]),
          fill: true,
          borderColor: colourDictionary[field][0],
          backgroundColor: colourDictionary[field][1]
        }],
      }
    }
  );

}
