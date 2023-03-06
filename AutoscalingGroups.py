import os
import boto3

# access_key and secrete_key are set as environment variable and used
access_key = os.environ['aws_access_key_id']
secrete_key = os.environ['aws_secret_access_key']


def describe_asg():
    try:
        asg = boto3.client("autoscaling", region_name='ap-south-1')
# Fetching auto scaling group details
        asg_details = asg.describe_auto_scaling_groups(AutoScalingGroupNames=['lv-test-cpu'])

# Fetching desired capacity value
        desired_capacity_count = asg_details["AutoScalingGroups"][0].get('DesiredCapacity')

# Fetching number of instances running in ASG
        number_of_instances_running = len(asg_details["AutoScalingGroups"][0].get('Instances'))

# 1 . ASG desired running count should be same as running instances else assert
        if desired_capacity_count == number_of_instances_running:
            print("Number of instances running is same as desired count")
        else:
            print("ASG desired running count is not same as running instances")


# 2 if more than 1 instance running on ASG, then ec2 instance should on availble on multiple availibity zone.
        number_of_availability_zones = len(asg_details["AutoScalingGroups"][0].get('AvailabilityZones'))
        if number_of_instances_running > 1:
            if number_of_availability_zones > 1:
                print(number_of_instances_running, "instances running on ", number_of_availability_zones, "availability zones")
            else:
                print("ec2 instance is not available on multiple availability zones")
        else:
            print("No more than one instance is available")

# Fetching instance id details running on ASG
        i = 0
        instance_ids = []
        while i < number_of_instances_running:
            instance_id = asg_details["AutoScalingGroups"][0]['Instances'][i]['InstanceId']
            instance_ids.append(instance_id)
            i = i + 1

# Fetching instance details by calling ec2 client
        ec2 = boto3.client('ec2', region_name='ap-south-1')

# Checking imageId's of both the instance same or not
        image_id = []
        for item in instance_ids:
            describe_ec2 = ec2.describe_instances(InstanceIds=[item])
            ami = describe_ec2['Reservations'][0]['Instances'][0]['ImageId']
            image_id.append(ami)

        for i in range(len(image_id)):
            for j in range(i + 1, len(image_id)):
                if image_id[i] == image_id[j]:
                    print("Image id's of both the instance are same")
                else:
                    print("Image Id's are not same")

# Checking VPC id's of both the instance same or not
        vpc_id = []
        for item in instance_ids:
            describe_ec2 = ec2.describe_instances(InstanceIds=[item])
            vpc = describe_ec2['Reservations'][0]['Instances'][0]['VpcId']
            vpc_id.append(vpc)

        for i in range(len(vpc_id)):
            for j in range(i + 1, len(vpc_id)):
                if vpc_id[i] == vpc_id[j]:
                    print("Vpc id's are same")
                else:
                    print("Image Id's of both the instance are not same")

# Checking security group value's  of both the instance same or not
        security_grp = []
        for item in instance_ids:
            describe_ec2 = ec2.describe_instances(InstanceIds=[item])
            sgrp = describe_ec2['Reservations'][0]['Instances'][0]['VpcId']
            security_grp.append(sgrp)

        for i in range(len(security_grp)):
            for j in range(i + 1, len(security_grp)):
                if security_grp[i] == security_grp[j]:
                    print("Security groups values of both the instance are same")
                else:
                    print("security group values are not same")

    except Exception as e:
        print(e)


def main():
    describe_asg()


if __name__ == "__main__":
    main()
