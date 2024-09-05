# Phishing URL Detection Tool

Developed by **Bansi Patel**, this project is a machine learning-based tool designed to detect phishing URLs. It uses a combination of feature extraction and a Naive Bayes classifier to determine whether a given URL is phishing or legitimate. The tool is built using Python, Scikit-learn, Flask, and other essential libraries.

## **Table of Contents**
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [How It Works](#how-it-works)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## **Introduction**
Phishing is a cybercrime where attackers attempt to obtain sensitive information such as usernames, passwords, and credit card details by disguising themselves as trustworthy entities. This tool, created by Bansi Patel, helps detect such phishing attempts by analyzing the URLs using machine learning techniques.

## **Features**
- Detects phishing URLs using a trained machine learning model.
- User-friendly web interface for URL input and detection.
- Real-time predictions with a clear indication of whether the URL is phishing or not.

## **Technologies Used**
- **Python 3.x**: Programming language used for the backend and machine learning model.
- **Flask**: Micro web framework for building the web interface.
- **Scikit-learn**: Used for building and training the machine learning model.
- **Pandas**: For data manipulation and analysis.
- **Joblib**: For saving and loading the trained model.
- **HTML/CSS**: For the web interface design.

## **Installation**

1. **Clone the Repository:**
   ```bash
   https://github.com/Bansipatel083/phishing-detection-for-url.git
   cd phishing-detection-for-url
2. **Create a Virtual Environment:**

    ```bash
    Copy code
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
3.**Install the Required Packages:**

    '''bash

    pip install -r requirements.txt



The application will start running on http://127.0.0.1:5000/. Open this URL in your browser to access the tool.
## Usage
    Open the web application in your browser.
    Enter a URL in the input field and click "Check URL".
    The application will display whether the URL is phishing or not.
## Project Structure
    python
    '''bash
    phishing-url-detection/
    │             # Main Flask application file
    ├── data/
    │   └── phishing_dataset.csv  # Dataset file (replace with your actual dataset) # Saved trained model 
    ├── model/
    │   └── train_model.py        # Script for training the phishing detection model 
    ├── static/
    │   └── styles.css            # CSS file for styling the web page
    ├── templates/
    │   └── index.html            # HTML file for the weinterface
    ├── app.py                    # Main Flask application file
    ├── phishing_model.pkl        # Saved trained model
    ├── requirements.txt          # List of required Python packages
    └── README.md                 # Project documentation


## How It Works
Data Preprocessing: URLs are vectorized using TfidfVectorizer, which converts them into numerical feature vectors.
Model Training: The MultinomialNB classifier is trained on these vectors to learn patterns indicative of phishing.
Prediction: When a new URL is input, it goes through the same vectorization process and is classified as either phishing or not.
## Testing
Use both phishing and non-phishing URLs to test the tool's accuracy.
## Example URLs:
Phishing: http://secure-update-paypal.com/login
Non-Phishing: https://www.amazon.com
## Contributing
Contributions are welcome! If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Created and maintained by Bansi Patel. If you have any questions or suggestions, feel free to open an issue or contact directly.

vbnet
Copy code

### **Key Additions:**
- The README now explicitly credits Bansi Patel as the author and creator of the project.
- The contact section invites users to reach out with questions or suggestions, reflecting the personal involvement in the project.

Feel free to further personalize or adjust this document to better suit your project presentation style!






