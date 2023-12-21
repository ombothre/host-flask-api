# Improved Flask API

This project is an improvement upon the [local svm api](https://github.com/ombothre/flask-api), now hosted on [PythonAnywhere](https://om1024.pythonanywhere.com/).

## API Endpoint

The Flask API is hosted [here](https://om1024.pythonanywhere.com/).

**Note**
Route `/predict` is to be used directly to post request and for exploring go to route `/`

## Usage

To use the API:
- Send a POST request to the `/predict` endpoint with JSON data containing the input for prediction.
- You can download api-test.py to test the api
- Example using `curl`:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"input": {"gender": "Male", "age": 30, "salary": 50000}}' https://om1024.pythonanywhere.com/predict
    ```

### Request Format

The JSON body should contain the following format:
```json
{
    "input": {
        "gender": "Male",
        "age": 30,
        "salary": 50000
    }
}
