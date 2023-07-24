def tree_visualize(root_node):
    tree_string = ""
    tree_string = print_decision_tree_latex(root_node, tree_string)
    
    os.system("cd ../Figures; rm -rf decision_tree.tex; more main_pt1.tex >> decision_tree.tex; echo '' >> decision_tree.tex;")
    os.system("cd ../Figures; echo '" + tree_string + "' >> decision_tree.tex;  more main_pt2.tex >> decision_tree.tex;")
    os.system("cd ../Figures; /Library/TeX/texbin/pdflatex decision_tree.tex;")
    os.system("cd ../Figures; convert -density 300 -trim decision_tree.pdf -quality 100 decision_tree.png")
    os.system("cd ../Figures; rm *.aux *.log")
    display(Image('../Figures/decision_tree.png', retina=True))
    
tree_visualize(root)