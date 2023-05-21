
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    """ Summary
    create the get method for checking first fast api app route
    Returns:
        simple message
    """
    return {"Message":"Welcome in Fast API ",
            "Doc string" : root.__doc__}
    
@app.get("/post") 
def get_post():
    """_summary_
    Create a route to get all post

    Returns:
        _type_: list of post in form of dict
    """
    return {"Message":"list of all post"}

