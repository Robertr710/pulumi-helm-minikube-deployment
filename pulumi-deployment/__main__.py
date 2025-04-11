import pulumi
from pulumi_kubernetes.helm.v3 import Chart, LocalChartOpts

# Deploy the local Helm chart
chart = Chart(
    "helm-chart",  # This is the Pulumi resource name (not Helm release name)
    LocalChartOpts(
        path="../helm-chart",  # Path to your local Helm chart directory
        values={
            "replicaCount": 1,
            "image": {
                "repository": "hello-python",  # This must match your Docker image name
                "pullPolicy": "IfNotPresent",
                "tag": "latest",
            },
            "service": {
                "type": "ClusterIP",
                "port": 80,
                "targetPort": 3000,
            },
        },
    )
)

# Optional export for Pulumi console
pulumi.export("name", chart._name)


