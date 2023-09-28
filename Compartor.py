# Define the names of your input files
file1_name = "Input.txt"
file2_name = "Legacy.txt"

# Open the input files
with open(file1_name, 'r') as file1, open(file2_name, 'r') as file2:
    # Read the lines from each file into lists
    lines1 = file1.readlines()
    lines2 = file2.readlines()

# Create a new file to store the comparison report
output_file_name = "comparison_report.txt"
with open(output_file_name, 'w') as output_file:
    # Calculate the total comparisons done
    total_comparisons = 0

    # Compare each line from file1 with each line from file2
    for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
        if line1 != line2:
            total_comparisons += 1
            output_file.write(f"Comparison {total_comparisons} (Line {i}):\n")
            output_file.write(f"Line 1: {line1.strip()}\n")
            output_file.write(f"Line 2: {line2.strip()}\n")

            # Find and report the differing portion
            for j in range(min(len(line1), len(line2))):
                if line1[j] != line2[j]:
                    output_file.write(f"Differing portion: {line1[j:j+10]} | {line2[j:j+10]}\n")
                    break

            output_file.write("\n")

print(f"Comparison report has been written to {output_file_name}")
print(f"Total comparisons done: {total_comparisons}")
