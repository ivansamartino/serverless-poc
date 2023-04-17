# Getting started

Clone the serverless offline fork you are working in, somewhere in your file
system. Navigate to that directory and run `npm link`

Then navigate to this directory and run: `npm link serverless-offline`

Ensure that in the serverless.yml you are referencing the plugin:

```yaml
plugins:
  - serverless-offline
```

Ensure that you run the following from a valid terminal with AWS credentials so
that `serverless-offline` plugin is able to download the public AWS layers

```bash
serverless offline --debug
```

From another terminal window:

```bash
aws lambda invoke /dev/stdout \
    --endpoint-url http://localhost:3002 \
    --function-name offline-test-dev-hello
```
