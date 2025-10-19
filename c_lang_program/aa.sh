#!/bin/bash

# -------------------------------------------
# All-in-One C++ Deployment with Output
# -------------------------------------------

# Variables – customize as needed
NAMESPACE="mynamespace"
APP_NAME="cppapp"
PROJECT_NAME="cppproject"
REGION="us"
IMAGE_TAG="latest"

# 1. Login to IBM Cloud
echo "Logging in to IBM Cloud..."
ibmcloud login --no-region
ibmcloud cr login

# 2. Create Container Registry namespace if it doesn't exist
if ! ibmcloud cr namespaces | grep -q "$NAMESPACE"; then
    echo "Creating namespace $NAMESPACE..."
    ibmcloud cr namespace-add $NAMESPACE
fi

# 3. Create a C++ program with output
echo "Creating C++ program..."
cat <<EOL > main.cpp
#include <iostream>

int main() {
    std::cout << "Hello from IBM Code Engine! This is your C++ app running in a container." << std::endl;
    return 0;
}
EOL

# 4. Create Dockerfile
echo "Creating Dockerfile..."
cat <<EOL > Dockerfile
# Use GCC image
FROM gcc:12.2.0

WORKDIR /app

# Copy C++ source code
COPY main.cpp .

# Compile the program
RUN g++ main.cpp -o myapp

# Run the program and keep the container alive for HTTP response
CMD ["./myapp"]
EOL

# 5. Build Docker image
echo "Building Docker image..."
docker build -t $APP_NAME:$IMAGE_TAG .

# 6. Tag Docker image for IBM Cloud Container Registry
docker tag $APP_NAME:$IMAGE_TAG $REGION.icr.io/$NAMESPACE/$APP_NAME:$IMAGE_TAG

# 7. Push Docker image
echo "Pushing Docker image to IBM Cloud Container Registry..."
docker push $REGION.icr.io/$NAMESPACE/$APP_NAME:$IMAGE_TAG

# 8. Create Code Engine project
ibmcloud ce project create --name $PROJECT_NAME || echo "Project may already exist"
ibmcloud ce project select --name $PROJECT_NAME

# 9. Deploy application on Code Engine
echo "Deploying application to IBM Code Engine..."
ibmcloud ce application create \
    --name $APP_NAME \
    --image $REGION.icr.io/$NAMESPACE/$APP_NAME:$IMAGE_TAG \
    --cpu 0.5 \
    --memory 512M \
    --max-scale 1

# 10. Get application URL
APP_URL=$(ibmcloud ce application get --name $APP_NAME --output json | jq -r '.status.url')
echo "Application deployed! Open the URL in your browser to see the output:"
echo $APP_URL