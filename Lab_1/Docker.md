### **Dockerfile best practices**

- Use .dockerignore to exclude unnecessary files 
- Don’t install unnecessary packages, use light base image
- Minimize the number of layers
- Leverage build cache (Use --no-cache-dir)
- Use linter to apply best practice to Docker images
- Prevent confidential data leaks (Do not put any credentials, use COPY over ADD)