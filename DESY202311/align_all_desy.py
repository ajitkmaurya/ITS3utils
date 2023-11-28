import argparse
import glob
import re
import os

# data_folder = '/home/akumar/ce65v2_ana_soft/data/beam'
data_folder = '/home/akumar/ce65v2_ana_soft/data/desy/beam'
corry_bin = '/home/akumar/ce65v2_ana_soft/corryvreckan/bin/corry'
config_path = 'config_files/'
corry_config_prealign_tel = config_path + 'prealign_tel_pcb02_desy.conf'
corry_config_align_tel = config_path + 'align_tel_pcb02_desy.conf'
corry_config_prealign_dut = config_path + 'prealign_dut_pcb02_desy.conf'
corry_config_align_dut = config_path + 'align_dut_pcb02_desy.conf'
geo_path = '../geo_files/'
output_dir = '/home/akumar/ce65v2_ana_soft/analysis/beam/align_out'

parser = argparse.ArgumentParser(description='corry alignment wrapper')
# parser.add_argument('-r', help='run number', default=5121205)
parser.add_argument('-r', help='run number', required=True)
parser.add_argument('-g', help='new geoid number', required=True)
parser.add_argument('-o', help='old geoid number. If specified telescope alignment with given geoid will be used and only DUT will be aligned.')
parser.add_argument('-n', help='number of events', default = -1)
parser.add_argument('-hv', help='number of events', default = 10)


args = parser.parse_args()

data_in_files = glob.glob(data_folder + '/*.raw')
# print('available raws: ', data_in_files)

current_run = args.r
hv = args.hv
number_of_events = args.n
print(hv, current_run)

output_file = f'analysis_run{current_run}.root'

current_file = ''
for f in data_in_files:
    m = re.search(f'ce65v2_pcb02_hv10_beam4gev_run482104543_231128104549.raw', f)
    # m = re.search(f'ce65v2_pcb08_hv10_beam5GeV_run481213135_231127213141.raw', f)
    # m = re.search(f'ce65v2_pcb08_hv10_beam_run481181643_231127181650.raw', f)
    if m:
        current_file = f
    else:
       # print("file not found")
       pass

