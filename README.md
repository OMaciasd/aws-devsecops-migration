# 🚀 DevSecOps Migration Project to AWS

This project focuses on migrating a legacy DevOps pipeline to a robust DevSecOps architecture using AWS services. It addresses challenges in scalability, security, and CI/CD automation while maintaining compliance and operational efficiency.

## 🗂️ Table of Contents

- [🚀 DevSecOps Migration Project to AWS](#-devsecops-migration-project-to-aws)
  - [🗂️ Table of Contents](#️-table-of-contents)
  - [📖 Project Description](#-project-description)
    - [🎯 Objectives](#-objectives)
    - [📂 Project Structure](#-project-structure)
  - [🌐 AWS DevSecOps Migration Project](#-aws-devsecops-migration-project)
  - [✅ Requirements](#-requirements)
  - [🔧 Installation and Setup](#-installation-and-setup)
    - [Clone the Repository](#clone-the-repository)
  - [🛠️ Setup Instructions](#️-setup-instructions)
    - [Setup AWS Infrastructure](#setup-aws-infrastructure)
  - [📦 Migrate Jenkins Pipelines to AWS CodePipeline](#-migrate-jenkins-pipelines-to-aws-codepipeline)
  - [🔄 Migration Script](#-migration-script)
  - [⚙️ AWS DevSecOps Pipeline Overview](#️-aws-devsecops-pipeline-overview)
  - [📋 Phases and Tools Comparison](#-phases-and-tools-comparison)
  - [📈 Benefits](#-benefits)
  - [🏗️ Architecture](#️-architecture)
  - [🤝 Contributing](#-contributing)
  - [📜 License](#-license)

---

## 📖 Project Description

This project enables the transition of legacy CI/CD pipelines to a modern DevSecOps environment on AWS. It ensures secure, automated, and scalable workflows for development and operations while incorporating advanced monitoring, threat detection, and policy management.

### 🎯 Objectives

1. **Address Scalability**: Ensure that the pipeline can handle increased workload and repository growth.
2. **Strengthen Security**: Introduce comprehensive security measures throughout the CI/CD lifecycle.
3. **Automate Processes**: Eliminate manual interventions in build, test, and deployment stages.

---

### 📂 Project Structure

  ```plaintext
  .
  ├── docs/
  │   ├── guides/
  │   │   ├── ARCHITECTURE.md
  │   │   └── CONTRIBUTING.md
  │   │   └── bootcamp-devsecops.pdf
  ├── scripts/
  │   └── migrate_jenkins_to_codepipeline.py
  │   ├── setup_aws_resources.sh
  ├── README.md

  ```

---

## 🌐 AWS DevSecOps Migration Project

 This project facilitates the migration of DevSecOps pipelines from legacy tools to AWS-native services. It leverages Terraform for infrastructure provisioning, Python for automation, and AWS services for CI/CD, security, and monitoring.

---

## ✅ Requirements

- 🖥️ **[AWS CLI](https://aws.amazon.com/cli/)**: Manage AWS resources.
- 🌐 **[Terraform](https://www.terraform.io/)**: Automate infrastructure provisioning.
- 📦 **[Git](https://git-scm.com/)**: For version control.
- 🐍 **[Python](https://www.python.org/)**: Scripting for additional configuration.
- 🔍 **[SonarQube](https://www.sonarqube.org/)**, **[Snyk](https://snyk.io/)**, **[Trivy](https://aquasecurity.github.io/trivy/)**: Legacy tools for code analysis and security scanning.
- 🚀 **[AWS Tools](https://aws.amazon.com/products/)**: CodePipeline, CodeBuild, Security Hub, WAF, GuardDuty, and more.

---

## 🔧 Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/omaciasd/aws-devsecops-migration.git
cd aws-devsecops-migration/

```

---

## 🛠️ Setup Instructions

### Setup AWS Infrastructure

Run the Terraform scripts located in the `terraform/` directory:

```bash
terraform init
terraform apply

```

---

## 📦 Migrate Jenkins Pipelines to AWS CodePipeline

This guide provides a structured approach for migrating existing Jenkins pipelines to AWS CodePipeline, leveraging AWS-native tools to improve scalability, security, and CI/CD automation.

---

## 🔄 Migration Script

Use the provided Python script to migrate existing pipelines to AWS CodePipeline:

```bash
python scripts/migrate_jenkins_to_codepipeline.py

```

---

## ⚙️ AWS DevSecOps Pipeline Overview

## 📋 Phases and Tools Comparison

| Phase           | Legacy                         | AWS                                                            |
|-----------------|--------------------------------|----------------------------------------------------------------|
| **Planning**    | GitLab                         | AWS IAM                                                        |
| **Development** | SonarQube, GitLab, Snyk, Trivy | Amazon CodeGuru, Amazon Inspector                              |
| **Integration** | Jenkins (SonarQube)            | AWS CodePipeline, AWS CodeBuild, Lambda                        |
| **Deployment**  | Jenkins                        | AWS CodeDeploy, Elastic Beanstalk, ECS/EKS, AWS CLOUDFORMATION |
| **Operation**   | GitLab, SonarQube, Trivy       | CloudWatch, CloudTrail, Config, Security Hub, GuardDuty        |
| **Feedback**    | GitLab                         | CloudWatch Logs, X-Ray, Security Hub                           |

---

## 📈 Benefits

- **Improved Scalability**: Transitioning from legacy tools to AWS-native services ensures better performance and availability.
- **Enhanced Security**: Integration of AWS Security Hub, GuardDuty, and WAF protects resources against threats.
- **Streamlined CI/CD**: AWS CodePipeline and CodeBuild provide end-to-end automation for faster deployments.

---

## 🏗️ Architecture

The architecture incorporates:

- **CodePipeline**: Orchestrates CI/CD workflows.
- **IAM Policies**: Enforces granular access control.
- **GuardDuty and Security Hub**: Ensure monitoring, compliance, and threat detection.
- **Transit Gateway**: Facilitates secure networking between environments.

For more details, refer to the [Architecture Guide](./docs/guides/ARCHITECTURE.md).

---

## 🤝 Contributing

To contribute to this project, please check out our [Contribution Guide](./docs/guides/CONTRIBUTING.md) for instructions on setting up your development environment and the process for submitting contributions.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---
