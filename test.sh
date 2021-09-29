LATEST_MODEL_VERSION=$(az ml model show -n risk-model -o tsv --query version)
MODEL=azureml:risk-model:$LATEST_MODEL_VERSION

