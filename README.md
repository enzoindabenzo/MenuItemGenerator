# Restaurant Menu Generator

This project allows restaurants to dynamically generate and download a customizable menu in PDF format. The application allows users to choose the number of items for different sections like "Pjate e Pare", "Pjate Kryesore", "Embelsire", and "Pije" and then generates a PDF menu based on those selections.

## Features

- Select and generate menu items for multiple categories: "Pjate e Pare", "Pjate Kryesore", "Embelsire", and "Pije".
- Generate a downloadable PDF version of the restaurant's menu.
- Simple and intuitive interface using Flask for web-based interaction.

## Installation

Follow these steps to set up the project locally.

### Prerequisites

- Python 3.x
- Flask
- ReportLab (for PDF generation)
- Other dependencies listed in `requirements.txt`

### Steps to Set Up

1. **Clone the repository:**
   ```bash
   git clone https://github.com/enzoindabenzo/MenuItemGenerator.git
   ```

2. **Navigate into the project directory:**
   ```bash
   cd MenuItemGenerator
   ```

3. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment:**
   - For Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - For Mac/Linux:
     ```bash
     source venv/bin/activate
     ```

5. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the application:**
   ```bash
   python app.py
   ```

The app should now be accessible at `http://127.0.0.1:5000/` in your web browser.

## Usage

- Navigate to the web page.
- Input the number of items you want in each section of the menu (e.g., "Pjate e Pare", "Pjate Kryesore", etc.).
- Click the "Generate Menu" button to see a preview of the generated menu.
- Click the "Download Menu" button to download the generated menu as a PDF.

## Project Structure

- **app.py**: Main Flask application file handling the routing and PDF generation.
- **templates/menu.html**: HTML template for rendering the menu.
- **static/**: Contains static files like CSS or images (if needed).
- **menu.csv**: The CSV file containing the restaurant's menu items.


The `extract_items` function filters and selects the relevant items based on the user’s input, ensuring that the appropriate number of items is extracted from the CSV.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
