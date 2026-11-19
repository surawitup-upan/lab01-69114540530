def to_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def is_pass(score):
    return score >= 50


def average(scores):
    return sum(scores) / len(scores) if scores else 0


if __name__ == "__main__":
    scores = [85, 72, 64, 91]
    print("Average:", average(scores))
    print("Grade:", to_grade(average(scores)))