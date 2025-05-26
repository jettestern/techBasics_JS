import csv
import random

def read_csv(filename):
    data = []
    try:
        with open(filename, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
        exit(1)
    return data

def populate_scores(data):
    weeks_to_add = ['week8', 'week9', 'week10', 'week11', 'week12', 'week13']
    for row in data:
        for week in weeks_to_add:
            row[week] = random.choice(['1', '2', '3', '', '-', None])
    return data

def parse_score(value):
    try:
        return float(value)
    except:
        return None

def calculate_grades(data):
    for row in data:
        week_keys = [k for k in row if k.lower().startswith('week')]
        scores = [parse_score(row[k]) for k in week_keys]
        valid_scores = sorted([s for s in scores if s is not None], reverse=True)

        total = sum(valid_scores[:10]) if valid_scores else 0
        average = sum(valid_scores) / len(valid_scores) if valid_scores else 0

        row["Total Points"] = round(total, 2)
        row["Average Points"] = round(average, 2)
    return data

def write_csv(data, output_filename):
    fieldnames = list(data[0].keys())
    with open(output_filename, "w", newline='', encoding='utf-8') as f_out:
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print("New file written:", output_filename)

def print_analysis(data):
    print("\n Average per Stream:")
    streams = {}
    for row in data:
        stream = row['Stream']
        avg = row.get("Average Points")
        if stream not in streams:
            streams[stream] = []
        streams[stream].append(float(avg))
    for s, values in streams.items():
        avg_stream = sum(values) / len(values)
        print(f"  Stream {s}: {avg_stream:.2f} Points")

    print("\n Average per Week:")
    week_cols = [k for k in data[0].keys() if k.lower().startswith("week")]
    for week in week_cols:
        values = [parse_score(row[week]) for row in data]
        valid = [v for v in values if v is not None]
        avg_week = sum(valid) / len(valid) if valid else 0
        print(f"  {week}: {avg_week:.2f} Points")

if __name__ == "__main__":
    input_filename = "Technical Basics I_2025 - Sheet1.csv"
    output_filename = "Technical_Basics_I_2025_calculated_by_yourname.csv"  # <-- Replace with your name

    data = read_csv(input_filename)
    data = populate_scores(data)
    data = calculate_grades(data)
    write_csv(data, output_filename)
    print_analysis(data)









