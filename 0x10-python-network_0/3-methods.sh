#!/bin/bash
# cURL body size
curl -si -X OPTIONS  "$1" | grep "Allow:" | cut -d " " -f2-
