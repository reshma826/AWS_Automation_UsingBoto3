Verefying Testcase A and B on AWS autoscalin group using Boto3 and AWS CLI

programing language used : Python

Testcase:- A
  1- ASG desire running count should be same as running instances. if mismatch fails
  2- if more than 1 instance running on ASG, then ec2 instance should on available and distributed on multiple availibity zone.
  3- SecuirtyGroup, ImageID and VPCID should be same on ASG running instances. Do not just print.
  4- Findout uptime of ASG running instances and get the longest running instance.
Testcase:- B
  Find the Scheduled actions of given ASG which is going to run next and calcalate elapsed in hh:mm:ss from current time.
  Calculate total number instances lunched and terminated on current day for the given ASG.

To install boto3 : "pip install boto3"
Set aws region: "aws set --region <region-name>"
set aws access key

Command to execute testcases : python autoscaling.py
