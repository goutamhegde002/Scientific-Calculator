# Scientific Calculator Web App

This project is a web-based scientific calculator built using **Streamlit** for the backend and **React.js** for the frontend. It supports various mathematical operations such as addition, subtraction, multiplication, division, trigonometric functions, logarithms, and more.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Advanced operations like power, square root, logarithms
- Trigonometric functions: sin, cos, tan
- Support for constants: `π (pi)` and `e`
- Interactive and easy-to-use frontend interface
- Backend API to handle calculations

## Tech Stack

- **Backend**: Python with Streamlit
- **Frontend**: React.js
- **API Communication**: Axios for sending requests from the frontend to the backend

## File Structure
```
scientific-calculator/
│
├── backend/
│   ├── app.py                 # Streamlit API
│   ├── calculator.py          # Scientific functions
│   ├── requirements.txt       # Backend dependencies
│
├── frontend/
│   ├── public/                # Public files
│   ├── src/
│   │   ├── Calculator.js      # Calculator component
│   │   ├── App.js             # Main React app file
│   │   └── App.css            # Stylesheet
│   ├── package.json           # Frontend dependencies
│   ├── package-lock.json
│
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore file

```
## How it Works

1. **Frontend**: The user inputs the mathematical operation and numbers into the React-based calculator interface.
2. **API Request**: The frontend sends a POST request to the backend using Axios, containing the operation and numbers.
3. **Backend**: The Streamlit backend receives the request, performs the calculation using the functions defined in `calculator.py`, and returns the result.
4. **Result**: The result of the calculation is displayed on the frontend interface.

---

## Available Operations

- **Basic operations**: `add`, `subtract`, `multiply`, `divide`
- **Power and square root**: `power`, `sqrt`
- **Trigonometric functions**: `sin`, `cos`, `tan`
- **Logarithmic functions**: `log`, `log10`
- **Constants**: `pi`, `e`

## Deployment

### Backend (Streamlit)

You can deploy the backend to platforms like **Streamlit Cloud**, **Heroku**, or any cloud service that supports Python.

1. **Streamlit Cloud**:
   - Go to [Streamlit Cloud](https://share.streamlit.io/) and sign in with GitHub.
   - Deploy your repository, and the backend will be live.

---

### Frontend (React.js)

You can deploy the frontend to platforms like **Netlify** or **Vercel**.

1. **Netlify**:
   - Push your code to GitHub.
   - Connect your GitHub repository to Netlify and deploy the site.

2. **Vercel**:
   - Follow a similar process by linking your GitHub repo to Vercel and deploying your React app.

---

## Known Issues

- **CORS errors** might occur when connecting the frontend and backend locally. You can resolve this by adding a CORS middleware or disabling CORS for development purposes.

---

## Future Enhancements

- Add more advanced scientific functions.
- Improve UI/UX design with better styling and responsive layout.
- Provide error messages for invalid inputs or unsupported operations.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

