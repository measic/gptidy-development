connection_all = []
special_k = []
mid_num = 10

for k in range(len(mapIdx)):
    score_mid = paf_avg[:,:,[x-19 for x in mapIdx[k]]]
    candA = all_peaks[limbSeq[k][0]-1]
    candB = all_peaks[limbSeq[k][1]-1]

    nA = len(candA)
    nB = len(candB)
    indexA, indexB = limbSeq[k]
    if(nA != 0 and nB != 0):
        connection_candidate = []
        for i in range(nA):
            for j in range(nB):
                vec = np.subtract(candB[j][:2], candA[i][:2])
                # print('vec: ',vec)
                norm = math.sqrt(vec[0]*vec[0] + vec[1]*vec[1])
                # print('norm: ', norm)
                vec = np.divide(vec, norm)
                # print('normalized vec: ', vec)
                startend = zip(np.linspace(candA[i][0], candB[j][0], num=mid_num), \
                               np.linspace(candA[i][1], candB[j][1], num=mid_num))
                # print('startend: ', startend)
                vec_x = np.array([score_mid[int(round(startend[I][1])), int(round(startend[I][0])), 0] \
                                  for I in range(len(startend))])
                # print('vec_x: ', vec_x)
                vec_y = np.array([score_mid[int(round(startend[I][1])), int(round(startend[I][0])), 1] \
                                  for I in range(len(startend))])
                # print('vec_y: ', vec_y)
                score_midpts = np.multiply(vec_x, vec[0]) + np.multiply(vec_y, vec[1])
                # print(score_midpts)
                # print('score_midpts: ', score_midpts)
                score_with_dist_prior = sum(score_midpts)/len(score_midpts) + min(0.5*oriImg.shape[0]/norm-1, 0)
                
                # print('score_with_dist_prior: ', score_with_dist_prior)
                criterion1 = len(np.nonzero(score_midpts > param['thre2'])[0]) > 0.8 * len(score_midpts)
                # print('score_midpts > param["thre2"]: ', len(np.nonzero(score_midpts > param['thre2'])[0]))
                criterion2 = score_with_dist_prior > 0
                
                if criterion1 and criterion2:
                    # print('match')
                    # print(i, j, score_with_dist_prior, score_with_dist_prior+candA[i][2]+candB[j][2])
                    connection_candidate.append([i, j, score_with_dist_prior, score_with_dist_prior+candA[i][2]+candB[j][2]])
                # print('--------end-----------')
        connection_candidate = sorted(connection_candidate, key=lambda x: x[2], reverse=True)
        # print('-------------connection_candidate---------------')
        # print(connection_candidate)
        # print('------------------------------------------------')
        connection = np.zeros((0,5))
        for c in range(len(connection_candidate)):
            i,j,s = connection_candidate[c][0:3]
            if(i not in connection[:,3] and j not in connection[:,4]):
                connection = np.vstack([connection, [candA[i][3], candB[j][3], s, i, j]])
                # print('----------connection-----------')
                # print(connection)
                # print('-------------------------------')
                if(len(connection) >= min(nA, nB)):
                    break

        connection_all.append(connection)
    else:
        special_k.append(k)
        connection_all.append([])