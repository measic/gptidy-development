%%bash

OUTDIR=gs://${BUCKET}/taxifare/feateng
JOBNAME=mllive_$(date -u +%y%m%d_%H%M%S)
TIER=STANDARD_1 
echo $OUTDIR $REGION $JOBNAME
#gsutil -m rm -rf $OUTDIR
gcloud ml-engine jobs submit training $JOBNAME \
   --region=$REGION \
   --module-name=trainer.task \
   --package-path=${PWD}/taxifare/trainer \
   --job-dir=$OUTDIR \
   --staging-bucket=gs://$BUCKET \
   --scale-tier=$TIER \
   --runtime-version=$TFVERSION \
   -- \
   --train_data_paths="gs://${BUCKET}/taxifare/taxi_preproc/train.csv-00001-of-*" \
   --eval_data_paths="gs://${BUCKET}/taxifare/taxi_preproc/valid.csv-00000-of-*"  \
   --output_dir=$OUTDIR \
   --train_steps=8000 \
   --train_batch_size=512 --nbuckets=16 --hidden_units="64 64 64 8"