reload(pccsims)
coco = pccsims.pyCoCo(pcc.utils.b(filter_path), pcc.utils.b(coco_root_path))
flux, variable_def = coco.simulate(b'SN2007uy', z_obs, 0.0, 0.0, 0.0, 3.1, mjdmax, mjd_to_sim, filters_to_sim)