#ignore
# @pysnooper.snoop()
def plot(value, group=None, group_dim=0, mask=None, labels=[], square=False, shape_desc='', width_prec=None, bottom_prec=None, 
         is_string=False, name='', fmt="d", single_plot_size=4, h_dist_ratio=0.7, w_dist_ratio=0.7, linewidths=None):

  shape = value.shape
  num_groups = shape[0]
  
  if hasattr(value, 'numpy'):
    if value.dtype in [tf.int32, tf.int64]:
      value = tf.cast(value, tf.int32)
    elif value.dtype in [tf.float32, tf.float64] and fmt == "d":
      fmt = ".2g"
    
    value = value.numpy()

  if hasattr(value, 'ndim'):
    ndim = value.ndim
  else:
    ndim = len(value)
    
    
  if ndim == 2:
    value = value[np.newaxis, np.newaxis, :, :]
  if ndim == 3:
    value = value[np.newaxis, :, :, :]
  if ndim == 4:
    pass
  
  # decide how to group sub-tensors smartly
  if not group_dim:
    group_dim = ndim - 1
    
  # generate group identifier tensor for differentiating between
  # different bactch / sentence
  if group is None:
    group_ids = tf.range(num_groups, dtype=tf.int64).numpy()
    if group_dim == 1:
      group = group_ids[:, tf.newaxis]
    elif group_dim == 2:
      group = group_ids[:, tf.newaxis, tf.newaxis]
    elif group_dim == 3:
      group = group_ids[:, tf.newaxis, tf.newaxis, tf.newaxis]

    # broadcast to all groups    
    group = tf.ones(shape=value.shape) * group

  d0, d1, d2, d3 = value.shape

  # set figure size based on tensor dimensions
  fig_width = (d3 * 1.0 / 4) * d0 * single_plot_size
  fig_height = (d2 * 1.0 / 4) * single_plot_size
  figsize = (fig_width, fig_height)
  
  if width_prec is None:
    width_prec = 1.0 / d0
  
  if bottom_prec is None:
    bottom_prec = 1.0 / d1

  fig = plt.figure(figsize=figsize)
  fig_title = f'name: {name}, shape: {shape}' if name else f'shape: {shape}'
  
  if shape_desc:
    fig_title = fig_title + ' = ' + shape_desc
    
  for e0 in range(d0):

    # plot 2d array in reverse order since the earlier plot will be covered
    for e1 in reversed(range(d1)):
      annot = value[e0, e1]

      # select corresponding matplotlib axis      
      cur_ax = fig.add_axes([(0.7) * e0 + (e1 / d0 / d3) * w_dist_ratio, 
                             e1 / d2 * h_dist_ratio, 
                             width_prec, 
                             bottom_prec]) 

      matrix_id = e0 + e1 * 2
      
      if mask is not None:
        if ndim == 2:
          mask_idx = e0
        elif ndim == 3:
          mask_idx = e1
        elif ndim ==4:
          mask_idx = e0
          
        # mimic broadcasting
        if mask.shape[0] == 1:
          mask_idx = 0
          
        plot_2d(annot, group=group[e0, e1], ax=cur_ax, matrix_id=matrix_id, 
                is_string=is_string, fmt=fmt, mask=mask[mask_idx], square=square)
      else:
        plot_2d(annot, group=group[e0, e1], ax=cur_ax, matrix_id=matrix_id, is_string=is_string, fmt=fmt, square=square)
      
      # minic shadowing for each 2d matrix
      width_delta_prec = 0.0005
      height_delta_prec = width_delta_prec * d2 / d3
      
      for k in range(1, 3):
        shadow_ax = fig.add_axes([(0.7) * e0 + (e1 / d0 / d3)  * w_dist_ratio - width_delta_prec * k, 
                                  e1 / d2 * h_dist_ratio - height_delta_prec * k, 
                                  width_prec, 
                                  bottom_prec])  
        
        if k == 2:
          linewidths = 1
        else:
          linewidths = 0
          
        if mask is not None:
          if ndim == 2:
            mask_idx = e0
          elif ndim == 3:
            mask_idx = e1
          elif ndim ==4:
            mask_idx = e0
            
          # mimic broadcasting
          if mask.shape[0] == 1:
            mask_idx = 0  
            
            
          plot_2d(annot, group=group[e0, e1], ax=shadow_ax, matrix_id=matrix_id, 
                  linewidths=linewidths, is_string=is_string, fmt=fmt, mask=mask[mask_idx], square=square)
        else:
          plot_2d(annot, group=group[e0, e1], ax=shadow_ax, matrix_id=matrix_id, 
                  linewidths=linewidths, is_string=is_string, fmt=fmt, square=square)

      if e0 == 0 and e1 == 0:
        ax1 = cur_ax
        
        if labels:
            plt.ylabel(labels[-2])
            plt.xlabel(labels[-1] + '\n' + fig_title)
        else:
          plt.xlabel(fig_title)

        # 4D 中的 axis1 說明 label
#           if len(labels) >= 3:
#             plt.text(d3 + 2, 1 + 0.5, labels[-3],
#                      rotation=0, rotation_mode='anchor')

      if e1 == d0 - 1:
        ax2 = cur_ax
        

#       transFigure = fig.transFigure.inverted()
#       coord1 = transFigure.transform(ax1.transData.transform([d3 + 2 + 0.5, 0]))
#       coord2 = transFigure.transform(ax2.transData.transform([d3 + 0.5, d2]))


#       line = mpl.lines.Line2D((coord1[0],coord2[0]),(coord1[1],coord2[1]), 
#                               transform=fig.transFigure, 
#                               linestyle='--',
#                               color='black')
#       fig.lines.append(line)

