# Single Service Deploy

This repository represents a toy project of a bitcoin price miner application
hosted on an Azure AKS cluster. The example is not fully functional
(as the docker image is not published on a public registry) but it
is still useful to guide a discussion around the three main components:
- Infrastructure
- Application
- Deployment


## Infrastructure
The code to create infrastructure can be found under
the **infra** directory.
There is also a basic script that automates the
infrastructure provisioning using terraform

## Application
The application can be found under the **app** dir and is a
python script that loops indefinitely to retrieve the current bitcoin
price in USD. This is then displayed on a (basic)
HTML page, generated from a template and served using a python
simple http server (not to be used in production).

A very basic Dockerfile is also provided together with a `build.sh`
to build, test, scan and publish the application as a docker image.

## Deployment
In the **k8s-workloads** directory a k8s manifest has been included
that deploys the app image as a k8s deployment and exposes it
as a service. There is also a deploy script to deploy the same
manifest using the k8s CLI, `kubectl`


## Improvements
- the App build and publish script provided should be turned into a proper
pipeline and have proper semantic version
- The infrastructure should have a proper pipeline too -
with syntactic/security validation and testing but also with environment management (i.e. terragrunt)
- The k8s manifest should be turned into a helm chart (version support,
  release history, testing)
