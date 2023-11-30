#Geometry file for CE65 for May 2022 beam test at PS-CERN
#Telescope B1, https://twiki.cern.ch/twiki/bin/viewauth/ALICE/ITS3WP3PS2022May

[ALPIDE_0]
type = "ALPIDE"
position = 0um,0um,0mm
number_of_pixels = 1024,512
pixel_pitch = 29.24um, 26.88um
spatial_resolution = 5.00um, 5.00um
time_resolution = 2us
material_budget = 0.001
coordinates = "cartesian"
orientation_mode = "xyz"
# orientation = 180deg, 180deg, 0deg
mask_file="/home/akumar/ce65v2_ana_soft/analysis/beam/mask_file/ref-plan0.txt"
orientation = 0deg, 0deg, 0deg
role = "reference"

[ALPIDE_1]
type = "ALPIDE"
position = 0um,0um,25mm
number_of_pixels = 1024,512
pixel_pitch = 29.24um, 26.88um
spatial_resolution = 5.00um, 5.00um
time_resolution = 2us
material_budget = 0.0005
coordinates = "cartesian"
orientation_mode = "xyz"
# orientation = 180deg, 180deg, 0deg
mask_file="/home/akumar/ce65v2_ana_soft/analysis/beam/mask_file/ref-plan1.txt"
orientation = 0deg, 0deg, 0deg

[ALPIDE_2]
type = "ALPIDE"
position = 0um,0um,50mm
number_of_pixels = 1024,512
pixel_pitch = 29.24um, 26.88um
spatial_resolution = 5.00um, 5.00um
time_resolution = 2us
material_budget = 0.0005
coordinates = "cartesian"
orientation_mode = "xyz"
# orientation = 180deg, 180deg, 0deg
mask_file="/home/akumar/ce65v2_ana_soft/analysis/beam/mask_file/ref-plan2.txt"
orientation = 0deg, 0deg, 0deg

[ALPIDE_3]
type = "ALPIDE"
position = 0um,0um,150mm
number_of_pixels = 1024,512
pixel_pitch = 29.24um, 26.88um
spatial_resolution = 5.00um, 5.00um
time_resolution = 2us
material_budget = 0.0005
coordinates = "cartesian"
orientation_mode = "xyz"
# orientation = 180deg, 180deg, 0deg
mask_file="/home/akumar/ce65v2_ana_soft/analysis/beam/mask_file/ref-plan3.txt"
orientation = 0deg, 0deg, 0deg

[ALPIDE_4]
type = "ALPIDE"
position = 0um,0um,175mm
number_of_pixels = 1024,512
pixel_pitch = 29.24um, 26.88um
spatial_resolution = 5.00um, 5.00um
time_resolution = 2us
material_budget = 0.0005
coordinates = "cartesian"
orientation_mode = "xyz"
# orientation = 180deg, 180deg, 0deg
mask_file="/home/akumar/ce65v2_ana_soft/analysis/beam/mask_file/ref-plan4.txt"
orientation = 0deg, 0deg, 0deg

[ALPIDE_5]
type = "ALPIDE"
position = 0um,0um,200mm
number_of_pixels = 1024,512
pixel_pitch = 29.24um, 26.88um
spatial_resolution = 5.00um, 5.00um
time_resolution = 2us
material_budget = 0.0005
coordinates = "cartesian"
orientation_mode = "xyz"
# orientation = 180deg, 180deg, 0deg
mask_file="/home/akumar/ce65v2_ana_soft/analysis/beam/mask_file/ref-plan5.txt"
orientation = 0deg, 0deg, 0deg

[CE65_6]
type = "CE65V2"
orientation_mode = "xyz"
orientation = 180deg, 180deg, 0deg
position = 0um,0mm,100mm
number_of_pixels = 48,24
pixel_pitch = 18um, 18um
spatial_resolution = 5.00um, 5.00um
time_resolution = 2us
material_budget = 0.0005
coordinates = "cartesian"
#calibration_file = "../qa/pcb08_hv10-noisemap.root"
calibration_file = "../qa/pcb02_hv10-noisemap.root"
role = "dut"
