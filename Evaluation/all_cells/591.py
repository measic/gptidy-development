start = datetime(2017, 3, 31, 10, 27)
stop = datetime(2017, 3, 31, 10, 44)
rangeSetting = 2*10**-7

norm = FluxNormalization('/home/pyne-user/Dropbox/UCB/Research/ETAs/88Inch/Data/Experiments/PHS/33MeVTa_29-31Mar17/BCM/2H+1_33MeV_1027_31Mar2017_Goldblum at 100 nA no bias.bcm', 
                        startTime=start, stopTime=stop)
norm.currentIntegrator = (575)*rangeSetting*1E6
norm.set_solid_angle(640+46.4, 25)
norm.set_dead_time(nonparalyzable_beam_dead_time, obsCountRate=(47833445)/norm.runTime, 
                   tauDetector=300E-9, tauBeam=158.5E-9)
norm.mcnpNormFactor=(1-cos(radians(1)))/2*4*np.pi*20.8E9*norm.currentIntegrator

print str(norm)