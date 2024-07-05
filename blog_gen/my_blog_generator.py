# -*- coding: utf-8 -*-
"""My Blog Generator

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ra0aEvyr3DrA6j38ddNgHm4U_UrFPwKm

# Project 1: Blog Generator with OpenAI API

Welcome to the first project of our course! In this section, we'll embark on an exciting journey to build a Blog Generator using the powerful OpenAI API. Our goal is to create an intelligent system capable of generating engaging and coherent blog content with just a prompt from the user. This project will not only introduce you to the world of AI-driven content creation but also demonstrate the practical application of the OpenAI API within a real-world scenario.

## What You Will Learn

- **OpenAI API Overview**: Gain a solid understanding of the OpenAI API and its capabilities for natural language processing and generation.
- **Setting Up Google Colab**: Familiarize yourself with Google Colab, an ideal platform for running Python code and integrating APIs in a cloud-based environment.
- **Prompt Engineering**: Develop skills in crafting prompts that guide the AI to produce the desired output, a critical aspect of leveraging generative language models.
- **Content Generation**: Understand how to generate text that is coherent, contextually relevant, and stylistically appropriate for blog posts.

## Project Objectives

By the end of this project, you will have created a Blog Generator that can:

1. **Take User Input**: Accept user-defined prompts or topics to generate content about.
2. **Generate Blog Posts**: Produce complete blog posts that are ready for publication, including titles, headers, and paragraphs.
3. **Display Results**: Present the generated blog posts in a clear and organized format within Google Colab.

## Before We Start

Make sure you have:
- A Google Colab account set up.
- Basic knowledge of Python programming.
- An OpenAI API key (you can obtain one from [OpenAI](https://platform.openai.com/account/api-keys)).

## Let's Build!

Are you ready to dive into the world of AI and transform the way blog content is created? Let's get started on building your very own Blog Generator using the OpenAI API!

# 2. Libraries import
"""

pip install openai

import os
import openai

from openai import OpenAI

"""# 3. Sending a first request to OpenAI API


### 3.1 Setting up API Key
"""

os.environ["OPENAI_API_KEY"] = "sk-proj-DLbPDOnYvszGBPfHyHZzT3BlbkFJR5ZzzsMHfnDKdbbcNte6"
client = OpenAI()

"""### 3.2 OpenAI available models"""

print(client.models.list())

"""Find about the Completion endpoint and all of its arguments: https://platform.openai.com/docs/api-reference/completions/create"""

client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt="Tell me about cricket in india",
)

"""# 4. Building our Blog generator"""

response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt="Generate a blog about importance of sports",
    temperature=0.9,
    max_tokens=400,
)

response

print(response.choices[0].text)

prompt = """
You are a copy writer with years of experience writing impactful blog that converge and help elevate brands.
Your task is to write a blog on any topic system provides you with. Make sure to write in a format that works for Medium.
Each blog should be separated into segments that have titles and subtitles. Each paragraph should be three sentences long.

Topic: fitness
Additiona pointers: consider health benefits
"""

response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt,
    temperature=1,
    max_tokens=400,
)

response.choices[0].text

"""### 4.2 Accepting user inputs"""

topic = input("Enter a topic: ")
additional_pointers = input("Enter any additional pointers, if any: ")

prompt = f"""
You are a copy writer with years of experience writing impactful blog that converge and help elevate brands.
Your task is to write a blog on any topic system provides you with. Make sure to write in a format that works for Medium.
Each blog should be separated into segments that have titles and subtitles. Each paragraph should be three sentences long.

Topic: {topic}
Additiona pointers: {additional_pointers}
"""

response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt,
    temperature=1,
    max_tokens=700,
)

print(response.choices[0].text)

