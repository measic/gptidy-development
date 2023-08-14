nodes = [ST, F, C, W, f_I, f_ST, f_F, f_C, f_W, I, B, f_B, S, f_S]
for n in nodes:
    n.reset()
    
C.pending.add(f_C)
W.pending.add(f_W)
f_I.pending.add(I)
f_S.pending.add(S)
ST.pending.add(f_ST)
F.pending.add(f_F)

sum_product(nodes)

print("I", I.marginal())
print("S", S.marginal())
print("ST", ST.marginal())
print("F", F.marginal())
print("B", B.marginal())
print("C", C.marginal())
print("W", W.marginal())