📦 PINAKSAGENT 2.0 – Deployment Guide (by PINAK for Keshav)

STEP 1: GitHub Setup
---------------------
1. Go to GitHub (https://github.com)
2. Create New Repository - name it pinaksagent2.0
3. Don't select “Add README” or “.gitignore”
4. Extract ZIP locally and upload all files via drag-drop

STEP 2: Render.com Setup
-------------------------
1. Visit https://dashboard.render.com
2. Click on New → Web Service
3. Connect GitHub and choose pinaksagent2.0 repo

Settings:
- Environment: Python
- Build Command: pip install -r requirements.txt
- Start Command: uvicorn main:app --host=0.0.0.0 --port=10000

4. Click Deploy
5. You'll get a public URL like https://pinaksagent2.onrender.com

TESTING:
- Enter prompt → video will be generated → link provided

✅ All done!