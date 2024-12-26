# ManualListSorter

**ManualListSorter** is a web-based application that helps users prioritize their ideas through a systematic comparison process. Built using Flask, the application allows users to input a list of ideas and sort them based on pairwise comparisons, leveraging binary search for efficient sorting.

## Features

- **Input Management**: Users can submit a list of ideas via a simple form.
- **Interactive Comparison**: Compare two ideas at a time to determine their relative priority.
- **Efficient Sorting**: Implements binary search to minimize the number of comparisons needed.
- **Responsive Interface**: Modern and user-friendly HTML templates for desktop and mobile devices.
- **Result Presentation**: Displays the prioritized list of ideas in a clear, ordered format.

## File Structure

```
ManualListSorter/
├── app.py                      # Main Flask application
├── match_amount_calculator.py  # Script for calculating comparison statistics
├── templates/                  # HTML templates for the application
│   ├── compare.html            # UI for pairwise idea comparison
│   ├── index.html              # Input form for submitting ideas
│   └── result.html             # Displays the sorted list of ideas
```

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Flask library

Install the dependencies by running:
```bash
pip install flask
```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ManualListSorter.git
   cd ManualListSorter
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

### Usage

1. On the homepage, enter each idea on a new line and click **Start Prioritizing**.
2. Compare pairs of ideas presented to you and select the one you prefer.
3. Once all comparisons are complete, view the sorted list of ideas on the results page.

### Additional Tool: Comparison Calculator

Use `match_amount_calculator.py` to estimate the number of comparisons required for sorting:
```bash
python match_amount_calculator.py
```
Input the number of ideas, and the script will calculate:
- Minimum total comparisons
- Maximum total comparisons
- Average total comparisons