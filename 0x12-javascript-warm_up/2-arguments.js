#!/usr/bin/node
import { argv } from 'process';

if(argv[2])
{
    console.log('Argument found');
}
else
{
    console.log('No argument');
}
