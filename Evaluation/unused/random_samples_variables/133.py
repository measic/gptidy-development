X = Variable(name='X', num_states=2)
X_prior = Factor(name='p(X)',
                 f=np.array([0.95, 0.05]),
                 neighbours=[X])

# Please stick to the naming convention used below, otherwise the test functionality throughout the lab won't work
Z = Variable(name='Z', num_states=2)
Z_prior = Factor(name='p(Z)',
                 f=np.array([0.8, 0.2]),
                 neighbours=[Z])
                 
Y = Variable(name='Y', num_states=2)
f_Y_cond = [
    [ #Y = 0
        [ # X = 0
          0.9999, # Z = 0
          0.3     # Z = 1
        ],
        [ # X = 1
          0.1,  # Z = 0
          0.01  # Z = 1
        ]
    ],
    [  #Y = 1
        [ # X = 0
          0.0001, # Z = 0
          0.7     # Z = 1
        ],
        [ # X = 1
          0.9,  # Z = 0
          0.99  # Z = 1
        ]
    ]
]
Y_cond = Factor(name='p(Y |X, Z)',
                 f=np.array(f_Y_cond),
                 neighbours=[Y, X, Z])
                                 
