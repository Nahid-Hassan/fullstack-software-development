# DevOps

## Table of Contents

- [DevOps](#devops)
  - [Table of Contents](#table-of-contents)
    - [Introduction and Overview](#introduction-and-overview)
    - [Why DevOps](#why-devops)
    - [How DevOps Works](#how-devops-works)
    - [DevOps Tools](#devops-tools)
    - [Git](#git)
      - [Introduction to Git](#introduction-to-git)

### Introduction and Overview

- **Git**
- **Docker**
  - What Is Docker Swarm
  - Configuration And Management
    - Puppet, Ansible
- **Software Testing**
  - Selenium
- Continuous Integration(**CI**)
  - Jenkins
- **Kubernetes**
- **Continuos Monitoring**
  - Nagios

### Why DevOps

![images](images/1.png)

![images](images/2.png)

![images](images/3.png)

![images](images/4.png)

![images](images/5.png)

![images](images/6.png)

![images](images/7.png)

### How DevOps Works

So, by definition,

> **DevOps** is a software **methodology** which improves the **collaboration** between `developers and operations team` using various **tools**. These `automation tools` are implemented using various stages which are a part of the **DevOps Lifecycle**.

![images](images/8.png)

> **Plan** --> **Code** --> **Build** --> **Test** --> **Release(IR, ER)** --> **Deploy(server)** --> **Operate** --> **Monitor(log)**.

> There is no `perfect release`.

![images](images/9.png)

![images](images/10.png)

- **Continuous Development**:

> This stage involves committing code to version control system tools such as **Git** or **SVN** for maintaining the different versions fo the code, and tools like **Ant**, **Maven**, **Gradle** for `building/packaging` the code into an executable file that can be forwarded to the QAs for Testing.

- **Continuous Integration**:

> This stage is a `critical point` in the whole **Devops** lifecycle. It deals with integrating the different stages of the devops lifecycle, and is therefore the key in automating the whole devops process.

- **Continuous Deployment**:

> In this stage the code is **built**, the **environment** or the **application** is **containerized** and is `pushed` on to the desired **server**. The key processes in this stage are **configuration management**, **virtualization** and **containerization**.

- **Continuous Testing**:

> The stage deals with automated **testing** of the application pushed by the developer. If there is an **error**, the message is `sent back to the integration tool`, this tool in turn notifies the developer of the error. If the test was a success, the message is sent to integration tool which pushes the build on the production server.

- **Continuous Monitoring**:

> This stage continuously monitors the deployed application for **bugs** or **crashes**. It can also be setup to collect **users** feedback. The collected data is then sent to the developers to **improve** the application.

### DevOps Tools

![images](images/11.png)

- **Continuous Development**:

![images](images/12.png)

- **Continuous Integration**:

![images](images/13.png)

- **Continuous Deployment**:

![images](images/14.png)

- **Continuous Testing**:

![images](images/15.png)

- **Continuous Monitoring**:

![images](images/16.png)

**Final Overview**:

![images](images/17.png)

 
### Git

#### Introduction to Git