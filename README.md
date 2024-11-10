# JungleRun
My CI/CD Pipeline *Finished*

As of now currently, my CI/CD pipeline has automated all steps bar the deployment onto a cluster. I've highlighted the steps below.
1) Application gets uploaded.
2) Basic test is ran.
3) Once all tests are ran the image is pushed to ECR
4) Image then at this stage would typically be pulled to the ECS/EKS and the deployment would be done automatically **READ BELOW**

Due to the sensitivity of my Terraform file I have decided not to automate this stage till I have a better understanding so currently using Terraform to deploy manually.