%bash
echo "bucket=${BUCKET}"
rm -rf babyweight_trained
export PYTHONPATH=${PYTHONPATH}:${PWD}/babyweight
python -m trainer.task \
   --bucket=${BUCKET} \
   --output_dir=babyweight_trained \
   --job-dir=./tmp \
   --pattern="00001-of-" --train_steps=1000