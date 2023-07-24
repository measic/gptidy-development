if not os.path.isfile('lst_bootcamp_gl_data.tar.gz'):
    !wget https://gitlab.lapp.in2p3.fr/GammaLearn/GammaLearn/raw/master/share/lst_bootcamp_gl_data.tar.gz
    !tar xvzf lst_bootcamp_gl_data.tar.gz