#!/usr/bin/node
import { argv } from 'process';

if (argv[3]) {
  console.log('Arguments found');
} else if (argv[2]) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
