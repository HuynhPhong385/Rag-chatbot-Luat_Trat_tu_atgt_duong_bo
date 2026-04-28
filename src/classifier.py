def classify_question(question):
    q = question.lower()

    if any(keyword in q for keyword in ["phạt", "bao nhiêu", "tiền"]):
        return "xu_phat"

    if any(keyword in q for keyword in ["có bị cấm", "được phép", "hợp pháp"]):
        return "luat"

    return "unknown"
