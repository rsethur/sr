# Setup and run MLOps pipelines from this repo

## Prerequisite

## Step 1: Fork this repo
You can [fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository) from github.com.

## Step 2: Set the required environment variables for the pipelines to work
In Github action you need to use secrets to set environment variables. These variables will be used in the various pipelines.
In your forked repository, create the following [repository level `secrets`](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository) :

Secret | Description/Instructions |
|------|------------|
|SUBSCRIPTION_ID | Your azure subscription id |
|RESOURCE_GROUP | Resource group where your resources will be created. Make sure this already exists |
| AML_WORKSPACE | Name of your azure ml workspace. If it does not already exist, a new one will be created. e.g. mlops |
| LOCATION | Azure region for your Azure ML workspace  e.g. eastus |
| LA_WORKSPACE | Name of your azure ml workspace. If it does not already exist, a new one will be created. e.g. mlops-la-ws. **Note** that underscore is not allowed in the name. |
| LA_LOCATION | Azure region for your log analytics workspace  e.g. eastus. Ideally same as `LOCATION`. This is a seperate variable than `LOCATION` because log analytics is not avaialble in all regions. |
| ENDPOINT_NAME | Name of the managed online endpoint that will be created part of the pipelines. This needs to be a unique value across azure region level. For e.g my-endpt-<XXXXX>, where XXXXX is a random number. |

## Step 3: Create Service Principal and add it to the Secrets

A service principal (SP) is needed inorder for your github actions pipelines to create and modify resources. Prerequsite to create a is that you have either `Owner` or `User access administrator` role at the subscription level. If you do not have it, ask your admin to execute the steps.

Create a SP and add it to the repository `secrets` named `AZURE_CREDENTIALS` by following instructions [here](https://github.com/marketplace/actions/azure-login#configure-deployment-credentials). Ignore the option to create SP for webapp, and just do it for `resource group`.

## Setup your workspace

[Run](https://docs.github.com/en/actions/managing-workflow-runs/manually-running-a-workflow) the `Setup` github action pipeline to finish the setup.
This will create the following resources:
1. Azure ML workspace, if it does not already exists
2. Log analytics workspace (used for managed online endpoints)
3. Training cpu-cluster
4. A sample dataset for training

## Get started!
Now you are all set! Go to the [getting started](getting-started.md) to try out the mlops pipelines

## Delete resources
Once you are done, [delete the resource group](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/manage-resource-groups-portal#delete-resource-groups) (or the azure ml workspace and other resources created from the pipelines) inorder to avoid any charges.

