marks = {
    "Aman": "78",
    "Ravi": "abc",
    "Neha": "85",
    "Sita": "40"
}
def data_analyzer(marks): 
    valid = {}
    invalid = []
    total = 0
    count = 0

    for name, value in marks.items() :
        try:
            result = int(value)
            valid[name] = result
            total += result
            count += 1

        except ValueError:
            invalid.append(name)
    average = round(total/count, 2)

    return {
        "valid" : valid,
        "invalid" : invalid,
        "average" : average
    }

print(data_analyzer(marks))   
   