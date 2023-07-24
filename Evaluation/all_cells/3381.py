import datasets.divahisdb as diva
hisdb = diva.HisDBDataset(datasets_path / diva.NAME, gt=True)
page, page_gt = hisdb[0]