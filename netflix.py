import boto3  
import time  

myec2 = boto3.client('ec2',  
    region_name="us-east-2",  
    aws_access_key_id="Your_Access_Key",  
    aws_secret_access_key="Your_Secret_Key"
    )

def launch_ec2():  
    response = myec2.run_instances(  
        ImageId="ami-002acc74c401fa86b",  
        InstanceType="t2.micro",  
        MinCount=1,  
        MaxCount=1,  
          
    )  
    instance_id = response['Instances'][0]['InstanceId']  
    print(f"Launched Instance: {instance_id}")  
    return instance_id  

# Monitor instance usage (mocking a traffic spike detection)  
def monitor_traffic():  
    print("Monitoring traffic...")  
    time.sleep(2)  # Simulate waiting for a traffic spike  
    return "HIGH"  # Simulated traffic level  

def terminate_ec2(instance_id):  
    myec2.terminate_instances(InstanceIds=[instance_id])  
    print(f"Terminated Instance: {instance_id}")  


# Workflow: Simulating dynamic scaling  
traffic_status = monitor_traffic()  
if traffic_status == "HIGH":  
    instance_id = launch_ec2()  
    time.sleep(5)  # Simulate usage during high traffic  
    terminate_ec2(instance_id)  
else:  
    print("Traffic is normal, no action required.")  
