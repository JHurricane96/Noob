#!/bin/bash
mkdir -p ~/nub
for counter in {1..100}; do
	mkdir -p ~/nub/folder$counter
	touch ~/nub/folder$counter/folder$counter.txt
done
chmod 700 ~/nub