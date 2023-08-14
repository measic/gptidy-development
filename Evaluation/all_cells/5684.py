def word2features(sent, i):
    word = sent[i][0]
    postag = sent[i][1]
    features = {
        'word_lower':word.lower(),
        'suffix3':word[-3:],
        'suffix2':word[-2:],
        'prefix1':word[:2],
        'prefix2':word[:3],
        'wordIsupper':word.isupper(),
        'wordIstitle':word.istitle(),
        'word.isdigit':word.isdigit(),
        'postag':postag,
#        'postag[:2]=' + postag[:2],
    }
    if i > 0:
        word1 = sent[i-1][0]
        postag1 = sent[i-1][1]
        features.update({
            '-1word.lower': word1.lower(),
            '-1word.istitle': word1.istitle(),
            '-1word.isupper': word1.isupper(),
            '-1word.isdigit':word1.isdigit(),
            '-1postag' :postag1,
#            '-1postag[:2]=' + postag1[:2],
        })
    else:
        #features.update('BOS')
        word1 = 'bos'
        postag1 = 'bos'
        features.update({
            '-1word.lower': word1.lower(),
            '-1word.istitle': word1.istitle(),
            '-1word.isupper': word1.isupper(),
            '-1postag' :postag1,
#            '-1postag[:2]=' + postag1[:2],
        })
        
    if i < len(sent)-1:
        word1 = sent[i+1][0]
        postag1 = sent[i+1][1]
        features.update({
            '1word.lower': word1.lower(),
            '1word.istitle': word1.istitle(),
            '1word.isupper': word1.isupper(),
            '1postag' :postag1,
#            '-1postag[:2]=' + postag1[:2],
        })
    else:
        #features.update('BOS')
        word1 = 'eos'
        postag1 = 'eos'
        features.update({
            '1word.lower': word1.lower(),
            '1word.istitle': word1.istitle(),
            '1word.isupper': word1.isupper(),
            '1postag' :postag1,
#            '-1postag[:2]=' + postag1[:2],
        })

                
    return features


def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

def sent2labels(sent):
    return [label for token, postag, label in sent]

def sent2tokens(sent):
    return [token for token, postag, label in sent]    