#!/bin/bash

for p_mig in {0..10}
do
    for i in {1..2}
    do
        P_MIG=$(awk "BEGIN {print 0.05 * $p_mig}")
        echo "$P_MIG"
    done
done