print(f'processing, file: {current_file}')
rough_geo = geo_path + f'{args.g}.geo'
prealign_tel_geo_itr01 = geo_path + f'{args.g}_{args.r}_gbl_3gev_tel_prealigned_itr1.geo'
prealign_tel_geo = geo_path + f'{args.g}_{args.r}_gbl_3gev_tel_prealigned.geo'
align_tel_geo_it01 = geo_path + f'{args.g}_{args.r}_gbl_3gev_tel_aligned_itr1.geo'
align_tel_geo_it02 = geo_path + f'{args.g}_{args.r}_gbl_3gev_tel_aligned_itr2.geo'
align_tel_geo_it03 = geo_path + f'{args.g}_{args.r}_gbl_3gev_tel_aligned_itr3.geo'
align_tel_geo_it04 = geo_path + f'{args.g}_{args.r}_gbl_3gev_tel_aligned_itr4.geo'
align_tel_geo_it05 = geo_path + f'{args.g}_{args.r}_gbl_3gev_tel_aligned_itr5.geo'
align_tel_geo = geo_path + f'{args.g}_{args.r}_gbl_3gev_tel_aligned.geo'
prealign_dut_geo = geo_path + f'{args.g}_{args.r}_gbl_3gev_dut_prealigned.geo'
align_dut_geo_it01 = geo_path + f'{args.g}_{args.r}_gbl_3gev_dut_aligned_itr1.geo'
align_dut_geo_it02 = geo_path + f'{args.g}_{args.r}_gbl_3gev_dut_aligned_itr2.geo'
align_dut_geo_it03 = geo_path + f'{args.g}_{args.r}_gbl_3gev_dut_aligned_itr3.geo'
align_dut_geo = geo_path + f'{args.g}_{args.r}_gbl_3gev_dut_aligned.geo'
print(args.o)
if not args.o:

    print('\n\n##################################################### prealigning telescope ####################################')
    corry_cmd = f'{corry_bin} -c {corry_config_prealign_tel} -o number_of_events={args.n} -o output_directory={output_dir} -o detectors_file={rough_geo} -o detectors_file_updated={prealign_tel_geo_itr01} -o histogram_file={args.g}_{args.r}_tel_prealigned_itr01.root -o EventLoaderEUDAQ2.file_name={current_file}'
    os.system(corry_cmd)

    print('\n\n##################################################### prealigning telescope ####################################')
    corry_cmd = f'{corry_bin} -c {corry_config_prealign_tel} -o number_of_events={args.n} -o output_directory={output_dir} -o detectors_file={prealign_tel_geo_itr01} -o detectors_file_updated={prealign_tel_geo} -o histogram_file={args.g}_{args.r}_tel_prealigned.root -o EventLoaderEUDAQ2.file_name={current_file}'
    os.system(corry_cmd)
    
    print('\n##################################################### aligning telescope: ITR1 ####################################')
    corry_cmd = f'{corry_bin} -c {corry_config_align_tel} -o number_of_events={args.n} -o output_directory={output_dir} -o detectors_file={prealign_tel_geo} -o detectors_file_updated={align_tel_geo_it01} -o histogram_file={args.g}_{args.r}_tel_aligned_it01.root -o EventLoaderEUDAQ2.file_name={current_file}'
    os.system(corry_cmd)

    print('\n##################################################### aligning telescope: ITR2 ####################################')
    corry_cmd = f'{corry_bin} -c {corry_config_align_tel} -o number_of_events={args.n} -o output_directory={output_dir} -o detectors_file={align_tel_geo_it01} -o detectors_file_updated={align_tel_geo_it02} -o histogram_file={args.g}_{args.r}_tel_aligned_it02.root -o EventLoaderEUDAQ2.file_name={current_file}'
    os.system(corry_cmd)

    print('\n##################################################### aligning telescope: ITR3 ####################################')
    corry_cmd = f'{corry_bin} -c {corry_config_align_tel} -o number_of_events={args.n} -o output_directory={output_dir} -o detectors_file={align_tel_geo_it02} -o detectors_file_updated={align_tel_geo_it03} -o histogram_file={args.g}_{args.r}_tel_aligned_it03.root -o EventLoaderEUDAQ2.file_name={current_file}'
    os.system(corry_cmd)

    print('\n##################################################### aligning telescope: ITR4 ####################################')
    corry_cmd = f'{corry_bin} -c {corry_config_align_tel} -o number_of_events={args.n} -o output_directory={output_dir} -o detectors_file={align_tel_geo_it03} -o detectors_file_updated={align_tel_geo_it04} -o histogram_file={args.g}_{args.r}_tel_aligned_itr04.root -o EventLoaderEUDAQ2.file_name={current_file}'
    os.system(corry_cmd)

    print('\n##################################################### aligning telescope: ITR Final ####################################')
    corry_cmd = f'{corry_bin} -c {corry_config_align_tel} -o number_of_events={args.n} -o output_directory={output_dir} -o detectors_file={align_tel_geo_it04} -o detectors_file_updated={align_tel_geo_it05} -o histogram_file={args.g}_{args.r}_tel_aligned.root -o EventLoaderEUDAQ2.file_name={current_file}'
    os.system(corry_cmd)

    print('\n##################################################### aligning telescope: ITR Final ####################################')
    corry_cmd = f'{corry_bin} -c {corry_config_align_tel} -o number_of_events={args.n} -o output_directory={output_dir} -o detectors_file={align_tel_geo_it05} -o detectors_file_updated={align_tel_geo} -o histogram_file={args.g}_{args.r}_tel_aligned.root -o EventLoaderEUDAQ2.file_name={current_file}'
    os.system(corry_cmd)



    print('\n##################################################### prealigning DUT ####################################')
    corry_cmd = f'{corry_bin} -c {corry_config_prealign_dut} -o number_of_events={args.n} -o output_directory={output_dir} -o detectors_file={align_tel_geo} -o detectors_file_updated={prealign_dut_geo} -o histogram_file={args.g}_{args.r}_dut_prealigned.root -o EventLoaderEUDAQ2.file_name={current_file}'
    os.system(corry_cmd)

    print('\n##################################################### aligning DUT: ITR1 ####################################')
    corry_cmd = f'{corry_bin} -c {corry_config_align_dut} -o number_of_events={args.n} -o output_directory={output_dir} -o detectors_file={prealign_dut_geo} -o detectors_file_updated={align_dut_geo_it01} -o histogram_file={args.g}_{args.r}_dut_aligned_itr01.root -o EventLoaderEUDAQ2.file_name={current_file}'
    os.system(corry_cmd)

    print('\n##################################################### aligning DUT: ITR2 ####################################')
    corry_cmd = f'{corry_bin} -c {corry_config_align_dut} -o number_of_events={args.n} -o output_directory={output_dir} -o detectors_file={align_dut_geo_it01} -o detectors_file_updated={align_dut_geo_it02} -o histogram_file={args.g}_{args.r}_dut_aligned_itr02.root -o EventLoaderEUDAQ2.file_name={current_file}'
    os.system(corry_cmd)

    print('\n##################################################### aligning DUT: ITR3 ####################################')
    corry_cmd = f'{corry_bin} -c {corry_config_align_dut} -o number_of_events={args.n} -o output_directory={output_dir} -o detectors_file={align_dut_geo_it02} -o detectors_file_updated={align_dut_geo_it03} -o histogram_file={args.g}_{args.r}_dut_aligned_itr03.root -o EventLoaderEUDAQ2.file_name={current_file}'
    os.system(corry_cmd)

    print('\n##################################################### aligning DUT: ITR Final ####################################')
    corry_cmd = f'{corry_bin} -c {corry_config_align_dut} -o number_of_events={args.n} -o output_directory={output_dir} -o detectors_file={align_dut_geo_it03} -o detectors_file_updated={align_dut_geo} -o histogram_file={args.g}_{args.r}_dut_aligned.root -o EventLoaderEUDAQ2.file_name={current_file}'
    os.system(corry_cmd)

else:
    pass
