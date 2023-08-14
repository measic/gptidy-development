%%bash
OUTDIR=gs://${BUCKET}/taxifare/taxi_trained
JOBNAME=ml_live_$(date -u +%y%m%d_%H%M%S)
echo $OUTDIR $REGION $JOBNAME
gsutil -m rm -rf $OUTDIR
gcloud ml-engine jobs submit training $JOBNAME \
  --region=$REGION \
  --module-name=trainer.task \
  --package-path=${PWD}/taxifare/trainer \
  --job-dir=$OUTDIR \
  --staging-bucket=gs://$BUCKET \
  --scale-tier=STANDARD_1 \
  --runtime-version=$TFVERSION \
  -- \
  --train_data_paths="gs://${BUCKET}/taxifare/taxi_preproc/train.csv-00000-of-*" \
  --eval_data_paths="gs://${BUCKET}/taxifare/taxi_preproc/valid.csv-00000-of-*"  \
  --train_steps=5000 \
  --output_dir=$OUTDIR