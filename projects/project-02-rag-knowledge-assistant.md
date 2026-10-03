# Project 02: RAG Knowledge Assistant

## Goal

Build a small knowledge assistant that answers questions grounded in a local document set.

## Suggested scope

Use a small set of business, policy, or SOP documents and ask the assistant to answer only questions supported by those documents.

## Core design

- retrieve relevant documents
- summarize the relevant section
- answer using grounded evidence
- mark unsupported answers as unknown

## Required steps

1. Prepare a small knowledge base
2. Add a retrieval layer
3. Prompt the model to answer only from retrieved content
4. Add a fallback for unsupported questions
5. Validate with a few test questions

## Good evaluation questions

- What does policy X say?
- What is the process for Y?
- Which part of the SOP is relevant to this workflow?
- If the answer is not in the docs, return “not found” instead of guessing

## Success criteria

- no invented facts
- less than 10% unsupported answers in evaluation set
- answer traces show evidence from source docs

## Stretch ideas

- add chunk filtering
- add metadata tags
- add source citations in output
