# Tech Connect 2025

## Session: Intelligent Inventory Manager Solution with GPT-4o

### Abstract

Demonstrate how to create an automated and Intelligent Inventory Manager solution capable of ingesting data in various formats (documents or pictures), extract objects, and validate product availability in a Datawarehouse.

### Solution requirements

* Customers will inquire about specific product names, technical characteristics, or descriptions of the desired product.
* The products sold by the client include a wide variety of nutritional supplements.
* The system should ingest data in various formats (.jpg, .png, .docx, .pdf, and others) and extract the content related to the product request.
* Based on the information provided by the customer, the system must query the database to verify the product's availability.
* If the product is not available, the system should suggest alternative products based on the database inventory.
* The solution must be fully automated without human intervention.

## Getting Started

Repository folder structure:

* **[images-aisearch](./images-aisearch/):** Pictures of nutrional supplements previously loaded into Azure AI Search. Each picture represents a document inside the Inventory Manager Azure AI Search Database.

* **[images-lab-tests](./images-lab-tests/):** Pictures used during the laboratories to query the existence of products (documents) inside Azure AI Search.

* **[labs](./labs/):** Demos executed during the workshop.

## Environment Setup Instructions

We have created a **[Course Setup](./00-course-setup/README.md)** section to help you with setting up your development environment to execute the code and the labs.

## Reference

Add data
