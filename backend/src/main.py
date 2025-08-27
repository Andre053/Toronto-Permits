from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


"""
fastapi dev main.py

"""

app = FastAPI()

# who can make cross-origin requests
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

SAMPLE_STATS = {
    "M5V": {
            "population": 1000, 
            "income": 1000
        }

}


@app.get("/")
async def root():
    return {"message": "Hallo, World!"}

@app.get("/stats/{fsa_code}")
async def stats(fsa_code: str):

    # lookup the fsv code and get the stats
    print("Received FSA code:", fsa_code)
    if fsa_code in SAMPLE_STATS:
        stats = SAMPLE_STATS[fsa_code]
    else: stats = {"population": 0, "income": 0}
    return stats


