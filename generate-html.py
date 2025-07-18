import sys

import pandas as pd
import os

# === SETTINGS ===
INPUT_FILE = sys.argv[1]
 # <- your spreadsheet filename
OUTPUT_FOLDER = "textbook-solutions"  # <- output folder in your GitHub repo

# === LOAD DATA ===
df = pd.read_excel(INPUT_FILE)

# === ENSURE OUTPUT FOLDER EXISTS ===
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# === GENERATE FILES ===
for _, row in df.iterrows():
   
    page = row["page"]
    exercise = row["exercise"]
    step1 = row["step1"]
    step2 = row["step2"]
    step3 = row["step3"]
    result = row["result"]
    back_file = row["back_file"]
    next_file = row["next_file"]
    chapter_file = row["chapter_file"]

    file_name = f"page-{page}-exercise-{exercise.lower().replace('exercise ', '').replace(' ', '').strip()}.html"
    file_path = os.path.join(OUTPUT_FOLDER, file_name)

    html = f"""<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8' />
  <meta name='viewport' content='width=device-width, initial-scale=1.0' />
 <title>Page {page}: {exercise} | Studying Smart</title>
  <link href='https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap' rel='stylesheet' />
  <script src='https://cdn.tailwindcss.com'></script>
  <style>
    body {{
      font-family: 'Inter', sans-serif;
    }}
    .step-box {{
      @apply transform transition hover:scale-[1.02] hover:shadow-lg;
    }}
  </style>
</head>
<body class='bg-white text-[#1D3557] min-h-screen flex flex-col'>
  <nav class='bg-[#1D3557] text-white px-6 py-4 flex justify-between items-center shadow sticky top-0 z-50'>
    <div class='text-2xl font-bold'>Studying Smart</div>
    <div class='flex items-center space-x-6 text-sm font-medium'>
      <a href='#' class='hover:text-[#A8DADC] transition'>Home</a>
      <a href='#' class='hover:text-[#A8DADC] transition'>Subjects</a>
      <a href='#' class='hover:text-[#A8DADC] transition'>Book Guides</a>
      <a href='#' class='hover:text-[#A8DADC] transition'>Textbook Solutions</a>
      <a href='#' class='hover:text-[#A8DADC] transition'>About</a>
    </div>
  </nav>
  <main class='flex-1 px-6 py-10 sm:px-10'>
    <div class='max-w-4xl mx-auto'>
      <div class='mb-4'>
        <a href='{chapter_file}' class='text-[#0077B6] underline underline-offset-2 font-medium hover:text-[#005f99] transition'>
          ← Back to Chapter
        </a>
      </div>
      <div class='text-center mb-10'>
        <p class='text-sm uppercase tracking-wide text-[#0077B6] font-semibold'>Campbell Biology</p>
        <h1 class='text-4xl font-extrabold mt-1 mb-1'>Page {page}: {exercise}</h1>
      </div>
      <div class='bg-[#E0F2FE] p-8 sm:p-10 rounded-2xl shadow-xl space-y-10'>
        <div class='step-box'>
          <p class='text-base leading-relaxed'><strong>STEP 1</strong><br>{step1}</p>
        </div>
        <div class='step-box'>
          <p class='text-base leading-relaxed'><strong>STEP 2</strong><br>{step2}</p>
        </div>
        <div class='step-box'>
          <p class='text-base leading-relaxed'><strong>STEP 3</strong><br>{step3}</p>
        </div>
        <div class='border border-black rounded-md p-4 bg-white'>
          <p class='text-xl font-bold text-[#1D3557]'>Result: {result}</p>
        </div>
      </div>
      <div class='flex justify-between mt-10'>
        <a href='{back_file}' class='flex items-center space-x-2 bg-[#1D3557] text-white px-5 py-2 rounded-xl hover:bg-[#16324c] transition shadow'>
          <svg xmlns='http://www.w3.org/2000/svg' class='h-5 w-5' fill='none' viewBox='0 0 24 24' stroke='currentColor'>
            <path stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M15 19l-7-7 7-7' />
          </svg>
          <span>Back</span>
        </a>
        <a href='{next_file}' class='flex items-center space-x-2 bg-[#1D3557] text-white px-5 py-2 rounded-xl hover:bg-[#16324c] transition shadow'>
          <span>Next</span>
          <svg xmlns='http://www.w3.org/2000/svg' class='h-5 w-5' fill='none' viewBox='0 0 24 24' stroke='currentColor'>
            <path stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M9 5l7 7-7 7' />
          </svg>
        </a>
      </div>
    </div>
  </main>
  <footer class='bg-[#1D3557] text-white text-center py-6 mt-16'>
    <div class='space-x-4 mb-2 text-sm'>
      <a href='#' class='hover:underline'>Terms</a>
      <a href='#' class='hover:underline'>Privacy</a>
      <a href='#' class='hover:underline'>Contact</a>
    </div>
    <p class='text-sm'>&copy; 2025 Studying Smart. All rights reserved.</p>
  </footer>
</body>
</html>"""

    with open(file_path, "w") as f:
        f.write(html)

print(f"✅ All HTML files have been generated into the '{OUTPUT_FOLDER}' folder.")
