# Use GCC image
FROM gcc:12.2.0

WORKDIR /app

# Copy C++ source code
COPY main.cpp .

# Compile the program
RUN g++ main.cpp -o myapp

# Run the program and keep the container alive for HTTP response
CMD ["./myapp"]
