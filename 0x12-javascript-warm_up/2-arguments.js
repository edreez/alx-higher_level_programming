#!/usr/bin/node
'use strict';
let w = process.argv.length;
if (w == 2) {
	  console.log('No argument');
} else if (w == 3) {
	  console.log('Argument found');
} else {
	  console.log('Arguments found');
}
