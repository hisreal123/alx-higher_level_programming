#!/usr/bin/node
/* global $ */
//  a jQuery script that updates the text color of the <header> element to red (#FF0000):
$(document).ready(() => {
  $('DIV#red_header').on({
    click: function () {
      $(this).css('color', '#FF0000');
    }
  });
});
