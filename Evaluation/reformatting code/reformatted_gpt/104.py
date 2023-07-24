bash
model_dir=$(gsutil ls gs://${BUCKET}/taxifare/feateng2m/export/exporter | tail -1)
gcloud ml-engine local predict \
  --model-dir=${model_dir} \
  --json-instances=/tmp/test.json