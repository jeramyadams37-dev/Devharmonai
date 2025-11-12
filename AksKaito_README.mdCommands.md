# Set up resource group
export RANDOM_ID="$(openssl rand -hex 3)"
export AZURE_RESOURCE_GROUP="myKaitoResourceGroup$RANDOM_ID"
export REGION="centralus"
export CLUSTER_NAME="myClusterName$RANDOM_ID"

az group create \
    --name $AZURE_RESOURCE_GROUP \
    --location $REGION \

# Install the Azure CLI preview extension
az extension add --name aks-preview
az extension update --name aks-preview

# Register the AI toolchain operator add-on feature flag
az feature register --namespace "Microsoft.ContainerService" --name "AIToolchainOperatorPreview"

# Verify the AI toolchain operator add-on registration
while true; do
    status=$(az feature show --namespace "Microsoft.ContainerService" --name "AIToolchainOperatorPreview" --query "properties.state" -o tsv)
    if [ "$status" == "Registered" ]; then
        break
    else
        sleep 15
    fi
done

# Create an AKS cluster with the AI toolchain operator add-on enabled
az aks create --location ${REGION} \
    --resource-group ${AZURE_RESOURCE_GROUP} \
    --name ${CLUSTER_NAME} \
    --enable-oidc-issuer \
    --node-os-upgrade-channel SecurityPatch \
    --auto-upgrade-channel stable \
    --enable-ai-toolchain-operator \
    --generate-ssh-keys \
    --k8s-support-plan KubernetesOfficial

# Connect to your cluster
az aks get-credentials --resource-group ${AZURE_RESOURCE_GROUP} --name ${CLUSTER_NAME}

# Establish a federated identity credential
export MC_RESOURCE_GROUP=$(az aks show --resource-group ${AZURE_RESOURCE_GROUP} \
    --name ${CLUSTER_NAME} \
    --query nodeResourceGroup \
    -o tsv)
export KAITO_IDENTITY_NAME="ai-toolchain-operator-${CLUSTER_NAME}"
export AKS_OIDC_ISSUER=$(az aks show --resource-group "${AZURE_RESOURCE_GROUP}" \
    --name "${CLUSTER_NAME}" \
    --query "oidcIssuerProfile.issuerUrl" \
    -o tsv)

az identity federated-credential create --name "kaito-federated-identity" \
    --identity-name "${KAITO_IDENTITY_NAME}" \
    -g "${MC_RESOURCE_GROUP}" \
    --issuer "${AKS_OIDC_ISSUER}" \
    --subject system:serviceaccount:"kube-system:kaito-gpu-provisioner" \
    --audience api://AzureADTokenExchange

# Verify that your deployment is running
kubectl rollout restart deployment/kaito-gpu-provisioner -n kube-system

# Deploy a default hosted AI model
kubectl apply -f https://raw.githubusercontent.com/Azure/kaito/main/examples/inference/kaito_workspace_falcon_7b-instruct.yaml

# Ask a question
echo "See last step for details on how to ask questions to the model."

