from flask import Flask, render_template, request, send_file
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

app = Flask(__name__)

PDF_PATH = 'menu.pdf'

def extract_items(category, count):
    items = pd.read_csv('menu.csv', encoding='utf-8')  # Siguro që përdor kodimin e duhur
    items.columns = items.columns.str.strip()  # Hiq hapësirat në emrat e kolonave
    return items[items['Tipi i pjates'] == category][['Emri I Pjates', 'Cmimi']].head(count)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/menu', methods=['POST'])
def menu():
    # Retrieve item counts from the form
    count_pjate_e_pare = int(request.form['pjate_e_pare'])
    count_pjate_kryesore = int(request.form['pjate_kryesore'])
    count_embelsire = int(request.form['embelsire'])
    count_pije = int(request.form['pije'])

    # Extract menu.csv items based on the requested counts
    pjate_e_pare = extract_items('Pjate e Pare', count_pjate_e_pare)
    pjate_kryesore = extract_items('Pjate Kryesore', count_pjate_kryesore)
    embelsire = extract_items('Embelsire', count_embelsire)
    pije = extract_items('Pije', count_pije)

    # Render menu.csv page with the extracted items
    return render_template('menu.html', pjate_e_pare=pjate_e_pare, pjate_kryesore=pjate_kryesore, embelsire=embelsire,
                           pije=pije)


@app.route('/download')
def download():
    # Generate the PDF
    c = canvas.Canvas(PDF_PATH, pagesize=letter)

    c.setFont("Helvetica", 12)
    c.drawString(100, 750, "Restaurant Menu")

    # Add Pjate e Pare section
    c.drawString(100, 730, "Pjate e Pare:")
    y_position = 710
    for _, row in extract_items('Pjate e Pare', 5).iterrows():  # Limit to 5 items for simplicity
        c.drawString(120, y_position, f"{row['Emri I Pjates']} - {row['Cmimi']} ALL")
        y_position -= 15

    # Add Pjate Kryesore section
    c.drawString(100, y_position - 10, "Pjate Kryesore:")
    y_position -= 20
    for _, row in extract_items('Pjate Kryesore', 5).iterrows():
        c.drawString(120, y_position, f"{row['Emri I Pjates']} - {row['Cmimi']} ALL")
        y_position -= 15

    # Add Embelsire section
    c.drawString(100, y_position - 10, "Embelsire:")
    y_position -= 20
    for _, row in extract_items('Embelsire', 5).iterrows():
        c.drawString(120, y_position, f"{row['Emri I Pjates']} - {row['Cmimi']} ALL")
        y_position -= 15

    # Add Pije section
    c.drawString(100, y_position - 10, "Pije:")
    y_position -= 20
    for _, row in extract_items('Pije', 5).iterrows():
        c.drawString(120, y_position, f"{row['Emri I Pjates']} - {row['Cmimi']} ALL")
        y_position -= 15

    c.save()

    # Return the PDF file for download
    return send_file(PDF_PATH, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
