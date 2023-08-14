from mixsig.utils import factors
# CODE
# fact_a = factors(self.batch_size)
# fact_b = factors(self.window_size)
# gcm = max(fact_a.intersection(fact_b))
# chop_index = len(timestamps) % (self.window_size * self.batch_size // gcm)

# TODO: Move this to unit tests
ws, bs = 512, 392
nts = 200771
print(f'nts   = {nts}\nws*bs = {ws * bs}')
print(factors(nts))

fact_a = factors(bs)
print(fact_a)
fact_b = factors(ws)
print(fact_b)
gcm = max(fact_a.intersection(fact_b))
print(gcm)

print('#'*20)
print(ws * bs // gcm)
print(nts % (ws * bs // gcm))
nts2 = nts - (nts % (ws * bs // gcm))
print(nts2, nts2 // bs, nts2 // ws)

print('#'*20)
print(ws * bs)
print(nts % (ws * bs))
nts2 = nts - (nts % (ws * bs))
print(nts2, nts2 // bs, nts2 // ws)