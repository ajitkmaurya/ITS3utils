#! /bin/bash

pcb_no=$1
hv=$2
run=$3

/home/akumar/ce65v2_ana_soft/ITS3utils/eudaq/CE65V2Dump.py /home/akumar/ce65v2_ana_soft/data/desy/noise/ce65v2_pcb${pcb_no}_hv${hv}_noise_run${run}.raw -o pcb${pcb_no}-hv${hv}-noise -e 5000 -n -d --qa
/home/akumar/ce65v2_ana_soft/ITS3utils/eudaq/analog_qa_ce54v2.py pcb${pcb_no}-hv${hv}-noise-qa.root -o pcb${pcb_no}_hv${hv}-noisemap --rts --frac 0.9

#../../../ITS3utils/eudaq/CE65V2Dump.py ../../../data/desy/noise/ce65v2_pcb03_hv10_noise_run483174912_231129175816.raw -o pcb03-hv10-noise -e 5000 -n -d --qa
#../../../ITS3utils/eudaq/analog_qa_ce54v2.py pcb03-hv10-noise-qa.root -o pcb03_hv10-noisemap --rts --frac 0.9

#../../../ITS3utils/eudaq/CE65V2Dump.py ../../../data/desy/noise/ce65v2_pcb18_hv10_noise_run484085812_231130090903.raw -o pcb18-hv10-noise -e 5000 -n -d --qa
#../../../ITS3utils/eudaq/analog_qa_ce54v2.py pcb18-hv10-noise-qa.root -o pcb18_hv10-noisemap --rts --frac 0.9
