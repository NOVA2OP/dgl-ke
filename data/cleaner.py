import csv

def clean_tsv_file(input_file):
    output_file = input_file.replace(".tsv", "_clean.tsv")

    with open(input_file, "r", encoding="utf-8", errors="ignore") as infile, \
         open(output_file, "w", newline="", encoding="utf-8") as outfile:

        reader = csv.reader(infile, delimiter='\t')
        writer = csv.writer(outfile, delimiter='\t')

        for row in reader:
            if len(row) == 3 and all(cell.strip() for cell in row):
                writer.writerow(row)

    print(f"Cleaned file written to: {output_file}")

# Apply to your 3 files
clean_tsv_file(r"C:\Users\mail2\OneDrive\Documents\Desktop\CollegeAssignmentsAndProjects\IP\RotateDGL\data\test.tsv")
clean_tsv_file(r"C:\Users\mail2\OneDrive\Documents\Desktop\CollegeAssignmentsAndProjects\IP\RotateDGL\data\train.tsv")
clean_tsv_file(r"C:\Users\mail2\OneDrive\Documents\Desktop\CollegeAssignmentsAndProjects\IP\RotateDGL\data\valid.tsv")
