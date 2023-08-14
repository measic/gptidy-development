nodes = [ST, F, C, W, f_I, f_ST, f_F, f_C, f_W, I, B, f_B, S, f_S]
for n in nodes:
    n.reset()
    
C.pending.add(f_C)
W.pending.add(f_W)
f_I.pending.add(I)
f_S.pending.add(S)
ST.pending.add(f_ST)
F.pending.add(f_F)

I.set_observed(0)

# I.set_observed(1)

max_sum(nodes)

I_ulm = I.unnormalized_log_marginal()
S_ulm = S.unnormalized_log_marginal()
ST_ulm = ST.unnormalized_log_marginal()
F_ulm = F.unnormalized_log_marginal()
B_ulm = B.unnormalized_log_marginal()
C_ulm = C.unnormalized_log_marginal()
W_ulm = W.unnormalized_log_marginal()

print("I", I_ulm)
print("S", S_ulm)
print("ST", ST_ulm)
print("F", F_ulm)
print("B", B_ulm)
print("C", C_ulm)
print("W", W_ulm)