from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

@app.get("/")
def init(query: str):
  try:
        response = requests.get(f"https://gpt4-apihubforblind.onrender.com/?msg={query}")
        response_data = response.json()

        if response.status_code == 200:
            return {
                "statusCode": "200",
                "developer": "Master Dara",
                "TGChannel": "https://t.me/I_T_L189",
                "message": response_data.get("message", "Null")
            }
        else:
            return {
                "statusCode": "400",
                "developer": "Master Dara",
                "error": "Unab		 to get API Response"
            }
    except Exception as error:
        return {
            "statusCode": "400",
            "developer": "Master Dara",
            "error": str(error)
        }
