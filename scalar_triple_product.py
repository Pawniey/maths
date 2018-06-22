# Scalar triple products for 3 vectors , to verify if they are coplanar or not

# User passes 3 tuples
def stp_calculate(u, v, w):
    stp = 0
    # Coffecient for every vector is calculated
    i_coffecient = ((v[1] * w[2]) - (w[1] * v[2]))
    j_coffecient = -((v[0] * w[2]) - (w[0] * v[2]))
    k_coffecient = ((v[0] * w[1]) - (w[0] * v[1]))
    
    #Forumla for STP = [u.(v * w)]
    
    v_w = (i_coffecient, j_coffecient, k_coffecient)
    for i in range(0, 3):
        stp += u[i] * v_w[i]

    return stp
