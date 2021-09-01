### **CI best practices**


**Continuous Integration** (CI) is a development practice where developers integrate code into a shared repository frequently, preferably several times a day. Each integration can then be verified by an automated build and automated tests. While automated testing is not strictly part of CI it is typically implied.

One of the key benefits of integrating regularly is that you can detect errors quickly and locate them more easily. As each change introduced is typically small, pinpointing the specific change that introduced a defect can be done quickly.

- Optimize CI pipeline speed
- Filter jobs on tags / branch names
- Automate testing and deployment
- Split jobs for different stages
- Cache tools and job dependencies

### **Github actions best practices**

- Keep actions small and fast
- Add additional security to protect workflow from changes
- Store secrets using Github secrets
- In public repos do not use self-hosted runners
- Protect script from injections

### **Jenkins best practices**

- Run inside jobs via docker agent
- Setup Github credentials for protection

![alt text](https://github.com/TopIvanAbramov/DevOps/blob/main/Images/jenkins.png)
