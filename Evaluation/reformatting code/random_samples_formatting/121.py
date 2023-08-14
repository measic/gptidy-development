corpora = []
for name in name_corpus:
    try:
        os.stat(corpus_path+name)
        with open(corpus_path+name, 'rb') as f:
            corpora.append(pickle.load(f))
    except FileNotFoundError:
        # int to string
        with open(corpus_path+'kor_'+name, 'rb') as f:
            corpus = pickle.load(f)
        corpus = [[str(pid) for pid in line] for line in corpus]
        with open(corpus_path+'kor_'+name,'wb') as f:
            pickle.dump(corpus, f)
        with open(corpus_path+'eng_'+name, 'rb') as f:
            corpus = pickle.load(f)
        corpus = [[str(pid) for pid in line] for line in corpus]
        with open(corpus_path+'eng_'+name,'wb') as f:
            pickle.dump(corpus, f)
        # 한글&영문 corpus 병합
        with open(corpus_path+'kor_'+name, 'rb') as f:
            kor = pickle.load(f)
        with open(corpus_path+'eng_'+name, 'rb') as f:
            eng = pickle.load(f)
        merged = kor+eng
        with open(corpus_path+name, 'wb') as f:
            pickle.dump(merged, f)
        corpora.append(merged)