#!/bin/bash
find . -name "*.pyc" -exec rm '{}' ';'
rm dist/scheduler.zip
rm dist/scheduler.tar.gz
mv src scheduler
tar -pczf dist/scheduler.tar.gz   --exclude=".*" --exclude="/.*" --exclude="/*/.*" --exclude="*.pyc" ./scheduler
mv scheduler/scheduler scheduler/scheduler.py
zip -r dist/scheduler.zip scheduler/[!\.]* -x \*/\.*
mv scheduler/scheduler.py scheduler/scheduler
mv scheduler src