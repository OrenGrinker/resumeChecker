from extractors import extract_text_from_pdf, extract_text_from_docx


def process_resumes(uploaded_files):
    candidates = []
    for uploaded_file in uploaded_files:
        try:
            if uploaded_file.type == "application/pdf":
                text = extract_text_from_pdf(uploaded_file)
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                text = extract_text_from_docx(uploaded_file)
            else:
                continue
            candidates.append({"name": uploaded_file.name, "text": text})
        except Exception as e:
            # Log error and continue processing other files
            print(f"Error processing {uploaded_file.name}: {str(e)}")
    return candidates


def find_suitable_candidates(client, candidates, query):
    suitable_candidates = []

    for candidate in candidates:
        user_content = (
            f"Given the following resume, determine if this candidate is suitable for the following query: {query}. "
            f"Please respond with 'Suitable' if the candidate matches the requirements or 'Not suitable' if they do not. "
            f"If suitable, also provide a brief summary of relevant experience and include the candidate's contact information.\n\n"
            f"Resume:\n{candidate['text']}"
        )

        try:
            summary = client.chat_completion(user_content)

            if "Suitable" in summary:
                contact_info = extract_contact_info(summary)
                suitable_candidates.append({
                    "name": candidate["name"],
                    "summary": summary,
                    "contact_info": contact_info,
                    "text": candidate["text"]
                })
        except Exception as e:
            print(f"Error processing candidate {candidate['name']}: {str(e)}")

    return suitable_candidates


def extract_contact_info(summary):
    # Implement your logic to extract contact info from the summary
    contact_info = "Extracted contact info placeholder"
    return contact_info
