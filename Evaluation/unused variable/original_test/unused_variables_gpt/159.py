# snname = "SN2007uy"
snname = "SN2013ge"

sn = pcc.classes.SNClass(snname)

phot_path = os.path.join(coco_root_path, "data/lc/", snname + ".dat")
speclist_path = os.path.join(str(coco_root_path),"lists/" + snname + ".list")
recon_filename = os.path.abspath(os.path.join(str(coco_root_path), "recon/", snname + ".dat"))

print(phot_path)
sn.load_phot(path = phot_path)
sn.get_lcfit(recon_filename)

sn.load_list(path = speclist_path)
sn.load_spec()
sn.plot_lc(multiplot = False, mark_spectra=True)