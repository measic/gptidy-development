%%bash
if [ -d sample ]; then
  rm -rf sample
fi
mkdir sample

gsutil cp "gs://$BUCKET/taxifare/taxi_preproc/train.csv-00000-of*" sample/train.csv
gsutil cp "gs://$BUCKET/taxifare/taxi_preproc/valid.csv-00000-of*" sample/valid.csv
wc -l sample/*