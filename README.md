# DALLE API - Example

# Setup environment
Copy .env.template to .env and pass your api key from openai website.

```shell
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

# Output
```json
{
   "created":1694185658,
   "data":[
      {
         "url":"https://oaidalleapiprodscus.blob.core.windows.net/private/org-468O4rdTWREgI5o7kqSJ8E8W/user-fu6XMWzcOWcuNkXksvO4ieJs/img-KLIKyVN3gx7MYKlWmRJrvZO5.png?st=2023-09-08T14%3A07%3A38Z&se=2023-09-08T16%3A07%3A38Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-09-07T18%3A16%3A05Z&ske=2023-09-08T18%3A16%3A05Z&sks=b&skv=2021-08-06&sig=ky59o/pMXVsQUfOldF%2B1YNHY%2Be6IcZMUzDobhNT5CGo%3D"
      }
   ]
}
```