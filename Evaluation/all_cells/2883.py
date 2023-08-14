abslookup_nolm_aer = axml.load('nolm_aer/abs_lookup.xml')
print(abslookup_nolm_aer.speciestags)
abslookup_nolm_aer_36 = axml.load('nolm_aer_36/abs_lookup.xml')
print(abslookup_nolm_aer_36.speciestags)
abslookup_nolm_aer_arts = axml.load('nolm_aer_arts/abs_lookup.xml')
print(abslookup_nolm_aer_arts.speciestags)
abslookup_nolm_hitran = axml.load('nolm_hitran/abs_lookup.xml')
print(abslookup_nolm_hitran.speciestags)
abslookup_lm_aer = axml.load('lm_aer/abs_lookup.xml')
print(abslookup_lm_aer.speciestags)
abslookup_lm_aer_36 = axml.load('lm_aer_36/abs_lookup.xml')
print(abslookup_lm_aer_36.speciestags)

abslookup_lm = abslookup_lm_aer
abslookup_nolm = abslookup_nolm_aer