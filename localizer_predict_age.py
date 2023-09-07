#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 14:43:20 2023

@author: edouard.duchenay@cea.fr
"""

import numpy as np
import os
import os.path
import numpy as np
import pandas as pd
import nibabel
import glob

###############################################################################
# %% Parameters

BASEDIR = '/home/ed203246/data/psy_sbox'
WD = os.path.join(BASEDIR, 'analyses/2023_localizer_toy-analysis')

# os.makedirs(WD)

###############################################################################
# % Load Data


img_filenames = glob.glob(os.path.join(BASEDIR, 'localizer/derivatives/cat12-12.6_vbm/sub-*/ses-*/anat/mri/mwp1*.nii'))
mask_filename = os.path.join(WD, 'data/mni_cerebrum-mask.nii.gz')

mask_arr = nibabel.load(mask_filename).get_fdata() != 0
imag_participant_ids = []
X = np.array([nibabel.load(img_filename).get_fdata()[mask_arr] for img_filename in img_filenames])
assert images.shape == (88, 331695)

data = pd.read_csv(os.path.join(BASEDIR, 'localizer/participants.tsv'), delimiter='\t')

y = data.age.values
