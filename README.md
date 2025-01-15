# AI Photo Enhancer

This project enhances the quality of photos using AI-powered super-resolution technology. It uses **Real-ESRGAN** as the model for photo enhancement, with a **FastAPI** backend and a **Streamlit** frontend for user interaction.

## Features

- Upload a low-resolution photo.
- Enhance the photo using AI.
- View the original and enhanced photos side-by-side.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/razvan234/Ai-Photo-Enhacer.git
   cd Ai-Photo-Enhacer
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download model weights:**
   - Download the Real-ESRGAN model weights and place them in the `weights/` folder.

4. **Start the backend:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Start the frontend:**
   ```bash
   streamlit run app.py
   ```

## Directory Structure

```
Ai-Photo-Enhancer/
├── app.py          # Streamlit frontend
├── main.py         # FastAPI backend
├── static/         # Storage for uploaded and enhanced images
│   ├── uploads/    # Uploaded images
│   └── enhanced/   # Enhanced images
├── weights/        # Real-ESRGAN model weights
├── requirements.txt # Dependencies
└── README.md       # Documentation
```

## Usage

1. Open the Streamlit app in your browser.
2. Upload a photo using the interface.
3. Click the "Upload and Enhance" button.
4. View the original and enhanced photos.

## Acknowledgments

- **[Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN):** AI model for photo enhancement.
- **[FastAPI](https://fastapi.tiangolo.com/):** Backend framework.
- **[Streamlit](https://streamlit.io/):** Frontend framework.

---

Enjoy enhancing your photos!
