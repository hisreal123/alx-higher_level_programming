#!/usr/bin/node
/* global $ */
// a JavaScript script that adds a <li>
// element to a list when the user clicks on the tag DIV#add_item

$(document).ready(() => {
  $('DIV#update_header').on({
    click: function () {
      $('header').text('New Header !!!');
    }
  });
});
