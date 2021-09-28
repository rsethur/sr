# Getting started

1. Complete the [setup](setup.md)
1. Run the `train` github action. This job will train the model based on the dataset and register it. This will automatically trigger the `auto-saferollout` github action. In the first run it will create the endpoint and first version of the deployment

1. Run the above action again. This time it run jobs to gradually rollout traffic to this new version of deployment.

You can keep running with the `train` or the `auto-saferollout` actions to rollout new versions. You can also configure this to run on a schedule.
