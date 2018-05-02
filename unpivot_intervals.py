# -*- coding: utf-8 -*-
"""
Created on Wed May  2 14:06:57 2018

@author: gatesk
"""

import pandas as pd

exampleunpivot = pd.read_csv(r"C:\Users\gatesk\Documents\___aaa___PERSONAL\NT\example_samples.csv")
print (list(exampleunpivot))

df = pd.melt(exampleunpivot, id_vars=['SAMPLEID'], value_vars=['Ag_PPB', 'Ag_PPM', 'Al_PCT', 'Al_PPM', 'Al2O3_PCT', 'As_PPB', 'As_PPM', 'Au_PPB', 'Au_PPM', 'Au1_PPB', 'Au1_PPM', 'Au2_PPB', 'Au3_PPB', 'Au4_PPB', 'B_PPM', 'Ba_PPM', 'BaO_PCT', 'BaO_PPM', 'Be_PPM', 'Bi_PCT', 'Bi_PPM', 'C_PCT', 'Ca_PCT', 'Ca_PPM', 'CaO_PCT', 'CaO_PPM', 'Cd_PPM', 'Ce_PPM', 'Co_PPB', 'Co_PPM', 'CO2_PCT', 'Cr_PPM', 'Cr2O3_PCT', 'Cr2O3_PPM', 'Cs_PPM', 'Cu_PCT', 'Cu_PPM', 'Dy_PPM', 'Er_PPM', 'Eu_PPM', 'F_PPM', 'Fe_PCT', 'Fe_PPM', 'Fe2O3_PCT', 'Ga_PPM', 'Gd_PPM', 'Ge_PPM', 'Hf_PPM', 'Hg_PPM', 'Ho_PPM', 'In_PPB', 'In_PPM', 'K_PCT', 'K_PPM', 'K2O_PCT', 'K2O_PPM', 'La_PPM', 'Li_PPM', 'LOI_PCT', 'Lu_PPM', 'Mg_PCT', 'Mg_PPM', 'MgO_PCT', 'MgO_PPM', 'Mn_PCT', 'Mn_PPM', 'MnO_PCT', 'MnO_PPM', 'Mo_PPM', 'Na_PCT', 'Na_PPM', 'Na2O_PCT', 'Na2O_PPM', 'Nb_PPM', 'Nd_PPM', 'Ni_PPB', 'Ni_PPM', 'P_PCT', 'P_PPM', 'P2O5_PCT', 'P2O5_PPM', 'Pb_PCT', 'Pb_PPB', 'Pb_PPM', 'Pd_PPB', 'Pd_PPM', 'Pd1_PPB', 'Pr_PPM', 'Pt_PPB', 'Pt_PPM', 'Pt1_PPB', 'Rb_PPM', 'Re_PPM', 'Ru_PPM', 'S_PCT', 'S_PPM', 'Sb_PPM', 'Sc_PPM', 'Se_PPM', 'Si_PCT', 'SiO2_PCT', 'Sm_PPM', 'Sn_PPM', 'SO3_PCT', 'Sr_PCT', 'Sr_PPM', 'SrO_PCT', 'Ta_PPM', 'Tb_PPM', 'Te_PPM', 'Th_PPM', 'Ti_PCT', 'Ti_PPM', 'TiO2_PCT', 'TiO2_PPM', 'Tl_PPM', 'Tm_PPM', 'U_PPB', 'U_PPM', 'V_PCT', 'V_PPM', 'V2O5_PPM', 'W_PPM', 'Y_PPM', 'Yb_PPM', 'Zn_PCT', 'Zn_PPB', 'Zn_PPM', 'Zr_PCT', 'Zr_PPM', 'ZrO2_PPM'])


df = df.sort_values('SAMPLEID', axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')
print (df)