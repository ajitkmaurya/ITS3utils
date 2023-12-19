#! /bin/bash

pcb_no=$1
hv=$2
run=$3

../eudaq/CE65V2Dump.py ../data/ce65v2_pcb${pcb_no}_hv${hv}_noise_run${run}.raw -o pcb${pcb_no}-hv${hv}-noise -e 5000 -n -d --qa
../eudaq/analog_qa_ce65v2.py pcb${pcb_no}-hv${hv}-noise-qa.root -o pcb${pcb_no}_hv${hv}-noisemap --rts --frac 0.9
