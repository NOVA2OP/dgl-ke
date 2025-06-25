# Optional quick check
for name in ["train_clean.tsv", "valid_clean.tsv", "test_clean.tsv"]:
    with open(f"data/{name}", 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            parts = line.strip().split('\t')
            if len(parts) != 3:
                print(f"{name} - Line {i} malformed: {parts}")
