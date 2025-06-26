## Open a terminal
- We can use venv

### Install dependencies if it is not there in your venv and run the following command,

```
pip install -r requirements.txt
```
### Create DB
```
python create_db.py
```
### Create a collection which is used by MCP server to reply user Query
```
python create_city_attractions_db.py
```
### Run MCP Server
```
python run_mcp.py
```
## Open Another Terminal(split):

- Activate your venv and run,

```
python app.py
```
