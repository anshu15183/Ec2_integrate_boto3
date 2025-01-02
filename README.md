# AWS EC2 Automation with Boto3

This project demonstrates how to use Python's Boto3 library to automate the creation and termination of AWS EC2 instances. The script provides a simple workflow for managing EC2 instances programmatically, which can be extended for various use cases such as scaling applications or testing environments.

---

## Features

- **Launch EC2 Instances**: Automatically create EC2 instances with predefined configurations.
- **Terminate EC2 Instances**: Programmatically shut down instances when no longer needed.
- **Cost Optimization**: Ensure efficient use of resources by automating instance lifecycles.

---

## Prerequisites

1. **AWS Account**: Ensure you have an active AWS account.
2. **AWS Credentials**: Access key and secret key with permissions to manage EC2 instances.
3. **Python**: Python 3.x installed on your local machine.
4. **Boto3 Library**: Install Boto3 using pip:
   ```bash
   pip install boto3
   ```

---

## Setup Instructions

1. Clone this repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd aws-boto3-ec2
   ```
3. Update the script with your AWS credentials:
   ```python
   myec2 = boto3.client('ec2',
                        region_name="us-east-2",
                        aws_access_key_id="Your_Access_Key",
                        aws_secret_access_key="Your_Secret_Key")
   ```

---

## Usage

### Launch an EC2 Instance
Run the script to launch an EC2 instance:
```bash
python ec2_automation.py
```
This will create an EC2 instance using the specified AMI ID and instance type, and print the instance ID.

### Terminate an EC2 Instance
Update the script with the instance ID you want to terminate and run the function:
```python
def terminate_ec2(instance_id):
    myec2.terminate_instances(InstanceIds=[instance_id])
    print(f"Terminated Instance: {instance_id}")
```

---

## Example Workflow

1. Launch an EC2 instance:
   ```python
   instance_id = launch_ec2()
   ```
   Output:
   ```
   Launched Instance: i-0abcd1234efgh5678
   ```

2. Terminate the EC2 instance:
   ```python
   terminate_ec2(instance_id)
   ```
   Output:
   ```
   Terminated Instance: i-0abcd1234efgh5678
   ```

---

## Applications

- **Dynamic Scaling**: Automatically provision resources during peak demand.
- **Cost Control**: Shut down unused resources to minimize expenses.
- **Testing Environments**: Quickly spin up and tear down test infrastructure.

---

## Notes

- Ensure proper IAM permissions are assigned to the credentials being used.
- Use `.env` files or AWS Secrets Manager to secure sensitive credentials.
- Always validate configurations before running scripts in production.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact
For any questions or suggestions, feel free to reach out:
- **Name**: Anshu Singh
- **Email**: [your_email@example.com]

---

Happy Coding! 🚀
