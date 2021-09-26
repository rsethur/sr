export TRAINING_JOB=risk-model-job-`echo $RANDOM`
# run the training job
az ml job create -f train/job.yml -n $TRAINING_JOB
# download the job output
az ml job download -n $TRAINING_JOB -p run-outputs
# register model
MODEL_VERSION=$(az ml model create -n ${{ env.MODEL_NAME }} -l run-outputs/$TRAINING_JOB/outputs/risk_model.joblib | jq -r .version)
#write model name and version to file
export MODEL_NAME_WITH_VERSION=azureml:${{ env.MODEL_NAME }}:$LATEST_MODEL_VERSION
echo $MODEL_NAME_WITH_VERSION > latest-model.txt