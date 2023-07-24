y_pred_array = [tree.predict(X_new) for tree in (tree_reg1, tree_reg2, tree_reg3)]
y_pred = sum(y_pred_array)
y_pred