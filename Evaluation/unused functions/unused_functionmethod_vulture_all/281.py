#ignore
# @pysnooper.snoop()
def plot_2d(value, ax=None, group=None, mask=None, matrix_id=0, mat_as_group=False, 
            group_id=None, linewidths=0, is_string=False, fmt="d", square=False):
  
  if hasattr(value, "numpy"):
    value = value.numpy()
  if group is not None and hasattr(group, "numpy"):
    group = group.numpy()
  if mask is not None and hasattr(mask, "numpy"):
    mask = tf.squeeze(mask)
    mask = tf.ones_like(value) * mask
    mask = mask.numpy()
    

  cmaps = ['PuOr', 'tab20b', 'RdBu']
  group_id = int(group[0][0])
  cmap = cmaps[group_id]
  
  if is_string:
    fmt = ''
  
  sns.heatmap(group, 
              fmt=fmt,
#               cmap=cmap,
              cmap=cmap,
              annot=value, 
              cbar=False, 
              xticklabels=False, 
              yticklabels=False, 
              square=square,
              mask=mask,
              linewidths=linewidths,
              ax=ax)