## Load symbol and parameters, the parameters can be downloaded from the following link. 
## including the realtimePose-symbol.json and realtimePose-0000.params
## https://drive.google.com/drive/folders/0BzffphMuhDDMV0RZVGhtQWlmS1U?usp=sharing
output_prefix='realtimePose'
sym, arg_params, aux_params = mx.model.load_checkpoint(output_prefix, 0)