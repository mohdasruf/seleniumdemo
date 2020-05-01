import json

from behave import *
import boto3
from configparser import ConfigParser

use_step_matcher("re")


@given("I download the input file from S3 and place it in the test files folder")
def step_impl(context):
    config_object = ConfigParser()
    config_object.read("config.ini")
    context.s3 = boto3.client('s3')
    filedetails = config_object["FILEDETAILS"]
    context.bucket_name = filedetails["bucketname"]
    context.s3_file_path = filedetails["s3_file_path"]
    context.save_as = filedetails["save_as"]
    context.s3.download_file(context.bucket_name, context.s3_file_path, context.save_as)
    print('Successfully placed it in the folder')


@then("the output is as expected")
def step_impl(context):
    assert (context.output == ['Test File'])


@step('read the input "(?P<input>.+)"')
def step_impl(context, input):
    context.input = input
    print('input is ', input)


@then('the output is as expected "(?P<output>.+)"')
def step_impl(context, output):
    assert (output == context.input)
    print('output is ', output)


@given(u'I download the input file and place it in the test files folder')
def step_impl(context):
    config_object = ConfigParser()
    config_object.read("config.ini")
    context.s3 = boto3.client('s3')
    filedetails = config_object["FILEDETAILS"]
    context.bucket_name = filedetails["bucketname"]
    context.s3_file_path = filedetails["s3_file_path1"]
    context.save_as = filedetails["save_as1"]
    context.s3.download_file(context.bucket_name, context.s3_file_path, context.save_as)


@given(u'compare with the expected output')
def step_impl(context):
    with open("expected/expectedoutput.json", "r") as f:
        data1 = f.readlines()
    with open("expected/inputfile.json", "r") as f:
        data2 = f.readlines()
    assert (data1 == data2)


@then(u'the output is correct')
def step_impl(context):
    print('all is well')
