#/bin/sh

terraform init
terraform plan -out=tf_plan.out
# remember to setenv.sh
terraform apply tf_plan.out
