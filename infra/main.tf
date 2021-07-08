terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=2.57.0"
    }
  }
}

provider "azurerm" {
  features {}

}

resource "azurerm_resource_group" "tf-rg" {
  name     = "aks-cluster"
  location = "West Europe"
}

resource "azurerm_kubernetes_cluster" "tf-cluster" {
  name                = "aks-cluster"
  location            = azurerm_resource_group.tf-rg.location
  resource_group_name = azurerm_resource_group.tf-rg.name
  dns_prefix          = "aks-cluster"

  default_node_pool {
    name       = "default"
    node_count = 2
    vm_size    = "Standard_D2_v2"
  }

  network_profile {
    network_plugin    = "azure"
    network_policy    = "calico"
  }

  identity {
    type = "SystemAssigned"
  }

  addon_profile {
    http_application_routing {
      enabled = true
    }
  }

  role_based_access_control {
    enabled = true
  }

  tags = {
    Environment = "Test"
  }

}

resource "local_file" "kubeconfig" {
  depends_on   = [azurerm_kubernetes_cluster.tf-cluster]
  filename     = "kubeconfig"
  content      = azurerm_kubernetes_cluster.tf-cluster.kube_config_raw
}
