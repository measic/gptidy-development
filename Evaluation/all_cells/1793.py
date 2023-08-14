mugler2014 = {'consonant_single': 36.1,
              'consonant_avg': 20.4,
              'consonant_avg_pm': 9.8,
              'consonant_chance': 7.4,
              'vowel_single': 23.9,
              'vowel_avg': 19.2,
              'vowel_avg_pm': 3.7,
              'vowel_chance': 12.9}
mugler2014['consonant_single_cc'] = accuracy.naive_channel_capacity(mugler2014['consonant_single']/100., 24)
mugler2014['consonant_avg_cc'] = accuracy.naive_channel_capacity(mugler2014['consonant_avg']/100., 24)
mugler2014['vowel_single_cc'] = accuracy.naive_channel_capacity(mugler2014['vowel_single']/100., 15)
mugler2014['vowel_avg_cc'] = accuracy.naive_channel_capacity(mugler2014['vowel_avg']/100., 15)

def format_string(string, *data):
    acc, std, ac, ncc, cc = data
    return string.format(np.around(acc, 1), np.around(std, 1), np.around(ac, 1), np.around(ncc, 2), np.around(cc, 2))

d_cv1 = "Deep network, 57 CV, single subj.         &{} $\pm$ {}\% & {}x & {} ({} exact) \\\\\n"
d_cv2 = "Deep network, 57 CV, subj. average        &{} $\pm$ {}\% & {}x & {} ({} exact) \\\\\n"
d_cv1 = format_string(d_cv1, dcv_acc[0].mean(), dcv_acc[0].std(),
                      (dcv_acc[0]/cv_chance[0]).mean(),
                      dcv_ncc[0], dcv_cc[0])
d_cv2 = format_string(d_cv2, dcv_acc.mean(), dcv_acc.std(),
                      (dcv_acc/cv_chance).mean(),
                      dcv_ncc.mean(), dcv_cc.mean())
l_cv1 = "Logistic Regression, 57 CV, single subj.  &{} $\pm$ {}\% & {}x & {} ({} exact) \\\\\n"
l_cv2 = "Logistic Regression, 57 CV, subj. average &{} $\pm$ {}\% & {}x & {} ({} exact) \\\\\n"
l_cv1 = format_string(l_cv1, lcv_acc[0].mean(), lcv_acc[0].std(),
                      (lcv_acc[0]/cv_chance[0]).mean(),
                      lcv_ncc[0], lcv_cc[0])
l_cv2 = format_string(l_cv2, lcv_acc.mean(), lcv_acc.std(),
                      (lcv_acc/cv_chance).mean(),
                      lcv_ncc.mean(), lcv_cc.mean())
hline = "\\hline\n"
d_c1 = "Deep network, 19 cons., single subj.         &{} $\pm$ {}\% & {}x & {} ({} exact) \\\\\n"
d_c2 = "Deep network, 19 cons., subj. average        &{} $\pm$ {}\% & {}x & {} ({} exact) \\\\\n"
d_c1 = format_string(d_c1, dc_acc[0].mean(), dc_acc[0].std(),
                      (dc_acc[0]/c_chance[0]).mean(),
                      dc_ncc[0], dc_cc[0])
d_c2 = format_string(d_c2, dc_acc.mean(), dc_acc.std(),
                      (dc_acc/c_chance).mean(),
                      dc_ncc.mean(), dc_cc.mean())
l_c1 = "Logistic Regression, 19 cons., single subj.  &{} $\pm$ {}\% & {}x & {} ({} exact) \\\\\n"
l_c2 = "Logistic Regression, 19 cons., subj. average &{} $\pm$ {}\% & {}x & {} ({} exact) \\\\\n"
l_c1 = format_string(l_c1, lc_acc[0].mean(), lc_acc[0].std(),
                      (lc_acc[0]/c_chance[0]).mean(),
                      lc_ncc[0], lc_cc[0])
l_c2 = format_string(l_c2, lc_acc.mean(), lc_acc.std(),
                      (lc_acc/c_chance).mean(),
                      lc_ncc.mean(), lc_cc.mean())
m_c = ("LDA~\cite{{mugler2014}}, 24 cons., single subj.  &{}\% & {}x & {} \\\\\n" +
       "LDA~\cite{{mugler2014}}, 24 cons., subj. average &{} $\pm$ {}\% & {}x & {} \\\\\n")
m_c = m_c.format(np.around(mugler2014['consonant_single'], 1),
                 np.around(mugler2014['consonant_single']/mugler2014['consonant_chance'], 1),
                 np.around(mugler2014['consonant_single_cc'][0], 2),
                 np.around(mugler2014['consonant_avg'], 1),
                 np.around(mugler2014['consonant_avg_pm'], 1),
                 np.around(mugler2014['consonant_avg']/mugler2014['consonant_chance'], 1),
                 np.around(mugler2014['consonant_avg_cc'][0], 2))
d_v1 = "Deep network, 3 vowels, single subj.         &{} $\pm$ {}\% & {}x & {} ({} exact) \\\\\n"
d_v2 = "Deep network, 3 vowels, subj. average        &{} $\pm$ {}\% & {}x & {} ({} exact) \\\\\n"
d_v1 = format_string(d_v1, dv_acc[0].mean(), dv_acc[0].std(),
                      (dv_acc[0]/v_chance[0]).mean(),
                      dv_ncc[0], dv_cc[0])
d_v2 = format_string(d_v2, dv_acc.mean(), dv_acc.std(),
                      (dv_acc/v_chance).mean(),
                      dv_ncc.mean(), dv_cc.mean())
l_v1 = "Logistic Regression, 3 vowels, single subj.  &{} $\pm$ {}\% & {}x & {} ({} exact) \\\\\n"
l_v2 = "Logistic Regression, 3 vowels, subj. average &{} $\pm$ {}\% & {}x & {} ({} exact) \\\\\n"
l_v1 = format_string(l_v1, lv_acc[0].mean(), lv_acc[0].std(),
                      (lv_acc[0]/v_chance[0]).mean(),
                      lv_ncc[0], lv_cc[0])
l_v2 = format_string(l_v2, lv_acc.mean(), lv_acc.std(),
                      (lv_acc/v_chance).mean(),
                      lv_ncc.mean(), lv_cc.mean())
m_v = ("LDA~\cite{{mugler2014}}, 15 vowels, single subj.  &{}\% & {}x & {} \\\\\n" +
       "LDA~\cite{{mugler2014}}, 15 vowels, subj. average &{} $\pm$ {}\% & {}x & {} \\\\\n")
m_v = m_v.format(np.around(mugler2014['vowel_single'], 1),
                 np.around(mugler2014['vowel_single']/mugler2014['vowel_chance'], 1),
                 np.around(mugler2014['vowel_single_cc'][0], 2),
                 np.around(mugler2014['vowel_avg'], 1),
                 np.around(mugler2014['vowel_avg_pm'], 1),
                 np.around(mugler2014['vowel_avg']/mugler2014['vowel_chance'], 1),
                 np.around(mugler2014['vowel_avg_cc'][0], 2))
print(d_cv1 + d_cv2 + l_cv1 + l_cv2 + hline +
      d_c1 + d_c2 + l_c1 + l_c2 + m_c + hline +
      d_v1 + d_v2 + l_v1 + l_v2 + m_v)