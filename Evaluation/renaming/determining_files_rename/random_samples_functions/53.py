from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(16, 8))
ax = fig.add_subplot(111, projection='3d')
import cv2
R1 = Rt1[:, 0:3]
t1 = Rt1[:, 3]
R2 = Rt2[:, 0:3]
t2 = Rt2[:, 3]

def draw_person(ax, indv_left, indv_right):
    HND_l = 0
    ELB_l = 1
    SHO_l = 2
    HND_r = 5
    ELB_r = 4
    SHO_r = 3
    FOT_l = 6
    KNE_l = 7
    HIP_l = 8
    FOT_r = 11
    KNE_r = 10
    HIP_r = 9

    def triangulate(elem):
        a = indv_left[1][elem]
        b = indv_right[1][elem]
        a = a[:2]
        b = b[:2]
        A = np.array([a], 'float32').T
        B = np.array([b], 'float32').T
        result = cv2.triangulatePoints(P1, P2, A, B)
        result /= result[3]
        return result[:3]
    left_hand = triangulate(HND_l)
    left_elbow = triangulate(ELB_l)
    left_shoulder = triangulate(SHO_l)
    right_hand = triangulate(HND_r)
    right_elbow = triangulate(ELB_r)
    right_shoulder = triangulate(SHO_r)
    right_hip = triangulate(HIP_r)
    right_knee = triangulate(KNE_r)
    right_foot = triangulate(FOT_r)
    left_hip = triangulate(HIP_l)
    left_knee = triangulate(KNE_l)
    left_foot = triangulate(FOT_l)
    ALL = np.squeeze(np.array([left_hand, left_elbow, left_shoulder, right_shoulder, right_elbow, right_hand, right_elbow, right_shoulder, right_hip, right_knee, right_foot, right_knee, right_hip, left_hip, left_knee, left_foot, left_knee, left_hip, left_shoulder]))
    X = ALL[:, 0]
    Y = ALL[:, 1]
    Z = ALL[:, 2]
    ax.plot(X, Y, Z)
draw_person(ax, annot1[0], annot2[1])
draw_person(ax, annot2[0], annot1[1])
ax.set_xlim([-4000, 4000])
ax.set_ylim([-4000, 4000])
ax.set_zlim([0, 4000])

def function_def(ax, R, t):
    pos = -R.T @ t
    ax.scatter(pos[0], pos[1], pos[2])
    ax.plot([pos[0], pos[0]], [pos[1], pos[1]], [pos[2], 0])
function_def(ax, R1, t1)
function_def(ax, R2, t2)