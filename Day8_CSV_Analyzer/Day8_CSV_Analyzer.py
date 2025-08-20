import csv

def process_csv(input_file, output_file):
    try:
        students = []

        # --- Step 1: Read CSV ---
        with open(input_file, mode='r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                try:
                    # Convert subject marks to integers
                    marks = [int(row[f"Subject{i}"]) for i in range(1, 6)]
                    
                    total = sum(marks)
                    percentage = total / 5
                    
                    students.append({
                        "Name": row["Name"],
                        "Roll Number": row["Roll Number"],
                        "Total": total,
                        "Percentage": percentage
                    })
                
                except ValueError:
                    print(f"⚠️ Data type error for student {row['Name']}. Skipping entry.")
        
        # --- Step 2: Identify Top 3 Performers ---
        top_students = sorted(students, key=lambda x: x["Percentage"], reverse=True)[:3]

        # --- Step 3: Students with <40% ---
        re_test = [s for s in students if s["Percentage"] < 40]

        # --- Display Results ---
        print("\n🏆 Top 3 Performers:")
        for s in top_students:
            print(f"{s['Name']} ({s['Roll Number']}) - {s['Percentage']:.2f}%")

        print("\n❌ Students for Re-Test (<40%):")
        for s in re_test:
            print(f"{s['Name']} ({s['Roll Number']}) - {s['Percentage']:.2f}%")

        # --- Step 4: Write Results to New CSV ---
        with open(output_file, mode='w', newline='') as file:
            fieldnames = ["Name", "Roll Number", "Total", "Percentage", "Result"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            for s in students:
                result = "Pass" if s["Percentage"] >= 40 else "Fail"
                writer.writerow({
                    "Name": s["Name"],
                    "Roll Number": s["Roll Number"],
                    "Total": s["Total"],
                    "Percentage": f"{s['Percentage']:.2f}",
                    "Result": result
                })

        print(f"\n✅ Results written to {output_file}")

    except FileNotFoundError:
        print(f"⚠️ Error: File '{input_file}' not found.")


# Run the function
process_csv("students.csv", "results.csv")
