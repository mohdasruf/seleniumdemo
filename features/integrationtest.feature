# Created by User at 07/04/2020
Feature: Sample integration test Demo

  Scenario: Download input file from S3 and trigger a python script
    Given I download the input file from S3 and place it in the test files folder
    And trigger the python script
    Then the output is as expected

  @datalake
  Scenario: Download input file from S3 and compare with the expected output
    Given I download the input file and place it in the test files folder
    And compare with the expected output
    Then the output is correct

  @ENV
  Scenario Outline: Example scenario for tagging
    Given I download the input file from S3 and place it in the test files folder
    And read the input "<input>"
    Then the output is as expected "<output>"
    @ENV1
    Examples:
      | input | output |
      | 10    | 10     |
      | 20    | 20     |
    @ENV2
    Examples:
      | input | output |
      | 30    | 30     |
      | 40    | 40     |
