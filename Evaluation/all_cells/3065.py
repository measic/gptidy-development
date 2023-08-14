%%bash
OUTDIR=gs://${BUCKET}/taxifare/taxi_hypertrain
JOBNAME=ml_live_hp_$(date -u +%y%m%d_%H%M%S)
echo $OUTDIR $REGION $JOBNAME
gsutil -m rm -rf $OUTDIR
gcloud ai-platform jobs submit training $JOBNAME \
   --region=$REGION \
   --module-name=trainer.task \
   --package-path=${PWD}/taxifare/trainer \
   --job-dir=$OUTDIR \
   --staging-bucket=gs://$BUCKET \
   --scale-tier=STANDARD_1 \
   --runtime-version=$TFVERSION \
   --config=hyperparam.yaml \
   -- \
   --train_data_paths="gs://${BUCKET}/taxifare/taxi_preproc/train.csv-00000-of-*" \
   --eval_data_paths="gs://${BUCKET}/taxifare/taxi_preproc/valid.csv-00000-of-*"  \
   --output_dir=$OUTDIR \
   --train_steps=2500