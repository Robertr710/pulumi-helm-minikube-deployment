import pulumi
from pulumi_kubernetes.helm.v3 import Chart, LocalChartOpts

# Get the current Pulumi stack name (e.g., "dev" or "prd")
stack = pulumi.get_stack()

# Define custom overrides based on the stack. Overrides is my dictionary. 
overrides = {
    "fullnameOverride": f"hello-python-{stack}",
    "stack": stack,
}

# Optionally add prd-specific overrides using a dictionary update method
if stack == "prd":
    overrides.update({
        "replicaCount": 3,
    })

# Deploy the local Helm chart
chart = Chart(
    "helm-chart",
    LocalChartOpts(
        path="../helm-chart",
        values=overrides
    )
)

# Export the name for reference
pulumi.export("name", chart._name)
