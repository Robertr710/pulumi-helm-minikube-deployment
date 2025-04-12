import pulumi
from pulumi_kubernetes.helm.v3 import Chart, LocalChartOpts

# Deploy the local Helm chart using defaults from values.yaml
chart = Chart(
    "helm-chart",
    LocalChartOpts(
        path="../helm-chart"
        # no need to include `values` if you're fine with defaults
    )
)

pulumi.export("name", chart._name)
