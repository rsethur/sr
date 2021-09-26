export TRAINING_JOB=risk-model-job-`echo $RANDOM`
# run the training job
az ml job create -f train/job.yml -n $TRAINING_JOB --web
# download the job output
az ml job download -n $TRAINING_JOB -p run-outputs
# register model

