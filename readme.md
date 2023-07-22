# Syllabus Condenser

## Overview

Syllabus Condenser is a natural language processing (NLP) based project that aims to summarize syllabuses and generate answers to questions based on the uploaded syllabus and question paper. The system uses NLP techniques to process the input files, extracts relevant content, and stores the data in MongoDB for efficient retrieval. With the help of an API from OpenAI, the system can generate accurate answers to user prompts using the stored data.

## Features

- Syllabus Summarization: The project allows users to upload syllabus documents, and the system generates a concise summary of the syllabus content using NLP techniques.

- Question Answering: Users can upload question papers, and the system can answer user prompts related to the syllabus based on the content extracted from the uploaded files.

- MongoDB Integration: Extracted syllabus content is stored in MongoDB, organized by the name of the subject uploaded. This enables efficient data retrieval for generating answers to user prompts.

- NLP Techniques: The project utilizes various NLP techniques, including tokenization, segmentation, and summarization, to process and analyze text data.

- OpenAI API Integration: To generate accurate answers to user prompts, the system leverages an API from OpenAI, which provides advanced language processing capabilities.

## Requirements

- Python 3.x
- MongoDB
- OpenAI API Key

## Installation

1. Clone the repository from GitHub:

2. Install the required Python packages:


3. Set up MongoDB:
- Install MongoDB on your machine and start the MongoDB server.
- Create a database named 'syllabus_data' to store the extracted syllabus content.

4. Get OpenAI API Key:
- Sign up for an account on OpenAI (https://openai.com/) to get an API key.
- Add the API key to the project's configuration file.

## Usage

1. Upload Syllabus:
- Use the web interface to upload syllabus documents in PDF format.
- The system will process the uploaded files, extract relevant content, and store it in the MongoDB database.

2. Upload Question Paper:
- Upload question papers in PDF format to enable the system to answer user prompts based on the syllabus content.

3. Generate Answer:
- Provide a user prompt related to the syllabus content.
- The system will use the prompt, retrieve relevant information from the MongoDB database, and generate an accurate answer using the OpenAI API.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- OpenAI (https://openai.com/): We acknowledge the use of OpenAI's language processing API, which enhances the question-answering capabilities of our project.

## Support

For any issues or inquiries, please contact:
- Email: your-email@example.com
- GitHub repository: https://github.com/your-username/syllabus-condenser

