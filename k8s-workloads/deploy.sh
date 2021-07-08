#/bin/sh

export KUBECONFIG=$KUBECONFIG:kubeconfig
# deploy
kubectl apply -f workloads.yml --kubeconfig ../infra/kubeconfig
