import csv


def main():
    with open("dataframe.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        rows = [{k: (v or "") for k, v in row.items()} for row in reader]

    with open("head.md", "r") as inp:
        out = inp.read()

    categories = dict.fromkeys(row["category"] for row in rows)
    for category in categories:
        category_rows = [row for row in rows if row["category"] == category]
        out += f"## {category}\n\n"

        subcategories = dict.fromkeys(row["subcategory"] for row in category_rows)
        for subcategory in subcategories:
            subcategory_rows = [row for row in category_rows if row["subcategory"] == subcategory]
            if subcategory:
                out += f"### {subcategory}\n\n"
            for row in subcategory_rows:
                out += f"- [{row['name']}]({row['url']}): {row['description']}\n"
            out += "\n"

    with open("README.md", "w") as outf:
        outf.write(out)

if __name__ == "__main__":
    main()
