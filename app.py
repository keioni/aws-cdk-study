#!/usr/bin/env python3

from aws_cdk import core

from aws_cdk_study.aws_cdk_study_stack import CdkworkshopStack


app = core.App()
CdkworkshopStack(app, "aws-cdk-study", env={'region': 'us-west-2'})

app.synth()
