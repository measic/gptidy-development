reload(pccsims)
coco = pccsims.pyCoCo(pcc.utils.b(filter_path), pcc.utils.b(coco_root_path))

# flux, flux_err = coco.simulate(b"SN2009jf", 
#                     0.008, 0.0, 0.0, 0.0, 3.1, 
#                     mjdmax, mjd_to_sim, 
#                     filters_to_sim)

flux, flux_err = coco.simulate(b"SN2007uy", 
                    z_obs, 0.0, 0.0, 0.0, 3.1, 
                    mjdmax, mjd_to_sim, 
                    filters_to_sim)

# flux, flux_err = coco.simulate(b"SN2009jf", 
#                     0.008, 0.0, 0.1, 0.1, 3.1, 
#                     mjdmax, mjd_to_sim, 
#                     filters_to_sim)