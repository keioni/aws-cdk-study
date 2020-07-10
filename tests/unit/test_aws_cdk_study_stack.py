import json
import pytest

from aws_cdk import core
from aws-cdk-study.aws_cdk_study_stack import AwsCdkStudyStack


def get_template():
    app = core.App()
    AwsCdkStudyStack(app, "aws-cdk-study")
    return json.dumps(app.synth().get_stack("aws-cdk-study").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
