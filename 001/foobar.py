import re

def extract_sum_numbers(file_path):
    total_sum = 0

    # Mapping of textual number representations to their numeric counterparts
    text_to_number = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            # Find all words and numbers in the line
            words_numbers = re.findall(r'[a-zA-Z]+|\d', line)

            # Convert textual representations to numeric values
            converted_numbers = [text_to_number[word.lower()] if word.lower() in text_to_number else word
                                 for word in words_numbers]

            # Filter out non-numeric values and get only numbers
            numbers = [word for word in converted_numbers if str(word).isdigit()]

            # If there are at least two numbers in the line, extract and concatenate the first and last numbers
            if len(numbers) >= 2:
                first_num = numbers[0]
                last_num = numbers[-1]

                # Convert first and last numbers to strings and concatenate them
                concatenated = str(first_num) + str(last_num)

                # Convert concatenated string to an integer and add it to the total sum
                total_sum += int(concatenated)

    return total_sum

# Example usage:
input_file_path = 'sample2'
result = extract_sum_numbers(input_file_path)
print("Total sum of numbers:", result)
