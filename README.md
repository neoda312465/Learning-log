# FastAPI Auth + CRUD API
This is a Backend API which lets users signup, login, create and manage their own items securily

## Features
- Full CRUD
- user authentication
- JWT based access sessions
- ownership-based access control

## Techstack
- FastAPI
- SQLModel, SQLite
- Passlib (bcrypt)
- Python-jose (JWT)

## Setup
1. Clone the repository
   \`\`\`bash
   git clone https://github.com/neoda312465/Learning-log.git
   cd Learning-log
   \`\`\`

2. Install dependencies
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. Run the server
   \`\`\`bash
   fastapi dev main.py
   \`\`\`

4. Open the interactive docs
   \`\`\`
   http://127.0.0.1:8000/docs
   \`\`\`

## API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|--------------|----------------|
| POST | /signup | Create a new user account | No |
| POST | /login | Log in and receive a JWT access token | No |
| GET | /items | Get all items | No |
| POST | /items | Create a new item (assigned to logged-in user) | Yes |
| GET | /items/{item_id} | Get a single item by ID | No |
| PUT | /items/{item_id} | Update an item (must be the owner) | Yes |
| DELETE | /items/{item_id} | Delete an item (must be the owner) | Yes |

## What I Learned
- This was my first project including FastAPI, so I learned how that works
- At first I relied on AI for the coding, but after finishing full CRUD, I was writing and debugging the logic myself.
- I learned about the concept of what to let users enter themselves and what not to prevent the database from breaking
- The hardest bug was a version incompatibility between passlib and bcrypt — no matter how short my password was, it kept saying "password longer than 72 bytes." Fixed by pinning bcrypt to a compatible version.
- Auth was the hardest overall concept — linking users and items across signup, login, JWT tokens, and ownership checks. It took longest because every piece depended on the others, so I couldn't stop halfway.
- Hashing could be verified right in VS Code, but past that point I had to use Postman to properly test things like authorization headers and multi-user data.
 