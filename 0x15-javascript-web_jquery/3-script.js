#!/usr/bin/node
/* global $ */

//   a JavaScript script that adds the class red to the <header>
//   element when the user clicks on the tag DIV#red_header
$(document).ready(() => {
  $('DIV#red_header').addClass('red');
});
