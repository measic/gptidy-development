from google.datalab.ml import TensorBoard
TensorBoard().start('gs://{}/babyweight/trained_model'.format(BUCKET))