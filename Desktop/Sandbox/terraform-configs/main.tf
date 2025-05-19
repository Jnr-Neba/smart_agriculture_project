terraform{
  required_providers {
    minikube = {
      source  = "scott-the-programmer/minikube"
      version = "0.5.0"
    }
  }
}

provider "minikube" {
  kubernetes_version = "v1.30.0"
}

resource "minikube_cluster" "minikube_docker" {
  driver       = "docker"
  cluster_name = "Sandbox"

  addons = [
    "default-storageclass",
    "storage-provisioner"
  ]
}


