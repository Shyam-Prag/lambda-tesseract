# lambda-tesseract

Run tesseract in an AWS Lambda using a Docker container. 

Steps:
1. Create a Cloud9 environment (I used a m5.large instance type) - We use Cloud9 as it runs on AL2 which helps to avoid any system level dependency issues. 
2. To avoid any "out of space" errors, increase the EBS volume size. (I increased from 10GB to 100GB)
3. Once the volume state is "in use", then reboot the EC2 instance.
4. Head back to Cloud9 and open the Cloud9 environment.

5. Inside the Cloud9 terminal, insert the following commands:

  5.1 sudo yum update
  
  5.2 sudo yum install docker
  
  5.3 sudo yum install gnupg2 
  
  5.4 mkdir lambda-pytesseract
  
  5.5 cd lambda-pytesseract
  
  5.6 vim Dockerfile
  
  #(insert Dockerfile script)
  
  5.7 vim requirements.txt
  
  #(insert requirements.txt script)
  
  5.8 vim example_docker_lambda.py
  
  #(insert example_docker_lambda.py script)
  
  5.9 aws configure 

  // In the above command, insert your access key and secret access key credentials. Cloud9 will throw a prompt. you can just hit 'cancel' and 'Re-enable after refresh'

6. Now in order to get the japanese.png image, I downloaded it from S3 using the below command:

  aws s3 cp s3://bucket/folder/japanese.png .

  #note the above command should be called once inside the lambda-pytesseract directory so that the image can be stored in the correct directory and subsequently in the   Docker container itself.

7. perform the ECR auth, docker build, tag and push commands 

8. This should succeed and you should now have your docker image inside ECR 

9. Create a Lambda container function and increase memory and timeout as desired. 

Note: All the above has been tested on Cloud9 which uses Amazon Linux 2 OS. This project provides a base to further implement your Tesseract business logic on AWS Lambda. This project is not fully optimized and is not the 'minimal requirements' to run Tesseract on Lambda, however is a fully functional working example. 
