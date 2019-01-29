#!/usr/bin/env node
'use strict';

const importJsx = require('import-jsx');
const {h, render} = require('ink');
const meow = require('meow');

const Ui = importJsx('./ui');

const cli = meow(`
	Usage
	  $ test-ink [input]

	Options
	  --stop  When to stop iteration [Default: 10]
`);

render(h(Ui, cli.flags));
