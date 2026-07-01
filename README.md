# Lambda Logs

A simple lambda service to log the different log levels.

## Prerequisites

* An AWS account - a [sandbox](https://www.whizlabs.com/labs/sandbox/aws/aws-sandbox) account works as well.
* AWS CLI - you will also need to configure it with your credentials.
* AWS SAM CLI - the CLI tool used to build and deploy the application.
* Python 3.14 - required for building the application.
* Docker (optional) - only if you want to test it locally.

## Install and configure dependencies

Install AWS CLI

```sh
brew install awscli
```

You will also need to configure your AWS CLI to add your credentials.

```sh
aws configure
```

Install AWS SAM CLI

```sh
brew install aws-sam-cli
```

## Validate the template

This checks to see if the `template.yaml` file is valid.

```sh
sam validate
```

## Build the project

This will compile the project into a `.aws-sam` folder.

```sh
sam build
```

## Test the application

This will spin up a Docker container to test the application locally. You can go to https://localhost:3000/greet to see it in action.

```sh
sam local start-api
```

## Invoke the function

Invoke the function locally. You should see the return message from the Lambda function.

```sh
sam local invoke <name-of-your-function>
```

## Invoke the function with event parameters

To invoke the function for log level `debug`.

```sh
sam local invoke LogLevelFunction -e events/debug.json
```

## Deploy the application

This will deploy the application based on the configuration in `samconfig.toml`.

```sh
sam deploy
```

## Destroy the application

This will destory the application and its infrastructure.

```sh
sam delete
```

