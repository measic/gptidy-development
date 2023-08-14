I = Variable(name='I', num_states=2) #Influenza
S = Variable(name='S', num_states=2) #Smokes
ST = Variable(name='ST', num_states=2) #SoreThreat
F = Variable(name='F', num_states=2) #Fever
B = Variable(name='B', num_states=2) #Bronchitis
C = Variable(name='C', num_states=2) #Coughing
W = Variable(name='W', num_states=2) #Wheezing

f_I = Factor(name='p(I)',
                 f=np.array([0.95, 0.05]),
                 neighbours=[I])

f_S = Factor(name='p(S)',
                 f=np.array([0.8, 0.2]),
                 neighbours=[S])

prob_ST = [
    [ #ST = 0
        0.999, # I = 0
        0.7 # I = 1
    ],
    [ #ST = 1
        0.001, # I = 0
        0.3 # I = 1
    ]
]
f_ST = Factor(name='p(ST |I)',
                 f=np.array(prob_ST),
                 neighbours=[ST, I])

prob_F = [
    [ #F = 0
        0.95, # I = 0
        0.1 # I = 1
    ],
    [ #F = 1
        0.05, # I = 0
        0.9 # I = 1
    ]
]
f_F = Factor(name='p(F |I)',
                 f=np.array(prob_F),
                 neighbours=[F, I])

prob_B = [
    [ #B = 0
        [ # I = 0
          0.9999, # S = 0
          0.3     # S = 1
        ],
        [ # I = 1
          0.1,  # S = 0
          0.01  # S = 1
        ]
    ],
    [  #B = 1
        [ # I = 0
          0.0001, # S = 0
          0.7     # S = 1
        ],
        [ # I = 1
          0.9,  # S = 0
          0.99  # S = 1
        ]
    ]
]
f_B = Factor(name='p(B |I, S)',
                 f=np.array(prob_B),
                 neighbours=[B, I, S])

prob_C = [
    [ #C = 0
        0.93, # B = 0
        0.2 # B = 1
    ],
    [ #C = 1
        0.07, # B = 0
        0.8 # B = 1
    ]
]
f_C = Factor(name='p(C |B)',
                 f=np.array(prob_C),
                 neighbours=[C, B])


prob_W = [
    [ #W = 0
        0.999, # B = 0
        0.4 # B = 1
    ],
    [ #W = 1
        0.001, # B = 0
        0.6 # B = 1
    ]
]
f_W = Factor(name='p(W |B)',
                 f=np.array(prob_W),
                 neighbours=[W, B])
