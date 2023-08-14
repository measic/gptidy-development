%%bash

WARNING -- this uses significant resources and is optional. Remove this line to run the block.

OUTDIR=gs://${BUCKET}/taxifare/feateng2m
JOBNAME=mllivexl_$(date -u +%y%m%d_%H%M%S)
TIER=STANDARD_1 
echo $OUTDIR $REGION $JOBNAME
# only remove the outdir if you don't want to resume a previous run
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
   --train_data_paths="gs://${BUCKET}/taxifare/taxi_preproc/train*" \
   --eval_data_paths="gs://${BUCKET}/taxifare/taxi_preproc/valid*"  \
   --output_dir=$OUTDIR \
   --train_steps=1600000 \
   --train_batch_size=512 --nbuckets=16 --hidden_units="64 64 64 8"