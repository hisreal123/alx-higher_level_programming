#!/usr/bin/node
/* global $ */
// A JavaScript script that toggles the class of the <header>
// element when the user clicks on the tag DIV#toggle_header:

let addOrRemove = false;

$(document).ready(() => {
  $('DIV#toggle_header').on({
    click: function () {
      if (!addOrRemove) {
        $('header').removeClass('green').addClass('red');
      } else {
        $('header').removeClass('red').addClass('green');
      }
      addOrRemove = !addOrRemove; // Toggle the variable for next click
    }
  });
});
