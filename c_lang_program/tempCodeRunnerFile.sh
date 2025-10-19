
echo "Creating Dockerfile..."
cat <<EOL > Dockerfile
# Use GCC image
FROM gcc:12.2.0