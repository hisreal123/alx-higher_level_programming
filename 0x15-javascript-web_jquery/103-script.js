#!/usr/bin/node
/* global $ */

$(function () {
  function searchCity () {
    $.get('https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22' + $('#city_search').val() + '%22)&format=json', function (data, textStatus) {
      if (textStatus === 'success' && data.query.results !== null) {
        $('#wind_speed').text(data.query.results.channel.wind.speed);
      } else {
        $('#wind_speed').text('Invalid city');
      }
    });
  }
  $('#btn_search').click(searchCity);
  $('#city_search').keypress(function (event) {
    if (event.keyCode === 13) {
      searchCity();
    }
  });
});
