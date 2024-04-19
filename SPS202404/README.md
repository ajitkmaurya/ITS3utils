The analysis can be run using the https://github.com/Edler1/UZH_CE65_Documentation/tree/main repository:

First, start the docker container using [run_container.sh](https://github.com/Edler1/UZH_CE65_Documentation/blob/main/testbeam_analysis/run_container.sh).

Inside docker, you still may need to install tqdm in the container using
```
pip install tqdm
```

Then put the data files into ITS3utils/SPS202404/data/<CHIPNAME> and run using 
```
sh UZH_CE65_Documentation/testbeam_analysis/run_tb_analysis.sh
```
you can give an optional .txt file with chip-specific run settings as
```
sh UZH_CE65_Documentation/testbeam_analysis/run_tb_analysis_new.sh UZH_CE65_Documentation/testbeam_analysis/params/GAP225SQ_SPS.txt
```
