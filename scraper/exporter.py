import csv

def export_to_csv(listings, filename):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "address", "price", "beds", "baths", "sqft", "lot_hoa_walk", "agent", "url"
        ])
        writer.writeheader()
        for row in listings:
            row["lot_hoa_walk"] = "; ".join(row.get("lot_hoa_walk", []))
            writer.writerow(row)
    print(f"[💾 CSV Exported] {filename} written successfully.")
